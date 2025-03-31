# Add this import at the top of your meson.build file
fs = import('fs')

incdir_f2py = run_command(py,
    ['-c', 'import os; import numpy.f2py; print(os.path.relpath(numpy.f2py.get_include()))'],
    check : true
).stdout().strip()

inc_f2py = include_directories(incdir_f2py)
f2py_dep = declare_dependency(
    include_directories : incdir_f2py
)

incdir_f2py_abs = run_command(py,
    ['-c', 'import os; os.chdir(".."); import numpy.f2py; print(numpy.f2py.get_include())'],
    check : true
).stdout().strip()

# The actual command is
# python -m numpy.f2py -c -m _igrf igrf.pyf --build-dir pyigrf2 --lower --skip-empty-wrappers --verbose
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
    '--build-dir', 'pyigrf2',
    '--lower', '--skip-empty-wrappers', '--verbose'
  ],
  build_by_default: true,
)

# For the fortranobject.c, use filesystem lookup
fortranobject_c = incdir_f2py / 'fortranobject.c'
if not fs.exists(fortranobject_c)
    message('fortranobject.c not found in ' + incdir_f2py)
    fortranobject_c = incdir_f2py / 'src' / 'fortranobject.c'
endif

py.extension_module('_igrf',
    'igrf_src.f',
    f2py_target,
    fortranobject_c,
    dependencies : [py_dep, numpy_dep, f2py_dep],
    include_directories : [inc_f2py], # for fortranobject.h
    install : true,
    subdir : 'pyigrf2'
)

py.install_sources(
    '__init__.py',
    subdir : 'pyigrf2'
)