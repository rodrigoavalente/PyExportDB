import os
import sys
from pathlib2 import Path
from .postgres_tools import pg_dump, pg_restore
from configuration import ROOT_PATH

def create_needed_directories():
    directory_list = ['backups']

    for directory_name in directory_list:
        directory_path = os.path.join(ROOT_PATH, directory_name)
        Path(directory_path).mkdir(parents=False, exist_ok=True)

def create_dbsqlite():
    path = os.path.join(ROOT_PATH, "db.sqlite")
    dbsqlite = Path(path)

    if not dbsqlite.is_file():
        with open(path, "wb"):
            os.utime(path, None)

def check_postgres_tools():
    try:
        pg_dump()
    except Exception as e:
        sys.stderr.write(str(e) + "\n")
    try:
        pg_restore()
    except Exception as e:
        sys.stderr.write(str(e) + "\n")
