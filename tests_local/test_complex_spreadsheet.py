from python_utility.spreadsheet.complex_spreadsheet import ComplexSpreadsheet


def test_complex_spreadsheet() -> None:
    spreadsheet = ComplexSpreadsheet()
    sheet = spreadsheet.load_spreadsheet()

    # restore default
    spreadsheet.update(
        sheet=sheet,
        spreadsheet_range='A1:B2',
        values=[['a1', 'b1'], ['a2', 'b2']],
    )
    rows = spreadsheet.read(
        sheet=sheet,
        spreadsheet_range='A1:B2',
    )
    assert rows == [['a1', 'b1'], ['a2', 'b2']]

    # modify and read again
    spreadsheet.update(
        sheet=sheet,
        spreadsheet_range='A1',
        values=[['foo']],
    )
    rows = spreadsheet.read(
        sheet=sheet,
        spreadsheet_range='A1:B2',
    )
    assert rows == [['foo', 'b1'], ['a2', 'b2']]
