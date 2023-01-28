from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in cheque_module/__init__.py
from cheque_module import __version__ as version

setup(
	name="cheque_module",
	version=version,
	description="Cheque details",
	author="DT Team",
	author_email="dev2@dipanetech.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
