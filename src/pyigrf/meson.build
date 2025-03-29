# Get NumPy include directory
incdir_numpy = run_command(py,
  ['-c', 'import numpy; print(numpy.get_include())'],
  check: true
).stdout().strip()

# List your Fortran source files here
fortran_sources = [
  'igrf_src.f',  # Replace with your actual Fortran source files
]

# Create Python extension module using f2py
py.extension_module(
  'igrf_module',  # Name of the resulting Python module
  fortran_sources,
  dependencies: [py_dep, numpy_dep],
  include_directories: include_directories(incdir_numpy),
  install: true,
  subdir: 'src',
)

# Install Python files
py.install_sources(
  '__init__.py',
  subdir: '.'
)
