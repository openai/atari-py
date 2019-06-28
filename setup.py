import multiprocessing
import os
from setuptools import setup, Extension
from setuptools.command.build_ext import build_ext
import subprocess
import sys

with open(os.path.join(os.path.dirname(__file__), 'atari_py', 'package_data.txt')) as f:
    package_data = [line.rstrip() for line in f.readlines()]


class Build(build_ext):
    def run(self):
        if os.name != 'posix' and not self.inplace:
            # silly patch to disable build steps on windows, as we are doing compilation externally
            return
        cores_to_use = max(1, multiprocessing.cpu_count() - 1)
        try:
            cwd = os.path.join('' if self.inplace else self.build_lib, 'atari_py', 'ale_interface', 'build')
            os.makedirs(cwd, exist_ok=True)
            subprocess.check_call(['cmake', '..'], cwd=cwd)
            subprocess.check_call(['cmake', '--build', '.'], cwd=cwd)
        except subprocess.CalledProcessError as e:
            sys.stderr.write("Could not build atari-py: %s. (HINT: are you sure cmake is installed? You might also be missing a library. Atari-py requires: zlib [installable as 'apt-get install zlib1g-dev' on Ubuntu].)\n" % e)
            raise
        except OSError as e:
            sys.stderr.write("Unable to execute '{}'. HINT: are you sure `make` is installed?\n".format(' '.join(cmd)))
            raise
  
class CMakeExtension(Extension):
    def __init__(self, name, sourcedir=''):
        Extension.__init__(self, name, sources=[])
        self.sourcedir = os.path.abspath(sourcedir)

setup(name='atari-py',
      version='0.2.4',
      description='Python bindings to Atari games',
      url='https://github.com/openai/atari-py',
      author='OpenAI',
      author_email='info@openai.com',
      license='',
      packages=['atari_py'],
      package_data={'atari_py': package_data},
      include_package_data=True,
      ext_modules=[CMakeExtension('atari_py')],
      cmdclass={'build_ext': Build},
      install_requires=['numpy', 'six'],
      tests_require=['nose2']
)
