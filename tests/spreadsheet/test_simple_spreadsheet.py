from python_utility.spreadsheet.simple_spreadsheet import SimpleSpreadsheet


def test_complex_spreadsheet() -> None:
    spreadsheet = SimpleSpreadsheet()
    assert spreadsheet.identifier != ''
