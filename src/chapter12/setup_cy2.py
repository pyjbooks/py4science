from distutils.core import setup
from distutils.extension import Extension
from Cython.Build import cythonize
import numpy as np

extensions = [
    Extension("cython_2", ["cython_2.c"],
              include_dirs=[np.get_include()],
              libraries=['npymath'],
              library_dirs=['C:/Python/Anaconda3/Lib/site-packages/numpy/core/lib'],
              extra_compile_args=['/openmp'],
              extra_link_args=['/openmp']),
]

setup(
    name="My matrix calc",
    ext_modules=cythonize(extensions),
    include_dirs=[np.get_include()]
)
