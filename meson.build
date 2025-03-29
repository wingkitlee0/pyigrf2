project(
  'pyigrf',
  'c', 'fortran',
  version: '0.1.0',
  license: 'MIT',
  meson_version: '>=0.64.0',
)

add_languages('fortran')

py_mod = import('python')
py = py_mod.find_installation(pure: false)
py_dep = py.dependency()
numpy_dep = dependency('numpy')

# Set the package directory
package_dir = 'src/pyigrf'
subdir(package_dir)
