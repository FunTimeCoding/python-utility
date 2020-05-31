from subprocess import Popen, PIPE
from os import name as os_name, environ
from typing import Union


class CommandFailed(RuntimeError):
    def __init__(
            self,
            command: list,
            return_code: int,
    ):
        self.command = command
        self.return_code = return_code
        self.standard_output = 'unavailable'
        self.standard_error = 'unavailable'

        RuntimeError.__init__(self)

    def set_standard_output(self, standard_output: str):
        self.standard_output = standard_output

    def set_standard_error(self, standard_error: str):
        self.standard_error = standard_error

    def get_command(self) -> str:
        return ' '.join(self.command)

    def get_standard_output(self) -> str:
        return self.standard_output

    def get_standard_error(self) -> str:
        return self.standard_error

    def get_return_code(self) -> int:
        return self.return_code

    def __str__(self) -> str:
        message = 'CommandFailed: ' + ' '.join(self.command) \
                  + '\nReturn code: ' + str(self.return_code) \
                  + '\nPath: ' + environ['PATH']

        if self.standard_output != '':
            message += '\nStandard output: \n' + self.standard_output

        if self.standard_error != '':
            message += '\nStandard error: \n' + self.standard_error

        return message


class CommandProcess:
    def __init__(
            self,
            arguments: list,
            path: str = '',
            sudo_user: str = ''
    ) -> None:
        if sudo_user != '':
            arguments = ['sudo', '-u', sudo_user] + arguments

        self.process = self.try_create_process(
            arguments=arguments,
            path=path,
        )
        self.standard_output, self.standard_error = self.communicate()

        if self.process.returncode != 0:
            command_failed = CommandFailed(
                command=arguments,
                return_code=self.process.returncode,
            )
            command_failed.set_standard_output(
                standard_output=self.get_standard_output()
            )
            command_failed.set_standard_error(
                standard_error=self.get_standard_error()
            )

            raise command_failed

    @staticmethod
    def try_create_process(arguments: list, path: str) -> Popen:
        try:
            return Popen(
                args=arguments,
                stdout=PIPE,
                stderr=PIPE,
                # find executables in PATH on Windows
                shell=bool(os_name == 'nt'),
                cwd=CommandProcess.translate_path(path=path),
            )
        except FileNotFoundError as exception:
            command_failed = CommandFailed(
                command=arguments,
                return_code=-1,
            )
            command_failed.set_standard_output(
                standard_output='File not found: ' + arguments[0]
            )
            command_failed.set_standard_error(
                standard_error=exception.strerror
            )

            raise command_failed

    @staticmethod
    def translate_path(path: str) -> Union[str, None]:
        # Pretty sure None is the expected default
        if path == '':
            path_for_process = None
        else:
            path_for_process = path

        return path_for_process

    def communicate(self):
        output, error = self.process.communicate()
        standard_output = output.decode().strip()
        standard_error = error.decode().strip()

        return standard_output, standard_error

    def print_output(self) -> None:
        if self.standard_error != '':
            print(self.get_standard_error())

        if self.standard_output != '':
            print(self.get_standard_output())

    def get_standard_output(self) -> str:
        return self.standard_output

    def get_standard_error(self) -> str:
        return self.standard_error

    def get_return_code(self) -> int:
        return self.process.returncode
