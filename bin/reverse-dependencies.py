#!/usr/bin/env python3

import pip
import sys


def find_reverse_dependencies(package_name):
    return [
        pkg.project_name for pkg in pip.get_installed_distributions()
        if package_name in {req.project_name for req in pkg.requires()}
    ]


if __name__ == '__main__':
    print(find_reverse_dependencies(sys.argv[1]))
