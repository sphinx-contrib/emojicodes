sphinxemoji
===========

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

.. code:: sphinx

   This text includes a smily face |:smile:| and a snake too! |:snake:|

   Don't you love it? |:heart_eyes:|

Emoji substitutions are processed after default substitutions like
``|release|``, ``|version|`` and ``|today|``, but before any other
substitutions in source files (i.e. emoji substitutions can be overriden).
