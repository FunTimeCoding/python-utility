import pytest
from gspread import CellNotFound

from python_utility.spreadsheet.simple_spreadsheet import SimpleSpreadsheet


def test_simple_spreadsheet() -> None:
    spreadsheet = SimpleSpreadsheet()
    spreadsheet.connect()

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

    # search for a value that does not exist
    with pytest.raises(CellNotFound):
        spreadsheet.search('baz')
