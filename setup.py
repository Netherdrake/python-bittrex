#!/usr/bin/env python

from distutils.core import setup


setup(name='python-bittrex',
      version='1.1.0',
      packages=['bittrex'],
      modules=['bittrex'],
      description='Python bindings for bittrex API.',
      install_requires=[
          'requests',
          'pycrypto',
      ],
      classifiers=[
          'Programming Language :: Python',
          'Operating System :: OS Independent',
          'License :: OSI Approved :: MIT License',
          'Topic :: Office/Business :: Financial',
      ])
