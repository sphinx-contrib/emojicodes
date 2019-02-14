"""
Setup module.
"""
from setuptools import setup


setup(
    name='sphinxemoji',
    version='0.1.0',
    description='An extension to use emoji codes in your Sphinx documentation',
    long_description="""TODO""",
    url='https://github.com/Peque/sphinxemoji',
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
    package_data={'sphinxemoji': ['codes.json']},
    install_requires=[
        'sphinx',
    ],
)
