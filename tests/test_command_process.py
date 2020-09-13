from python_utility.command_process import CommandProcess


def test_command_process(capfd) -> None:
    process = CommandProcess(
        arguments=['echo', 'hello']
    )

    assert process.get_return_code() == 0
    assert process.get_standard_output() == 'hello'
    assert process.get_standard_error() == ''

    process.print_output()
    standard_output, standard_error = capfd.readouterr()
    assert standard_output == 'hello\n'
    assert standard_error == ''
