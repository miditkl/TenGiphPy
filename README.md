TenGiphPy is a Python wrapper for the Tenor and Giphy API.

Installation
===============
Clone Repository: ``python3 setup.py install``

Install with pip: ``python3 -m pip install TenGiphPy``

Update with pip: ``python3 -m pip install -U TenGiphPy``

Usage
=====
**GIF Endpoints**

To use:

```python

import TenGiphPy
t = TenGiphPy.Tenor(token='APITOKEN')
g = TenGiphPy.Giphy(token='APITOKEN')

#sync
print(t.random("GIFTAG"))
print(g.random(tag="GIFTAG")['data']['images']['downsized_large']['url'])

# Will return synchronously a random GIF with the tag "GIFTAG"

#async
import asyncio
print(asyncio.run(t.arandom('GIFTAG')))
print((asyncio.run(g.arandom(tag="GIFTAG"))['data']['images']['downsized_large']['url']))

# Will return asynchronously a random GIF with the tag "GIFTAG"

```

Get API Tokens
==============
[Tenor Developer Portal](https://tenor.com/developer/dashboard)

[Giphy Developer Portal](https://developers.giphy.com/)

Examples
=========
[Click here, if you want a sample script for the discord.py library](https://gist.github.com/realSnosh/3eae65975e09e3f60fbeeee393054cf2)

[Click here, if you want a sample script for the discord.py library in an asynchronous version](https://gist.github.com/realSnosh/735adb1660823261a881f4b17276cd9e)

_If you are on pypi and this readme is incorrect showed, [click here](https://github.com/realSnosh/TenGiphPy) to view the GitHub version!_