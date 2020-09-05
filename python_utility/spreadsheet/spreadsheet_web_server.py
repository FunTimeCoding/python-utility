import cherrypy

from python_utility.spreadsheet.spreadsheet_service import SpreadsheetService


class SpreadsheetWebServer:
    @staticmethod
    def main():
        SpreadsheetWebServer().run()

    @staticmethod
    def run():
        cherrypy.config.update({'server.socket_host': '0.0.0.0'})
        cherrypy.quickstart(SpreadsheetService())
