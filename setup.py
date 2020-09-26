#!/usr/bin/env python3
from setuptools import setup

setup(
    name='python-utility',
    version='0.1.0',
    description='Stub description.',
    url='https://github.com/FunTimeCoding/python-utility',
    author='Alexander Reitzel',
    author_email='funtimecoding@gmail.com',
    license='MIT',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Operating System :: MacOS :: MacOS X',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Topic :: Software Development',
    ],
    keywords='development project skeleton',
    packages=[
        'python_utility',
        'python_utility.language_example',
        'python_utility.powerline',
        'python_utility.spreadsheet',
    ],
    install_requires=['pyyaml', 'gitpython'],
    python_requires='>=3.2',
    entry_points={
        'console_scripts': [
            'pu=python_utility.python_utility:'
            'PythonUtility.main',
            'spreadsheet-service=python_utility.spreadsheet'
            '.spreadsheet_web_server:SpreadsheetWebServer.main',
        ],
    },
)
