from setuptools import setup

setup(
    name='bombaysoftwares-pysupp',
    version='1.0.4',
    description='The bombaysoftwares_pysupp package provides a comprehensive set of utility functions for various operations in Python. These functions simplify common tasks such as date formatting, timestamp conversion, manipulating strings. This package is designed to enhance the functionality of various operations in your Python projects.',
    author='Bombay Softwares',
    packages=["bombaysoftwares_pysupp"],
    install_requires=["PyJWT", "hashids", "python-dateutil", "python-slugify", "six", "text-unidecode", "pytz"],
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    license='MIT',
    project_urls={
        "Bug Tracker": "https://github.com/Edugem-Technologies/bombaysoftwares-pysupp/issues",
        "Source Code": "https://github.com/Edugem-Technologies/bombaysoftwares-pysupp",
        "Documentation": "https://github.com/Edugem-Technologies/bombaysoftwares-pysupp#readme"
    },
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.8",
        "License :: OSI Approved :: MIT License",
        "Topic :: Software Development",
        "Topic :: Scientific/Engineering",
        "Operating System :: OS Independent",
    ]
)