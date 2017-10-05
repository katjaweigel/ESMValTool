#!/usr/bin/env python
"""ESMValTool installation script"""
# This script installs dependencies available on PyPI
#
# Dependencies that need to be installed some other way (e.g. conda):
# - ncl
# - iris
# - basemap

import sys

from setuptools import Command, setup

PACKAGES = [
    'esmvaltool',
]


class RunTests(Command):
    """Class to run tests and generate reports"""
    user_options = []

    def initialize_options(self):
        """Do nothing"""

    def finalize_options(self):
        """Do nothing"""

    def run(self):
        """Run tests and generate a coverage report."""
        import pytest

        report_dir = 'test-reports'
        errno = pytest.main([
            'tests',
            '--cov=esmvaltool',
            '--cov-report=html:{}/coverage_html'.format(report_dir),
            '--cov-report=xml:{}/coverage.xml'.format(report_dir),
            '--junit-xml={}/report.xml'.format(report_dir),
        ])

        sys.exit(errno)


with open('README.md') as readme:
    setup(
        name='ESMValTool',
        version="2.0.0",
        description=readme.read(),
        packages=PACKAGES,
        # Include all version controlled files
        include_package_data=True,
        use_scm_version=True,
        setup_requires=[
            'setuptools_scm',
        ],
        install_requires=[
            'cdo',
            'cf_units',
            'coverage',
            'cython',
            'esgf-pyclient',
            'numpy',
            'netCDF4',
            'matplotlib',
            'pyyaml',
            'pytest',
            'pytest-cov',
            'shapely',
        ],
        tests_require=[
            'easytest',
            'mock',
            'nose',
            'pytest',
            'pytest-cov',
        ],
        entry_points={
            'console_scripts': [
                'esmvaltool = esmvaltool.main:run',
            ],
        },
        cmdclass={
            'test': RunTests,
        }, )