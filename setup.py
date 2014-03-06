#!/usr/bin/env python

from company.package import version

from pip.req import parse_requirements

from setuptools import find_packages, setup


setup(name='python-primogen',
      version=version.__version__,
      description='Python basic package.',
      author='Pedro Salgado',
      author_email='steenzout@ymail.com',
      maintainer='Pedro Salgado',
      maintainer_email='steenzout@ymail.com',
      url='https://github.com/steenzout/python-primogen',
      namespace_packages=('company',),
      packages=find_packages(exclude=('*.tests', '*.tests.*', 'tests.*', 'tests')),
      install_requires=[str(pkg.req) for pkg in parse_requirements('requirements.txt')],
      tests_requires=[str(pkg.req) for pkg in parse_requirements('test-requirements.txt')],)