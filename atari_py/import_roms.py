import os
import hashlib
import shutil
import zipfile
import argparse
import io

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
        if hexdigest == "ce5cc62608be2cd3ed8abd844efb8919":
            # the ALE version of road_runner.bin is not easily available
            # patch this file instead to match the correct data
            delta = {4090: 216, 4091: 111, 4092: 216, 4093: 111, 4094: 216, 4095: 111, 8186: 18, 8187: 43, 8188: -216, 8189: 49, 8190: -216, 8191: 49, 12281: 234, 12282: 18, 12283: 11, 12284: -216, 12285: 17, 12286: -216, 12287: 17, 16378: 18, 16379: -21, 16380: -216, 16381: -15, 16382: -216, 16383: -15}
            f.seek(0)
            data = bytearray(f.read())
            for index, offset in delta.items():
                data[index] += offset
            name = f"patched version of {f.name}"
            f = io.BytesIO(bytes(data))
            f.name = name
            hexdigest = _calc_md5(f)

        if hexdigest in md5s and hexdigest not in copied_md5s:
            copied_md5s.add(hexdigest)
            rom_path = md5s[hexdigest]
            print(f"copying {os.path.basename(rom_path)} from {f.name} to {rom_path}")
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