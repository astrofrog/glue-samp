#!/usr/bin/env python

from __future__ import print_function, division, absolute_import

from setuptools import setup, find_packages

entry_points = """
[glue.plugins]
samp=glue_samp:setup
"""

with open('README.rst') as infile:
    LONG_DESCRIPTION = infile.read()

with open('glue_samp/version.py') as infile:
    exec(infile.read())

setup(name='glue-samp',
      version=__version__,
      description='A SAMP plugin for glue',
      long_description=LONG_DESCRIPTION,
      url="https://github.com/glue-viz/glue-samp",
      author='Thomas Robitaille',
      author_email='thomas.robitaille@gmail.com',
      packages = find_packages(),
      package_data={'glue_samp': ['glue_samp_icon.png'],
                    'glue_samp.qt': ['samp_options.ui']},
      entry_points=entry_points,
      install_requires=['astropy>=2.0', 'glue-core>=0.11']
    )
