"""Package setup."""

import setuptools
from src.mysql_hello_world.version import Version


setuptools.setup(
    name="mysql-hello-world",
    version=Version("1.0.0").number,
    description="mysql-hello-world",
    long_description=open("README.md").read().strip(),
    author="bedevere",
    author_email="noahgill409@gmail.com",
    url="https://www.github.com/noahgill409",
    py_modules=["mysql-hello-world"],
    install_requires=[],
    license="MIT License",
    zip_safe=False,
    keywords="",
    classifiers=["Packages"],
)
