from python_utility.spreadsheet.spreadsheet_service import SpreadsheetService


def test_complex_spreadsheet() -> None:
    assert SpreadsheetService.read_status() != ''
