from setuptools import setup, find_packages


setup(
	name="tformat",
	version="0.1",
	packages=find_packages(),
	author="Carter Temm",
	author_email="cartertemm@gmail.com",
	description="Efficient conversion of timestamps to human-readable equivalents",
	long_description=open("readme.md", "r").read(),
	long_description_content_type="text/markdown",
	url="https://github.com/cartertemm/tformat",
	classifiers=[
		"Programming Language :: Python :: 2",
		"Programming Language :: Python :: 3",
		"License :: Public Domain",
		"License :: OSI Approved :: MIT License",
		"Development Status :: 5 - Production/Stable",
		"Topic :: Utilities",
	]
)