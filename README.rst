========
Overview
========

.. start-badges

.. list-table::
    :stub-columns: 1

    * - docs
      - |docs|
    * - tests
      - | |travis| |appveyor| |requires|
        | |codecov|
    * - package
      - | |version| |wheel| |supported-versions| |supported-implementations|
        | |commits-since|

.. |docs| image:: https://readthedocs.org/projects/python-deploytool/badge/?style=flat
    :target: https://readthedocs.org/projects/python-deploytool
    :alt: Documentation Status


.. |travis| image:: https://travis-ci.org/pcrespov/python-deploytool.svg?branch=master
    :alt: Travis-CI Build Status
    :target: https://travis-ci.org/pcrespov/python-deploytool

.. |appveyor| image:: https://ci.appveyor.com/api/projects/status/github/pcrespov/python-deploytool?branch=master&svg=true
    :alt: AppVeyor Build Status
    :target: https://ci.appveyor.com/project/pcrespov/python-deploytool

.. |requires| image:: https://requires.io/github/pcrespov/python-deploytool/requirements.svg?branch=master
    :alt: Requirements Status
    :target: https://requires.io/github/pcrespov/python-deploytool/requirements/?branch=master

.. |codecov| image:: https://codecov.io/github/pcrespov/python-deploytool/coverage.svg?branch=master
    :alt: Coverage Status
    :target: https://codecov.io/github/pcrespov/python-deploytool

.. |version| image:: https://img.shields.io/pypi/v/simcore-deploy-tool.svg
    :alt: PyPI Package latest release
    :target: https://pypi.python.org/pypi/simcore-deploy-tool

.. |commits-since| image:: https://img.shields.io/github/commits-since/pcrespov/python-deploytool/v0.1.0.svg
    :alt: Commits since latest release
    :target: https://github.com/pcrespov/python-deploytool/compare/v0.1.0...master

.. |wheel| image:: https://img.shields.io/pypi/wheel/simcore-deploy-tool.svg
    :alt: PyPI Wheel
    :target: https://pypi.python.org/pypi/simcore-deploy-tool

.. |supported-versions| image:: https://img.shields.io/pypi/pyversions/simcore-deploy-tool.svg
    :alt: Supported versions
    :target: https://pypi.python.org/pypi/simcore-deploy-tool

.. |supported-implementations| image:: https://img.shields.io/pypi/implementation/simcore-deploy-tool.svg
    :alt: Supported implementations
    :target: https://pypi.python.org/pypi/simcore-deploy-tool


.. end-badges

Toolkit to taid deployment of simcore

* Free software: MIT license

Installation
============

::

    pip install simcore-deploy-tool

Documentation
=============


https://python-deploytool.readthedocs.io/


Development
===========

To run the all tests run::

    tox

Note, to combine the coverage data from all the tox environments run:

.. list-table::
    :widths: 10 90
    :stub-columns: 1

    - - Windows
      - ::

            set PYTEST_ADDOPTS=--cov-append
            tox

    - - Other
      - ::

            PYTEST_ADDOPTS=--cov-append tox
