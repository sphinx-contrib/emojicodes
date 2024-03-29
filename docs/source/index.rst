******************************
Sphinx Emoji Codes - |version|
******************************

.. toctree::
   :maxdepth: 2

.. include:: ../../README.rst
   :start-line: 3

Supported Styles
----------------

Currently there is just one supported style, `Twemoji <https://twemoji.twitter.com/>`_. Feel free to `contribute <https://github.com/sphinx-contrib/emojicodes>`_ other styles if you want, just please pay attention to the licensing. The relevant code can be found in ``sphinxemoji/sphinxemoji.py``:

.. literalinclude::  ../../sphinxemoji/sphinxemoji.py
   :language: python
   :start-at: emoji_styles
   :end-at: }


Supported Codes
---------------

Sphinx Emoji Codes supports many emoji codes. It currently combines the
following sources:

- `gemojione <https://github.com/bonusly/gemojione>`_
- `joypixels <https://github.com/joypixels>`_

Here is the full list of supported emoji codes, sorted alphabetically:

.. sphinxemojitable::
