from python_utility.spreadsheet.spreadsheet_web_server import \
    SpreadsheetWebServer


def test_spreadsheet_web_server() -> None:
    web_server = SpreadsheetWebServer()
    assert web_server is not None
