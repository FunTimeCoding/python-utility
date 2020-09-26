from python_utility.spreadsheet.spreadsheet_service import SpreadsheetService


def test_spreadsheet_service() -> None:
    assert SpreadsheetService.read_status() != ''
