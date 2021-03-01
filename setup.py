from setuptools import setup
from os import path
from io import open

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

package_name = 'TenGiphPy'
author = 'Snosh'
version = '2.5.0'
desc = 'API Wrapper for the Gif library Tenor and Giphy. Join my server: https://discord.gg/uFdVUMH'
kw = 'giphy, tenor, python, python3, api, wrapper, alphasnosh, snosh'
download_url = 'https://github.com/realSnosh/TenGiphPy/archive/2.5.0.tar.gz'
requirements = ['requests']
classifiers = [
            "Intended Audience :: Developers",
            "Topic :: Software Development :: Build Tools",
            "License :: OSI Approved :: MIT License",
            "Programming Language :: Python :: 3.6",
            "Programming Language :: Python :: 3.7",
            "Programming Language :: Python :: 3.8",
            "Programming Language :: Python :: 3.9"
        ]


try:
    setup(
        name=package_name,
        version=version,
        author=author,
        description=desc,
        long_description=long_description,
        license='MIT',
        keywords=kw,
        url='https://github.com/realSnosh/TenGiphPy',
        download_url=download_url,
        packages=[f'{package_name}'],
        install_requires=requirements,
        classifiers=classifiers
    )
except Exception:
    setup(
        name=package_name,
        version=version,
        author=author,
        description=desc,
        license='MIT',
        keywords=kw,
        url='https://github.com/realSnosh/TenGiphPy',
        download_url=download_url,
        packages=[f'{package_name}'],
        install_requires=requirements,
        classifiers=classifiers
    )
