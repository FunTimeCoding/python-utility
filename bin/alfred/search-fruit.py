#!/usr/bin/env python3

from python_utility.alfred.search import fruit_search
from sys import exit
# noinspection PyPackageRequirements
from workflow import Workflow

if __name__ == "__main__":
    exit(Workflow().run(fruit_search))
