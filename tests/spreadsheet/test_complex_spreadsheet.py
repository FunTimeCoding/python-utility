from python_utility.spreadsheet.complex_spreadsheet import ComplexSpreadsheet


def test_complex_spreadsheet() -> None:
    assert ComplexSpreadsheet().identifier != ''


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
