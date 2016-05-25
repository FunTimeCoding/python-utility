from importlib.util import find_spec

from python_utility.custom_argument_parser import CustomArgumentParser
from python_utility.user_interface import UserInterface


class PythonUtility:
    def __init__(self, arguments: list):
        parser = self.get_parser()
        parsed_arguments = parser.parse_args(arguments)
        self.parsed_arguments = parsed_arguments

    def run(self) -> int:
        if self.curses_exists() is True:
            from curses import wrapper

            def main(standard_screen) -> int:
                interface = UserInterface(
                    self.parsed_arguments,
                    standard_screen
                )

                return interface.run()

            return_code = wrapper(main)
        else:
            return_code = 1
            print('Curses library not found.')

        return return_code

    @staticmethod
    def curses_exists():
        curses_specification = find_spec('curses')
        return curses_specification is not None

    @staticmethod
    def get_parser() -> CustomArgumentParser:
        parser = CustomArgumentParser(description='Example curses program.')

        return parser
