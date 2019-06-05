"""
Setup module.
"""
from setuptools import setup

from sphinxemoji import __version__


setup(
    name='sphinxemoji',
    version=__version__,
    description='An extension to use emoji codes in your Sphinx documentation',
    long_description="""TODO""",
    url='https://github.com/sphinx-contrib/emojicodes',
    author='Miguel Sánchez de León Peque',
    author_email='peque@neosit.es',
    license='BSD License',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Topic :: Documentation',
        'Topic :: Software Development',
        'Topic :: Utilities',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3',
        'Framework :: Sphinx :: Extension',
    ],
    packages=['sphinxemoji'],
    package_data={
        'sphinxemoji': [
            'codes.json',
            'twemoji.css',
            'twemoji.js',
        ],
    },
    install_requires=[
        'sphinx',
    ],
)
