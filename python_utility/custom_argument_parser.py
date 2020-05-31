from argparse import ArgumentParser
from sys import exit as system_exit, stderr


class CustomArgumentParser(ArgumentParser):
    def error(self, message):
        stderr.write('Error: %s\n' % message)

        system_exit(1)
