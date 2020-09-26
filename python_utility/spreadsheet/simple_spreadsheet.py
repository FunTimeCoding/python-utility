import gspread
from python_utility.configuration import Configuration


class SimpleSpreadsheet:
    def __init__(self):
        configuration = Configuration('~/.python-utility.yaml')
        self.identifier = configuration.get('spreadsheet')
        self.worksheet = None

    def connect(self):
        connection = gspread.service_account()
        spreadsheet = connection.open_by_key(self.identifier)
        self.worksheet = spreadsheet.get_worksheet(0)

    def read(self, spreadsheet_range):
        return self.worksheet.get(spreadsheet_range)

    def edit(self, spreadsheet_range, values):
        self.worksheet.update(spreadsheet_range, values)

    def search(self, value):
        return self.worksheet.find(value)

    def edit_coordinates(self, row, column, value):
        self.worksheet.update_cell(row, column, value)
