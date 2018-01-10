#!/usr/bin/env python
# -*- coding: utf-8 -*-

from distutils.core import setup

setup(
    name='python-coincap',
    version='0.0.1',
    url='https://github.com/pyasi/python-coincap',
    download_url='https://github.com/pyasi/python-coincap/archive/master.zip',
    author='Peter Yasi',
    packages=['coincap'],
    module=['coincap'],
    description='Python wrapper around the coincap.io API',
    long_description=open('README.md', 'r').read(),
    install_requires=['requests', 'requests_cache'],
    keywords=['cryptocurrency', 'API', 'coinmarketcap', 'BTC', 'Bitcoin', 'LTC', 'Litecoin', 'DOGE', 'Dogecoin',
                'ETH', 'Ethereum '],
)
