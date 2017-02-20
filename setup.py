import glob
import os
import sys
from setuptools import setup
from setuptools.command.build_ext import build_ext as _build_ext
from setuptools.extension import Library


# Force linker to produce a shared library
class build_ext(_build_ext):
    if sys.platform.startswith('linux'):
        def get_ext_filename(self, fullname):
            import setuptools.command.build_ext
            tmp = setuptools.command.build_ext.libtype
            setuptools.command.build_ext.libtype = 'shared'
            ret = _build_ext.get_ext_filename(self, fullname)
            setuptools.command.build_ext.libtype = tmp
            return ret

    def setup_shlib_compiler(self):
        _build_ext.setup_shlib_compiler(self)
        if sys.platform == 'win32':
            from distutils.ccompiler import CCompiler
            mtd = CCompiler.link_shared_object.__get__(self.shlib_compiler)
            self.shlib_compiler.link_shared_object = mtd
        elif sys.platform.startswith('linux'):
            from functools import partial
            c = self.shlib_compiler
            c.link_shared_object = partial(c.link, c.SHARED_LIBRARY)


def list_files(path):
    for root, dirs, files in os.walk(path):
        for fname in files:
            yield os.path.join(root, fname)

        for dirname in dirs:
            for rpath in list_files(os.path.join(root, dirname)):
                yield rpath


basepath = os.path.normpath(r'atari_py/ale_interface/src')
modules = [os.path.join(basepath, os.path.normpath(path))
           for path in 'common controllers emucore emucore/m6502/src '
                       'emucore/m6502/src/bspf/src environment games '
                       'games/supported external external/TinyMT'.split()]
defines = []
sources = [os.path.join('atari_py', 'ale_c_wrapper.cpp'),
           os.path.join(basepath, 'ale_interface.cpp')]
includes = ['atari_py', basepath, os.path.join(basepath, 'os_dependent')]
includes += modules

for folder in modules:
    sources += glob.glob(os.path.join(folder, '*.c'))
    sources += glob.glob(os.path.join(folder, '*.c?[xp]'))

if sys.platform.startswith('linux'):
    defines.append(('BSPF_UNIX', None))
    for fname in 'SettingsUNIX.cxx OSystemUNIX.cxx FSNodePOSIX.cxx'.split():
        sources.append(os.path.join(basepath, 'os_dependent', fname))
elif sys.platform == "darwin":
    defines.append(('BSPF_MAC_OSX', None))
    includes.append(
        '/System/Library/Frameworks/vecLib.framework/Versions/Current/Headers')
elif sys.platform == "win32":
    defines.append(('BSPF_WIN32', None))
    for fname in 'SettingsWin32.cxx OSystemWin32.cxx FSNodeWin32.cxx'.split():
        sources.append(os.path.join(basepath, 'os_dependent', fname))

library_dirs = []
zlib_root = os.environ.get('ZLIB_ROOT')
if zlib_root is not None:
    if not os.path.isfile(os.path.join(zlib_root, 'zlib.h')):
        raise ValueError("There is no 'zlib.h' in ZLIB_ROOT folder")
    zlib_includes = [zlib_root]

    import fnmatch
    zlib_includes += {
        os.path.dirname(path)
        for path in fnmatch.filter(list_files(zlib_root), '*zconf.h')
    }
    if not zlib_includes:
        raise ValueError("Failed to find 'zconf.h' under ZLIB_ROOT folder. "
                         "Have you compiled zlib?")
    includes += zlib_includes

    zlib_libraries = set()

    # Try to compile a test program against zlib
    from distutils.ccompiler import get_default_compiler, new_compiler
    compiler = new_compiler(compiler=get_default_compiler())
    ext = compiler.static_lib_extension

    if os.name == 'nt':
        zlib_name = 'zlib'
    else:
        zlib_name = 'libz'

    import tempfile
    from distutils.ccompiler import CompileError, LinkError
    tmp_dir = tempfile.mkdtemp()
    src_path = os.path.join(tmp_dir, 'zlibtest.c')
    with open(src_path, 'w') as f:
        f.write("#include <zlib.h>\nint main() { inflate(0, 0); return 0; }")
    try:
        for i, path in enumerate(fnmatch.filter(list_files(zlib_root),
                                                '*%s*%s' % (zlib_name, ext))):
            tmp_dir_i = os.path.join(tmp_dir, str(i))
            zlib_library = os.path.splitext(os.path.basename(path))[0]
            zlib_library_dir = os.path.dirname(path)
            try:
                objects = compiler.compile([src_path], tmp_dir_i,
                                           include_dirs=zlib_includes)
                compiler.link_executable(objects, 'zlibtest', tmp_dir_i,
                                         libraries=[zlib_library],
                                         library_dirs=[zlib_library_dir])
            except (CompileError, LinkError) as e:
                pass  # skip this library as malformed
            else:
                zlib_libraries.add((zlib_library, zlib_library_dir))
    finally:
        import shutil
        shutil.rmtree(tmp_dir, ignore_errors=True)

    if not zlib_libraries:
        raise ValueError("Failed to find a suitable library (zlib*%s) under "
                         "ZLIB_ROOT folder. Have you compiled zlib?" % ext)

    # Priority to static library (Windows)
    for zlib_library, zlib_library_dir in zlib_libraries:
        if 'static' in zlib_library:
            break
    library_dirs.append(zlib_library_dir)
else:
    if os.name == 'nt':
        zlib_library = 'zlib'
    else:
        zlib_library = 'z'


ale_c = Library('ale_c',
                define_macros=defines,
                sources=sources,
                include_dirs=includes,
                libraries=[zlib_library],
                library_dirs=library_dirs,
                )


setup(name='atari-py',
      version='0.0.18',
      description='Python bindings to Atari games',
      url='https://github.com/openai/atari-py',
      author='OpenAI',
      author_email='info@openai.com',
      license='',
      packages=['atari_py'],
      package_data={'atari_py': ['atari_roms/*']},
      cmdclass={'build_ext': build_ext},
      ext_modules=[ale_c],
      install_requires=['numpy', 'six'],
      tests_require=['nose2']
      )
