from python_utility.spreadsheet.complex_spreadsheet import ComplexSpreadsheet


def test_complex_spreadsheet() -> None:
    assert ComplexSpreadsheet().identifier != ''
