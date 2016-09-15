#!/usr/bin/env python

from distutils.core import setup

setup(name='discord-dumpbot',
      version='0.0.0',
      description='Dump Discord logs into an SQLite3 DB',
      author='Andrea Pascal',
      author_email='andrea@anodium.net',
      url='https://github.com/anodium/dumpbot',
      packages=['dumpbot'],
      requires='discord.py>=0.11.0,<=0.12.0',
      license='MIT'
     )
