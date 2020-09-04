from python_utility.spreadsheet.complex_spreadsheet import ComplexSpreadsheet
from python_utility.spreadsheet.simple_spreadsheet import SimpleSpreadsheet


def disabled_test_complex_spreadsheet() -> None:
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


def test_simple_spreadsheet() -> None:
    spreadsheet = SimpleSpreadsheet('API test')

    # restore default
    spreadsheet.edit('A1', [['a1', 'b1'], ['a2', 'b2']])
    result = spreadsheet.read('A1:B2')
    assert result == [['a1', 'b1'], ['a2', 'b2']]

    # modify and read again
    spreadsheet.edit('A1', 'foo')
    result = spreadsheet.read('A1')
    assert result == [['foo']]

    # find a cell
    cell = spreadsheet.search('foo')
    assert cell.col == 1
    assert cell.row == 1

    # update the cell next to the found cell
    spreadsheet.edit_coordinates(cell.row, cell.col + 1, 'bar')
    result = spreadsheet.read('B1')
    assert result == [['bar']]
