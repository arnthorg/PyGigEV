from distutils.core import setup
from distutils.extension import Extension
from Cython.Distutils import build_ext

ext_modules = [Extension("pygev", 
                             ["pygev.pyx"], 
                             language="c",
                             include_dirs=["/usr/dalsa/GigeV/include/"],
                             libraries=["GevApi"],
                             )]

setup(
    name='pygev',
    cmdclass = {'build_ext': build_ext},
    ext_modules=ext_modules
    )