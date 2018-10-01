import distutils.util
platform = distutils.util.get_platform()
platform = platform.replace('linux', 'manylinux1')
print(platform)
