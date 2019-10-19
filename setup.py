#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

setup(
    name="testpackage",
    version="0.0.1",
    description="test package",
    author="Gertjan van den Burg",
    author_email="gertjanvandenburg@gmail.com",
    packages=find_packages(exclude=["tests"]),
    license="MIT",
)
