"""
Copyright 2012 Red Hat, Inc.

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""
import os
import sys

try: from distutils.core import setup
except ImportError: from setuptools import setup

if sys.argv[-1] == "test":
    os.system ("ln tests/bungee_plugins_test.py test.py")
    os.system("python test.py")
    os.system("rm -f test.py")
    sys.exit()

setup(
    name="bungee-plugins",
    version="0.1alpha",
    description="Bungee python plugins",
    url="https://github.com/harshavardhana/bungee-plugins",
    license="Apache",
    packages=["encryption", "encryption.decoders",
              "fileutils", "fs", "pymagic", "pypdf",
              "pypdf.adobe"],
    classifiers=[
        "Development Status :: 4 - Alpha",
        "Environment :: Console",
        "Intended Audience :: Developers",
        "Intended Audience :: System Administrators",
        "License :: OSI Approved :: Apache License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.6",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.1",
        "Programming Language :: Python :: 3.2",
        "Topic :: Software Development :: Build Tools",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
)
