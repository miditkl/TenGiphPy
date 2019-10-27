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
