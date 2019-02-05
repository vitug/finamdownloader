#!/usr/bin/env python
# coding: utf8

VERSION = '0.1.4'

import sys
from setuptools import setup

extra_args = {}

setup(name='finamdownloader',
      version=VERSION,
      description='finamdownloader',
      author='Serg Shabalin, Vasily Tugarinov',
      url='https://github.com/vitug/finamdownloader',
      packages=['finamdownloader'],
      install_requires=['numpy', 'pandas'],
      **extra_args)
