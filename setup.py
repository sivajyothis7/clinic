from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in appointments/__init__.py
from appointments import __version__ as version

setup(
	name="appointments",
	version=version,
	description="clinic app",
	author="siva",
	author_email="siva@enfono.in",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
