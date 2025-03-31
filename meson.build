project(
  'pyigrf2',
  'c', 'fortran',
  version: '0.1.0',
  license: 'MIT',
  meson_version: '>=0.64.0',
  default_options: [
    'buildtype=release',
  ],
)

py_mod = import('python')
py = py_mod.find_installation(pure: false)
py_dep = py.dependency()

# Declare numpy dependency
# This is needed because the meson's dependency('numpy') may
# return a dependency that is incompatible with the specified python
numpy_incdir_relative = run_command(py,
  '-c',
  'import numpy, os; print(os.path.relpath(numpy.get_include()))'
).stdout().strip()
numpy_incdir = include_directories(numpy_incdir_relative)
numpy_dep = declare_dependency(include_directories: [numpy_incdir])

# Set the package directory
subdir('pyigrf2')
