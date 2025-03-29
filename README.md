# pyigrf




Full command
```
gcc -shared -fPIC -o _igrf.so _igrfmodule.c -I$(python -c "import numpy; print(numpy.get_include())") -I$(python -c "import distutils.sysconfig; print(distutils.sysconfig.get_python_inc())") -I$(python -c "import numpy; print(numpy.f2py.get_include())") -L$(python -c "import distutils.sysconfig; print(distutils.sysconfig.get_config_var('LIBDIR'))") -lpython$(python -c "import sys; print(f'{sys.version_info.major}.{sys.version_info.minor}')") -lgfortran
```