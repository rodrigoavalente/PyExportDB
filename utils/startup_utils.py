import os
from pathlib2 import Path
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

