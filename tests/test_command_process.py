import pytest

from python_utility.command_process import CommandProcess, CommandFailed


def test_command_process(capfd) -> None:
    process = CommandProcess(arguments=['echo', 'hello'])

    assert process.get_return_code() == 0
    assert process.get_standard_output() == 'hello'
    assert process.get_standard_error() == ''

    process.print_output()
    standard_output, standard_error = capfd.readouterr()
    assert standard_output == 'hello\n'
    assert standard_error == ''


def test_command_fails() -> None:
    with pytest.raises(CommandFailed) as exception:
        CommandProcess(arguments=['tests/fixture/command-fails.sh'])

    assert 'test stdout' in str(exception.value)
    assert 'tests/fixture/command-fails.sh' == exception.value.get_command()
    assert exception.value.get_return_code() == 1
    assert exception.value.get_standard_output() == 'test stdout'
    assert exception.value.get_standard_error() == 'test stderr'
