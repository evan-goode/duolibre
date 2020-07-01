#!/usr/bin/env python3

from setuptools import setup, find_packages


setup(
    name="duolibre",
    version="1.0.0",
    description="Authenticate to Duo 2FA systems without the proprietary Duo Mobile app",
    url="https://github.com/evan-goode/duolibre",
    author="Evan Goode",
    author_email="mail@evangoo.de",
    license="The Unlicense",
    install_requires=["Click", "pycryptodome", "pyotp", "qrcode", "requests"],
    packages=find_packages(),
    entry_points={"console_scripts": ["duolibre=duolibre.duolibre:duolibre"]},
)
