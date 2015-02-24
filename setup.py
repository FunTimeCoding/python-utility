try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

setup(name='python-utility',
      version='0.1',
      description='Stub description for python-utility.',
      install_requires=[],
      scripts=['bin/pu'],
      packages=[],
      author='Alexander Reitzel',
      author_email='funtimecoding@gmail.com',
      url='http://example.org',
      download_url='http://example.org/python-utility.tar.gz')
