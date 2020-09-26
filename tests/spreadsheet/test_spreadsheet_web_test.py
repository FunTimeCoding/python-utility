import cherrypy
from cherrypy.test import helper

from python_utility.spreadsheet.spreadsheet_service import SpreadsheetService


class SpreadsheetWebTest(helper.CPWebCase):
    @staticmethod
    def setup_server():
        cherrypy.tree.mount(SpreadsheetService(), '/', {})

    def test_status(self):
        self.getPage("/status")
        self.assertStatus('200 OK')

    def test_spreadsheet_search_missing(self):
        body = '{}'
        headers = [('Content-Type', 'application/json'),
                   ('Content-Length', str(len(body)))]
        self.getPage("/spreadsheet", method='POST', headers=headers, body=body)
        self.assertBody('"search missing"')
        self.assertStatus('200 OK')

    def test_spreadsheet_replace_missing(self):
        body = '{"search": "test"}'
        headers = [('Content-Type', 'application/json'),
                   ('Content-Length', str(len(body)))]
        self.getPage("/spreadsheet", method='POST', headers=headers, body=body)
        self.assertBody('"replace missing"')
        self.assertStatus('200 OK')

    def test_spreadsheet_x_offset_missing(self):
        body = '{"search": "foo", "replace": "bar"}'
        headers = [('Content-Type', 'application/json'),
                   ('Content-Length', str(len(body)))]
        self.getPage("/spreadsheet", method='POST', headers=headers, body=body)
        self.assertBody('"x-offset missing"')
        self.assertStatus('200 OK')
