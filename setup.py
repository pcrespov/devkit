#!/usr/bin/env python
# -*- encoding: utf-8 -*-
from __future__ import absolute_import
from __future__ import print_function

import io
import re
import sys
from glob import glob
from os.path import basename
from os.path import dirname
from os.path import join
from os.path import splitext

from typing import List
from pathlib import Path
from setuptools import find_packages
from setuptools import setup

CURRENT_DIR = Path(sys.argv[0] if __name__ == "__main__" else __file__).resolve().parent
COMMENT = re.compile(r'^\s*#')

def read(*names, **kwargs):
    with io.open(
        join(dirname(__file__), *names),
        encoding=kwargs.get('encoding', 'utf8')
    ) as fh:
        return fh.read()

def list_packages(reqpath: Path) -> List[str]:
    pkg_names = []
    with reqpath.open() as f:
        pkg_names = [line.strip() for line in f.readlines() if not COMMENT.match(line)]
    return pkg_names


requirements = list_packages(CURRENT_DIR / 'requirements.txt')
setup_requirements = ['pytest-runner', ]
test_requirements = list_packages(CURRENT_DIR / 'tests' / 'requirements.txt')


setup(
    name='devkit',
    version='0.1.0',
    license='MIT license',
    description='toolkit to aid development of simcore',
    long_description='%s\n%s' % (
        re.compile('^.. start-badges.*^.. end-badges', re.M | re.S).sub('', read('README.rst')),
        re.sub(':[a-z]+:`~?(.*?)`', r'``\1``', read('CHANGELOG.rst'))
    ),
    author='Pedro Crespo',
    url='https://github.com/pcrespov/devkit',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    py_modules=[splitext(basename(path))[0] for path in glob('src/*.py')],
    include_package_data=True,
    zip_safe=False,
    classifiers=[
        # complete classifier list: http://pypi.python.org/pypi?%3Aaction=list_classifiers
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: Unix',
        'Operating System :: POSIX',
        'Operating System :: Microsoft :: Windows',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Topic :: Utilities',
    ],
    keywords=[
        # eg: 'keyword1', 'keyword2', 'keyword3',
    ],
    install_requires=requirements,
    setup_requires=setup_requirements,
    python_requires='>=3.6',
    test_suite='tests',
    tests_require=test_requirements,
    extras_require={
        # eg:
        #   'rst': ['docutils>=0.11'],
        #   ':python_version=="2.6"': ['argparse'],
    },
    entry_points={
        'console_scripts': [
            'devkit = devkit.cli:main',
        ]
    },
)
