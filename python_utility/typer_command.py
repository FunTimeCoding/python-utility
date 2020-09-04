from __future__ import print_function

import typer


class TyperCommand:
    @staticmethod
    def main():
        typer.run(TyperCommand.echo_example)

    @staticmethod
    def echo_example():
        typer.echo('Hello friend.')
