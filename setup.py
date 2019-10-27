import os
from distutils.core import setup


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


try:
    setup(
        name='tenorpy',
        version='1.0.0',
        author='alpha_Snosh',
        description='API Wrapper for the Gif library Tenor. Join my server: https://discord.gg/uFdVUMH',
        long_description=read('README.md'),
        license='MIT',
        keywords='tenor, python, python3, api, wrapper, alphasnosh, snosh',
        url='https://github.com/realSnosh/tenorpy',
        download_url='https://github.com/realSnosh/tenorpy/archive/1.0.0.tar.gz',
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
            "Programming Language :: Python :: 3.7"

        ]
    )
except:
    setup(
        name='tenorpy',
        version='2.0.1',
        author='alpha_Snosh',
        description='API Wrapper for the Gif library Tenor. Join my server: https://discord.gg/uFdVUMH',
        license='MIT',
        keywords='tenor, python, python3, api, wrapper, alphasnosh, snosh',
        url='https://github.com/realSnosh/tenorpy',
        download_url='https://github.com/realSnosh/tenorpy/archive/1.0.0.tar.gz',
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
            "Programming Language :: Python :: 3.7"

        ]
    )
