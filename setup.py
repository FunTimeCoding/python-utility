try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

setup(
    name='python-utility',
    version='0.1',
    description='Stub description for python-utility.',
    scripts=['bin/pu'],
    packages=['python_utility'],
    author='Alexander Reitzel',
    author_email='funtimecoding@gmail.com',
    url='http://example.org',
    download_url='http://example.org/python-utility.tar.gz'
)
