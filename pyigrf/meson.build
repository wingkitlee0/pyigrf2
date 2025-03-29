incdir_numpy = run_command(py,
  ['-c', 'import os; os.chdir(".."); import numpy; print(numpy.get_include())'],
  check : true
).stdout().strip()

incdir_f2py = run_command(py,
    ['-c', 'import os; os.chdir(".."); import numpy.f2py; print(numpy.f2py.get_include())'],
    check : true
).stdout().strip()

inc_np = include_directories(incdir_numpy, incdir_f2py)

# The actual command is
# python -m numpy.f2py -c -m _igrf igrf.pyf --build-dir pyigrf --lower --skip-empty-wrappers --verbose
#
# When using a prewritten pyf signature file, we do not need to pass the Fortran source code. See
# https://github.com/numpy/numpy/issues/25654
#
f2py_target = custom_target(
  'f2py_target',
  input: ['igrf.pyf'],
  output: ['_igrfmodule.c'],
  command: [
    py,
    '-m', 'numpy.f2py',
    '@INPUT@',
    '--build-dir', 'pyigrf',
    '--lower', '--skip-empty-wrappers', '--verbose'
  ],
  build_by_default: true,
)

py.extension_module('_igrf',
    'igrf_src.f',
    f2py_target,
    incdir_f2py / 'fortranobject.c',
    include_directories: inc_np,
    dependencies : py_dep,
    install : true,
    subdir : 'pyigrf'
)

py.install_sources(
    '__init__.py',
    subdir : 'pyigrf'
)