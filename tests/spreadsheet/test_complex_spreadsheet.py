from os import mkdir
from os.path import exists, join
from shutil import rmtree

from python_utility.spreadsheet.complex_spreadsheet import ComplexSpreadsheet, \
    TOKEN_FILE
from tests.constants import TEMPORARY_DIRECTORY


def test_complex_spreadsheet() -> None:
    assert ComplexSpreadsheet().identifier != ''


def test_load_token_file() -> None:
    assert ComplexSpreadsheet.load_token_file(TOKEN_FILE) != ''


def test_load_missing_token_file() -> None:
    assert not ComplexSpreadsheet.load_token_file('does-not-exist')


def test_save_token_file() -> None:
    if exists(TEMPORARY_DIRECTORY):
        rmtree(TEMPORARY_DIRECTORY)

    mkdir(TEMPORARY_DIRECTORY)
    assert exists(TEMPORARY_DIRECTORY)

    pickle_path = join(TEMPORARY_DIRECTORY, 'test.pickle')
    ComplexSpreadsheet.save_token_file(
        pickle_path,
        {'hello'}
    )
    assert exists(pickle_path)
    assert ComplexSpreadsheet.load_token_file(pickle_path) == {'hello'}

    rmtree(TEMPORARY_DIRECTORY)


def test_print_rows(capfd) -> None:
    ComplexSpreadsheet.print_rows([['a1', 'a2'], ['b1', 'b2']])
    standard_output, standard_error = capfd.readouterr()
    assert standard_output.strip() == 'a1,a2\nb1,b2'
    assert standard_error.strip() == ''


def test_print_rows_no_data(capfd) -> None:
    ComplexSpreadsheet.print_rows([])
    standard_output, standard_error = capfd.readouterr()
    assert standard_output.strip() == 'No data found.'
    assert standard_error.strip() == ''
