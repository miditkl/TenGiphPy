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
print(t.random("GIFTAG"))
print(g.random(tag="GIFTAG")['data']['images']['downsized_large']['url'])
```

Get API Tokens
==============
[Tenor Developer Portal](https://tenor.com/developer/dashboard)
[Giphy Developer Portal](https://developers.giphy.com/)

[Click here, if you want a sample script for the discord.py library](https://gist.github.com/realSnosh/3eae65975e09e3f60fbeeee393054cf2)
