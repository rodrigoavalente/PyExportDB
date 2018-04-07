import wx
from dbaccessor.db import connect_to_local_db
from utils.startup_utils import create_dbsqlite, create_needed_directories, check_postgres_tools


class PyExportDB(wx.App):
    def __init__(self, *args, **kwargs):
        super(PyExportDB, self).__init__(*args, **kwargs)
        create_dbsqlite()
        connect_to_local_db()
        check_postgres_tools()
        create_needed_directories()
