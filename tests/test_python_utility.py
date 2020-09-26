from sys import modules

import pytest

from python_utility.python_utility import PythonUtility


def test_return_code(capfd):
    with pytest.raises(SystemExit):
        PythonUtility(['--help'])

    standard_output, standard_error = capfd.readouterr()
    assert 'Example' in standard_output.strip()
    assert standard_error.strip() == ''


def test_curses_exists():
    application = PythonUtility([])
    assert application.curses_exists() is True


def test_main():
    # This runs into a py.test error, but it covers a line.
    with pytest.raises(SystemExit):
        PythonUtility([]).main()


def test_curses_does_not_exist():
    modules['curses'] = None
    assert PythonUtility([]).curses_exists() is False


def test_run_without_curses(capfd):
    modules['curses'] = None
    assert PythonUtility([]).run() == 1
    standard_output, standard_error = capfd.readouterr()
    assert standard_output.strip() == 'Curses library not found.'
    assert standard_error.strip() == ''


def test_main_without_curses():
    modules['curses'] = None

    with pytest.raises(SystemExit):
        PythonUtility([]).main()
