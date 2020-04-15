Sphinx Emoji Codes
==================

An extension to use emoji codes in your Sphinx documentation!

.. code::

   pip install sphinxemoji


Usage
-----

Enable the Sphinx extension(s) in your ``conf.py`` file:

.. code:: python

   extensions = [
       '...',
       'sphinxemoji.sphinxemoji',
   ]

Then you can use emoji code replacements by writing them between bars:

.. code:: rst

   This text includes a smiley face |:smile:| and a snake too! |:snake:|

   Don't you love it? |:heart_eyes:|

If you want a consistent emoji style, you can set it in your ``conf.py`` file:

.. code:: python

   sphinxemoji_style = 'twemoji'

You can find the list of all supported emoji codes `in the project's documentation page
<https://sphinxemojicodes.readthedocs.io/#supported-codes>`_.


Notes
-----

Emoji substitutions are processed after default substitutions like
``|release|``, ``|version|`` and ``|today|``, but before any other
substitutions in source files (i.e. emoji substitutions can be overriden).
