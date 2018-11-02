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


..  |docs| image:: https://readthedocs.org/projects/simcore-devkit/badge/?version=latest
    :target: https://simcore-devkit.readthedocs.io/en/latest/?badge=latest
    :alt: Documentation Status

.. |travis| image:: https://travis-ci.org/pcrespov/devkit.svg?branch=master
    :alt: Travis-CI Build Status
    :target: https://travis-ci.org/pcrespov/devkit

.. |appveyor| image:: https://ci.appveyor.com/api/projects/status/github/pcrespov/devkit?branch=master&svg=true
    :alt: AppVeyor Build Status
    :target: https://ci.appveyor.com/project/pcrespov/devkit

.. |requires| image:: https://requires.io/github/pcrespov/devkit/requirements.svg?branch=master
    :alt: Requirements Status
    :target: https://requires.io/github/pcrespov/devkit/requirements/?branch=master

.. |codecov| image:: https://codecov.io/github/pcrespov/devkit/coverage.svg?branch=master
    :alt: Coverage Status
    :target: https://codecov.io/github/pcrespov/devkit

.. |version| image:: https://img.shields.io/pypi/v/devkit.svg
    :alt: PyPI Package latest release
    :target: https://pypi.python.org/pypi/devkit

.. |commits-since| image:: https://img.shields.io/github/commits-since/pcrespov/devkit/v0.1.0.svg
    :alt: Commits since latest release
    :target: https://github.com/pcrespov/devkit/compare/v0.1.0...master

.. |wheel| image:: https://img.shields.io/pypi/wheel/devkit.svg
    :alt: PyPI Wheel
    :target: https://pypi.python.org/pypi/devkit

.. |supported-versions| image:: https://img.shields.io/pypi/pyversions/devkit.svg
    :alt: Supported versions
    :target: https://pypi.python.org/pypi/devkit

.. |supported-implementations| image:: https://img.shields.io/pypi/implementation/devkit.svg
    :alt: Supported implementations
    :target: https://pypi.python.org/pypi/devkit


.. end-badges

toolkit to aid development of simcore

* Free software: MIT license

Installation
============

::

    pip install devkit

Documentation
=============

This is a toolkit intended to aid the development of osparc-simcore

https://devkit.readthedocs.io/


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
