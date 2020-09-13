import pytest

from python_utility.typer_command import TyperCommand


def test_typer_command_main() -> None:
    with pytest.raises(SystemExit):
        TyperCommand.main()


def test_typer_command_echo_example(capfd) -> None:
    TyperCommand.echo_example()
    standard_output, standard_error = capfd.readouterr()
    assert 'Hello friend.' in standard_output.strip()
    assert standard_error.strip() == ''
