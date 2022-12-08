from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in cdf_management/__init__.py
from cdf_management import __version__ as version

setup(
	name="cdf_management",
	version=version,
	description="Community Development Fund Management System",
	author="Alphazen Technoliginologies",
	author_email="nchimumilimo939@gmail.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
