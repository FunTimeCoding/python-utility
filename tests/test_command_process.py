import pytest

from python_utility.command_process import CommandProcess, CommandFailed


def test_prints_output(capfd) -> None:
    process = CommandProcess(arguments=['tests/fixture/prints-output.sh'])

    assert process.get_return_code() == 0
    assert process.get_standard_output() == 'test stdout'
    assert process.get_standard_error() == 'test stderr'

    process.print_output()
    standard_output, standard_error = capfd.readouterr()
    assert standard_output == 'test stdout\n'
    assert standard_error == 'test stderr\n'


def test_prints_no_output() -> None:
    process = CommandProcess(arguments=['tests/fixture/prints-no-output.sh'])
    assert process.get_standard_output() == ''
    assert process.get_standard_error() == ''


def test_command_fails_with_output() -> None:
    with pytest.raises(CommandFailed) as exception:
        CommandProcess(arguments=['tests/fixture/fails-with-output.sh'])

    assert 'test stdout' in str(exception.value)
    assert exception.value.get_command() == 'tests/fixture/fails-with-output.sh'
    assert exception.value.get_return_code() == 1
    assert exception.value.get_standard_output() == 'test stdout'
    assert exception.value.get_standard_error() == 'test stderr'


def test_command_fails_without_output() -> None:
    with pytest.raises(CommandFailed) as exception:
        CommandProcess(arguments=['tests/fixture/fails-without-output.sh'])

    assert 'CommandFailed' in str(exception.value)
    assert exception.value.get_command() == \
           'tests/fixture/fails-without-output.sh'
    assert exception.value.get_return_code() == 1
    assert exception.value.get_standard_output() == ''
    assert exception.value.get_standard_error() == ''


def test_command_not_found() -> None:
    with pytest.raises(CommandFailed) as exception:
        CommandProcess(arguments=['does-not-exist'])

    assert 'File not found: does-not-exist' in str(exception.value)
    assert exception.value.get_command() == 'does-not-exist'
    assert exception.value.get_return_code() == -1
    assert exception.value.get_standard_output() == \
           'File not found: does-not-exist'
    assert exception.value.get_standard_error() == \
           'No such file or directory: \'does-not-exist\''
