from setuptools import setup, find_packages
from os import path
from io import open

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

version = '1.0.3'
download_url = 'https://github.com/realSnosh/tenorpy/archive/1.0.3.tar.gz'

try:
    setup(
        name='tenorpy',
        version=version,
        author='alpha_Snosh',
        description='API Wrapper for the Gif library Tenor. Join my server: https://discord.gg/uFdVUMH',
        long_description=long_description,
        license='MIT',
        keywords='tenor, python, python3, api, wrapper, alphasnosh, snosh',
        url='https://github.com/realSnosh/tenorpy',
        download_url=download_url,
        packages=['tenorpy'],
        install_requires=['requests'],
        classifiers=[
            "Intended Audience :: Developers",
            "Topic :: Software Development :: Build Tools",
            "License :: OSI Approved :: MIT License",
            "Programming Language :: Python :: 3",
            "Programming Language :: Python :: 3.4",
            "Programming Language :: Python :: 3.5",
            "Programming Language :: Python :: 3.6",
            "Programming Language :: Python :: 3.7",
            "Programming Language :: Python :: 3.8"

        ]
    )
except Exception:
    setup(
        name='tenorpy',
        version=version,
        author='alpha_Snosh',
        description='API Wrapper for the Gif library Tenor. Join my server: https://discord.gg/uFdVUMH',
        license='MIT',
        keywords='tenor, python, python3, api, wrapper, alphasnosh, snosh',
        url='https://github.com/realSnosh/tenorpy',
        download_url=download_url,
        packages=['tenorpy'],
        install_requires=['requests'],
        classifiers=[
            "Intended Audience :: Developers",
            "Topic :: Software Development :: Build Tools",
            "License :: OSI Approved :: MIT License",
            "Programming Language :: Python :: 3",
            "Programming Language :: Python :: 3.4",
            "Programming Language :: Python :: 3.5",
            "Programming Language :: Python :: 3.6",
            "Programming Language :: Python :: 3.7",
            "Programming Language :: Python :: 3.8"

        ]
    )
