# Copyright (C) 2015 Bitquant Research Laboratories (Asia) Limited
# Released under the Simplified BSD License

from setuptools import (
    setup,
    find_packages,
)

setup(
    name="algobroker",
    version="0.0.12",
    author="Joseph C Wang",
    author_email='joequant@gmail.com',
    url="https://github.com/joequant/algobroker",
    description="Algorithmic trading broker",
    long_description="""Algobroker is an interface to trading and events""",
    license="BSD",
    packages=['algobroker'],
    install_requires=['pyzmq',
                      'msgpack-python',
                      'plivo >= 0.11.0',
                      'twilio',
                      'numpy',
                      'scipy',
                      'python-dateutil',
                      'yahoo_finance',
                      'requests',
                      'ib-api',
                      'gevent',
                      'simplejson',
                      'cryptoexchange >= 0.0.6',
                      'bitcoin-price-api >= 0.0.3'],
    scripts=['start-algo.sh', 'stop-algo.sh'],
    use_2to3=True
)
