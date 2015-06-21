from __future__ import absolute_import

from Cython.Distutils import build_ext
from distutils.core import Extension
from distutils.core import setup

import glob


VERSION = open('VERSION').read().strip()

# Sources & libraries
inc_dirs = []
lib_dirs = []
libs = []
sources = []

inc_dirs += ['c_alg/src']
sources += glob.glob("cy_alg/*.pyx")
sources += glob.glob("c_alg/src/*.c")

setup(
    name="c algorithms in cython",
    version=VERSION,
    description='Let c-algorithms project be imported in cython',
    long_description="""\
    """,
    # url='',
    license='http://www.opensource.org/licenses/bsd-license.php',
    cmdclass={'build_ext': build_ext},
    ext_modules=[
        Extension("cython_algos",
                  include_dirs=inc_dirs,
                  sources=sources,
                  library_dirs=lib_dirs,
                  libraries=libs,
                  ),
    ],
    packages=['cy_alg'],
)
