#!/usr/bin/env python
import os
import sys

if sys.version_info < (3, 8):
    print("Please upgrade to Python 3.8 or higher.")
    sys.exit(1)

from setuptools import setup

try:
    from setuptools import find_namespace_packages
except ImportError:
    # the user has a downlevel version of setuptools.
    print("Error: requires setuptools v40.1.0 or higher.")
    print('Please upgrade setuptools with "pip install --upgrade setuptools" ' "and try again")
    sys.exit(1)

this_directory = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(this_directory, "README.md")) as f:
    long_description = f.read()


package_name = "exampleplatform-core"
package_version = "1.8.0b3"
description = """With example platform, data analysts and engineers can build analytics \
the way engineers build applications."""

setup(
    name=package_name,
    version=package_version,
    description=description,
    long_description=long_description,
    entry_points={
        "console_scripts": ["exampleplatform = exampleplatform.cli.main:cli"],
    }
)