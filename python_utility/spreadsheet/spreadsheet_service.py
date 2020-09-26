import cherrypy
from gspread import CellNotFound

from python_utility.spreadsheet.simple_spreadsheet import SimpleSpreadsheet


class SpreadsheetService:
    @staticmethod
    def read_status() -> str:
        try:
            from python_utility.build import Build
        except ImportError:
            # TODO: Understand the best practice.
            from python_utility.build_undefined import Build  # type: ignore

        return 'Version: ' + Build.GIT_TAG + '\n' \
               + 'Git hash: ' + Build.GIT_HASH + '\n' \
               + 'Build date: ' + Build.BUILD_DATE + '\n'

    @cherrypy.expose
    def index(self):
        cherrypy.response.headers['Content-Type'] = 'text/plain'

        return 'Hello friend.\n'

    @cherrypy.expose
    @cherrypy.tools.json_out()
    @cherrypy.tools.json_in()
    def spreadsheet(self):
        request = cherrypy.request.json

        if 'search' not in request:
            response = 'search missing'
        elif 'replace' not in request:
            response = 'replace missing'
        elif 'x-offset' not in request:
            response = 'x-offset missing'
        else:
            search = request['search']
            replace = request['replace']
            x_offset = request['x-offset']
            spreadsheet = SimpleSpreadsheet()
            spreadsheet.connect()

            try:
                cell = spreadsheet.search(search)
                spreadsheet.edit_coordinates(
                    cell.row,
                    cell.col + int(x_offset),
                    replace
                )
                response = 'Success'
            except CellNotFound as e:
                response = 'Not found: ' + str(e)

        return response

    @cherrypy.expose
    def status(self):
        cherrypy.response.headers['Content-Type'] = 'text/plain'

        return SpreadsheetService.read_status()
