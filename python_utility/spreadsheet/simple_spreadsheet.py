import gspread


class SimpleSpreadsheet:
    def __init__(self, name: str):
        connection = gspread.service_account()
        spreadsheet = connection.open(name)
        self.worksheet = spreadsheet.get_worksheet(0)

    def read(self, spreadsheet_range):
        return self.worksheet.get(spreadsheet_range)

    def edit(self, spreadsheet_range, values):
        self.worksheet.update(spreadsheet_range, values)

    def search(self, value):
        return self.worksheet.find(value)
