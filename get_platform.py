import distutils.util
platform = distutils.util.get_platform()

# technically, our platform is not actually multilinux... so this may fail in some distros
# however, tested in python:3.6 docker image (by construction)
# and in ubuntu:16.04
platform = platform.replace('linux', 'manylinux1')

print(platform)
