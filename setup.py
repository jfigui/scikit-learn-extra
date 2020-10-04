#! /usr/bin/env python
"""A template for scikit-learn compatible packages."""

import codecs
import os

from setuptools import find_packages, setup, Extension

import numpy as np

from Cython.Build import cythonize
from Cython.Distutils import build_ext

# get __version__ from _version.py
ver_file = os.path.join("sklearn_extra", "_version.py")
with open(ver_file) as f:
    exec(f.read())

DISTNAME = "scikit-learn-extra"
DESCRIPTION = "A set of tools for scikit-learn."
with codecs.open("README.rst", encoding="utf-8-sig") as f:
    LONG_DESCRIPTION = f.read()
MAINTAINER = "G. Lemaitre"
MAINTAINER_EMAIL = "g.lemaitre58@gmail.com"
URL = "https://github.com/scikit-learn-contrib/scikit-learn-extra"
LICENSE = "new BSD"
DOWNLOAD_URL = "https://github.com/scikit-learn-contrib/scikit-learn-extra"
VERSION = __version__  # noqa
INSTALL_REQUIRES = ["numpy>=1.13.3", "scipy>=0.19.1", "scikit-learn>=0.22.0"]
CLASSIFIERS = [
    "Intended Audience :: Science/Research",
    "Intended Audience :: Developers",
    "License :: OSI Approved",
    "Programming Language :: Python",
    "Topic :: Software Development",
    "Topic :: Scientific/Engineering",
    "Operating System :: Microsoft :: Windows",
    "Operating System :: POSIX",
    "Operating System :: Unix",
    "Operating System :: MacOS",
    "Programming Language :: Python :: 3.6",
    "Programming Language :: Python :: 3.7",
    "Programming Language :: Python :: 3.8",
    "Programming Language :: Python :: Implementation :: CPython",
]
EXTRAS_REQUIRE = {
    "tests": ["pytest", "pytest-cov"],
    "docs": [
        "pillow",
        "sphinx",
        "sphinx-gallery",
        "sphinx_rtd_theme",
        "numpydoc",
        "matplotlib",
    ],
}

args = {
    "ext_modules": cythonize(
        [
            Extension(
                "sklearn_extra.utils._cyfht",
                ["sklearn_extra/utils/_cyfht.pyx"],
                include_dirs=[np.get_include()],
            ),
            Extension(
                "sklearn_extra.cluster._commonnn_inner",
                ["sklearn_extra/cluster/_commonnn_inner.pyx"],
                include_dirs=[np.get_include()],
                language="c++",
            ),
        ]
    ),
    "cmdclass": dict(build_ext=build_ext),
}


setup(
    name=DISTNAME,
    maintainer=MAINTAINER,
    maintainer_email=MAINTAINER_EMAIL,
    description=DESCRIPTION,
    license=LICENSE,
    url=URL,
    version=VERSION,
    download_url=DOWNLOAD_URL,
    long_description=LONG_DESCRIPTION,
    zip_safe=False,  # the package can run out of an .egg file
    classifiers=CLASSIFIERS,
    packages=find_packages(),
    install_requires=INSTALL_REQUIRES,
    extras_require=EXTRAS_REQUIRE,
    **args
)
