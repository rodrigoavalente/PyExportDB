from wx import App
from dbaccessor.db import connect_to_local_db
from utils.startup_utils import create_dbsqlite, create_needed_directories

class PyExportDB(App):
    def __init__(self, *args, **kwargs):
        super(PyExportDB, self).__init__(*args, **kwargs)
        create_dbsqlite()
        connect_to_local_db()        
        create_needed_directories()