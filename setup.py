"""
pickleDB
--------

pickleDB is lightweight, fast, and simple database based on Python's own
json module. And it's BSD licensed!

pickleDB is Fun
```````````````

::

    >>> import pickledb

    >>> db = pickledb.load('test.db', False)

    >>> db.set('key', 'value')

    >>> db.get('key')
    'value'

    >>> db.dump()
    True


And Easy to Install
```````````````````

::

    $ pip install pickledb

Links
`````

* `website <https://patx.github.io/pickledb>`_
* `documentation <http://patx.github.io/pickledb/commands.html>`_
* `pypi <http://pypi.python.org/pypi/pickleDB>`_
* `github repo <https://github.com/patx/pickledb>`_

Latest Release Notes (version: 0.8)
```````````````````````````````````

* All *keys* must now be strings (0.8)
* All *names* for lists must now be strings (0.8)
* All *names* for dicts must now be strings (0.8)
* The get(key) function now returns *False* instead of None if there is no key (0.8)
* Switched to Python's built in json module from simplejson (0.8.1)


"""

from distutils.core import setup

setup(name = "pickleDB",
    version="0.8.2",
    description="A lightweight and simple database using simplejson.",
    author="Harrison Erd",
    author_email="erdh@mail.broward.edu",
    license="three-clause BSD",
    url="http://github.com/patx/pickledb",
    long_description=__doc__,
    classifiers = [
        "Programming Language :: Python",
        "License :: OSI Approved :: BSD License",
        "Intended Audience :: Developers",
        "Topic :: Database" ],
    py_modules=['pickledb'],)
