# pyigrf2

This is a simple python wrapper for the International Geomagnetic Reference Field (IGRF) model. Please refer to https://www.ncei.noaa.gov/products/international-geomagnetic-reference-field for more information.

It uses the new `meson` build system recommended by `numpy`, while the original `numpy.disutils` is deprecated (fully removed in numpy 2.x).

## Installation

This package is not on pypi yet. So to install it, you need to clone the repository and install it manually. Run
```
pip install . --no-build-isolation
```
or in editable mode
```
pip install -e . --no-build-isolation
```
`--no-build-isolation` is needed for meson-python.

## Developer Notes

As the meson build system is relative new in the python ecosystem, here are some notes on the construction of this wrapper package.

### f2py

The `f2py` steps are the same. I have chosen to use a `pyf` signature file to specific `intent(in)` and `intent(out)` (one can also add special code comment in the source code).

### Meson

The `meson.build` files are used to build the package with `meson`. In particular, we used a `custom_target` to generate `_igrfmodule.c` using `f2py`. The final shared library (`.so`) is generated by the `external_module` object in the `meson.build`.

The full command is similar to the one below.
```
gcc -shared -fPIC -o _igrf.so _igrfmodule.c -I$(python -c "import numpy; print(numpy.get_include())") -I$(python -c "import distutils.sysconfig; print(distutils.sysconfig.get_python_inc())") -I$(python -c "import numpy; print(numpy.f2py.get_include())") -L$(python -c "import distutils.sysconfig; print(distutils.sysconfig.get_config_var('LIBDIR'))") -lpython$(python -c "import sys; print(f'{sys.version_info.major}.{sys.version_info.minor}')") -lgfortran
```