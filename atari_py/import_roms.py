import os
import hashlib
import shutil
import zipfile
import argparse

from .games import get_games_dir


SCRIPT_DIR = os.path.abspath(os.path.dirname(__file__))
MD5_CHUNK_SIZE = 8096


def _check_zipfile(f, process_f):
    with zipfile.ZipFile(f) as zf:
        for entry in zf.infolist():
            _root, ext = os.path.splitext(entry.filename)
            with zf.open(entry) as innerf:
                if ext == ".zip":
                    _check_zipfile(innerf, process_f)
                else:
                    process_f(innerf)


def _calc_md5(f):
    h = hashlib.md5()
    while True:
        chunk = f.read(MD5_CHUNK_SIZE)
        if chunk == b'':
            break
        h.update(chunk)
    return h.hexdigest()


def import_roms(dirpath="."):
    md5s = {}
    copied_md5s = set()

    with open(os.path.join(SCRIPT_DIR, "ale_interface", "md5.txt")) as f:
        f.readline()
        f.readline()
        for line in f:
            hexdigest, filename = line.strip().split(' ')
            md5s[hexdigest] = os.path.join(get_games_dir(), filename)

    def save_if_matches(f):
        hexdigest = _calc_md5(f)
        if hexdigest in md5s and hexdigest not in copied_md5s:
            copied_md5s.add(hexdigest)
            rom_path = md5s[hexdigest]
            print(f"copying {os.path.basename(rom_path)} from {f.name}")
            os.makedirs(os.path.dirname(rom_path), exist_ok=True)
            f.seek(0)
            with open(rom_path, "wb") as out_f:
                shutil.copyfileobj(f, out_f)
    
    for root, dirs, files in os.walk(dirpath):
        for filename in files:
            filepath = os.path.join(root, filename)
            with open(filepath, "rb") as f:
                _root, ext = os.path.splitext(filename)
                if ext == ".zip":
                    try:
                        _check_zipfile(f, save_if_matches)
                    except zipfile.BadZipFile:
                        pass
                else:
                    save_if_matches(f)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("dirpath", help="path to directory containing extracted ROM files")
    args = parser.parse_args()
    import_roms(args.dirpath)


if __name__ == "__main__":
    main()