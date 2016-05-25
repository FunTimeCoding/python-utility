from sys import modules

from python_utility.python_utility import PythonUtility


def test_return_code(capfd) -> None:
    try:
        PythonUtility(['--help'])
    except SystemExit:
        pass

    standard_output, standard_error = capfd.readouterr()
    assert 'Example' in standard_output.strip()


def test_curses_exists():
    application = PythonUtility([])
    assert application.curses_exists() is True


def test_curses_does_not_exist():
    modules['curses'] = None
    application = PythonUtility([])
    assert application.curses_exists() is False


def test_run_without_curses(capfd) -> None:
    modules['curses'] = None
    application = PythonUtility([])
    exit_code = application.run()
    standard_output, standard_error = capfd.readouterr()
    assert exit_code is 1
    assert standard_output.strip() == 'Curses library not found.'
