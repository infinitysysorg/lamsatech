from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in lamsatech/__init__.py
from lamsatech import __version__ as version

setup(
	name="lamsatech",
	version=version,
	description="LamsaTech",
	author="Infinity Systems",
	author_email="info@infinitysys.org",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
