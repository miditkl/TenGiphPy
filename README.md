Tenorpy is a Python wrapper for the Tenor API.

Installation
===============
Clone Repository: ``python3 setup.py install``

Install with pip: ``python3 -m pip install tenorpy``

Update with pip: ``python3 -m pip install -U tenorpy``

Usage
=====
**GIF Endpoints**

To use:

````python
import tenorpy
t = tenorpy.Tenor()
print(t.random("GIFTAG"))
# Will return a random GIF with the tag "GIFTAG"
````

[Click here, if you want a sample script for the discord.py library](https://gist.github.com/realSnosh/58b78b8304a835e6d9d471c067b4b0df#file-sample_tenorpy_discordpy_commands_script-py)
