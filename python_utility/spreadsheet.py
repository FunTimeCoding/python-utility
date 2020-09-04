from __future__ import print_function

import pickle
import os.path
import typer
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request

from python_utility.configuration import Configuration

TOKEN_FILE = 'token.pickle'


class Spreadsheet:
    @staticmethod
    def main():
        typer.run(Spreadsheet.edit)

    @staticmethod
    def hello():
        typer.echo('Hello friend.')

    @staticmethod
    def edit():
        configuration = Configuration('~/.python-utility.yaml')
        identifier = configuration.get('spreadsheet')

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

        sheet = service.spreadsheets()

        # Spreadsheet.update(sheet, identifier)
        Spreadsheet.read(sheet, identifier)

    @staticmethod
    def update(sheet, identifier):
        result = sheet.values().get(
            spreadsheetId=identifier,
            range='A1:B2'
        ).execute()
        values = result.get('values', [])

        if not values:
            print('No data found.')
        else:
            for row in values:
                print('%s, %s' % (row[0], row[1]))

    @staticmethod
    def read(sheet, identifier):
        sheet.values().update(
            spreadsheetId=identifier,
            valueInputOption='USER_ENTERED',
            body={
                'values': [
                    ['foo'],
                ]
            },
            range='A1'
        ).execute()
