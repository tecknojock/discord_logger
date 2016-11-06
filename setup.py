#!/usr/bin/env python
'discord.export setup script.'

import os
from setuptools import setup

def read(fname):
    'Utility function to read files.'
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

LONG_DESCRIPTION = read('README.md').splitlines()
DESCRIPTION = LONG_DESCRIPTION[1]
REQUIRES = read('requirements.txt').splitlines()

setup(
    name='discord.export',
    version='0.0.0',
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    keywords="discord data dump export message dms script",
    author='Andrea Pascal',
    author_email='andrea@anodium.net',
    url='https://github.com/anodium/discord-data-export',
    packages=['discord.export', 'discord.tests'],
    requires=REQUIRES,
    license='MIT'
)
