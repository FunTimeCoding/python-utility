import sys
from argparse import ArgumentParser


class CustomArgumentParser(ArgumentParser):
    def error(self, message):
        sys.stderr.write('Error: %s\n' % message)

        sys.exit(1)
