import multiprocessing
import os
from setuptools import setup, Extension
from setuptools.command.build_ext import build_ext
import subprocess
import sys
from distutils.command.build import build as DistutilsBuild

with open(os.path.join(os.path.dirname(__file__), 'atari_py/package_data.txt')) as f:
    package_data = [line.rstrip() for line in f.readlines()]

class Build(build_ext):
    def run(self):
        cores_to_use = max(1, multiprocessing.cpu_count() - 1)
        cmd = ['make', 'build', '-C', 'atari_py/ale_interface', '-j', str(cores_to_use)]
        try:
            subprocess.check_call(cmd, cwd=self.build_lib)
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
      version='0.1.7',
      description='Python bindings to Atari games',
      url='https://github.com/openai/atari-py',
      author='OpenAI',
      author_email='info@openai.com',
      license='',
      packages=['atari_py'],
      package_data={'atari_py': package_data},
      ext_modules=[CMakeExtension('atari_py')],
      cmdclass={'build_ext': Build},
      install_requires=['numpy', 'six'],
      tests_require=['nose2']
)
