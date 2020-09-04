import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request

from python_utility.configuration import Configuration

TOKEN_FILE = 'token.pickle'


class ComplexSpreadsheet:
    def __init__(self):
        configuration = Configuration('~/.python-utility.yaml')
        self.identifier = configuration.get('spreadsheet')

    @staticmethod
    def load_spreadsheet():
        credentials = None

        if os.path.exists(TOKEN_FILE):
            with open(TOKEN_FILE, 'rb') as token:
                credentials = pickle.load(token)

        if not credentials or not credentials.valid:
            if credentials \
                    and credentials.expired \
                    and credentials.refresh_token:
                credentials.refresh(Request())
            else:
                flow = InstalledAppFlow.from_client_secrets_file(
                    'credentials.json',
                    ['https://www.googleapis.com/auth/spreadsheets']
                )
                credentials = flow.run_local_server(port=0)
            with open(TOKEN_FILE, 'wb') as token:
                pickle.dump(credentials, token)

        service = build('sheets', 'v4', credentials=credentials)

        return service.spreadsheets()

    def read(self, sheet, spreadsheet_range):
        result = sheet.values().get(
            spreadsheetId=self.identifier,
            range=spreadsheet_range
        ).execute()

        return result.get('values', [])

    def update(self, sheet, spreadsheet_range, values):
        sheet.values().update(
            spreadsheetId=self.identifier,
            valueInputOption='USER_ENTERED',
            body={'values': values},
            range=spreadsheet_range
        ).execute()

    @staticmethod
    def print_rows(rows):
        if not rows:
            print('No data found.')
        else:
            for row in rows:
                print(','.join(row))
