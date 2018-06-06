#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requirements

from setuptools import find_packages, setup

exec(open('steenzout/object/metadata.py').read())


def install_requires(file_name):
    """
    Parse the requirements.txt file

    Returns:
        dict: parsed requirements.txt
    """
    with open(file_name, 'r') as f:
        install_requires = [str(i.line) for i in requirements.parse(f) if i.name]
    return install_requires


setup(name='steenzout.object',
      version=__version__,
      description=__description__,
      author=__author__,
      author_email=__author_email__,
      maintainer=__maintainer__,
      maintainer_email=__maintainer_email__,
      url=__url__,
      namespace_packages=['steenzout'],
      packages=find_packages(exclude=('*.tests', '*.tests.*', 'tests.*', 'tests')),
      package_data={'': ['LICENSE', 'NOTICE.md']},
      install_requires=install_requires('requirements.txt'),
      tests_require=install_requires('requirements-test.txt'),
      license=__license__,
      classifiers=__classifiers__)
