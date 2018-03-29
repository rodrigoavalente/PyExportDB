import sys
import platform
from dbmanager.dbmanager import DatabaseManager

from utils.startup_utils import create_dbsqlite, create_needed_directories
from dbaccessor.db import connect_to_local_db, disconnect_from_local_db
from services.host_service import HostService


def main():
    # manager = DatabaseManager(
    #     user="postgres", password="master", host="10.2.25.230")
    # manager.dump_database("DBa1a2419fd4de4a3f8cbb594c86b44fb8")
    # manager.restore_database("DBa1a2419fd4de4a3f8cbb594c86b44fb8" ,"backups\\DBa1a2419fd4de4a3f8cbb594c86b44fb8 2018-03-28.backup")
    create_dbsqlite()
    create_needed_directories()
    connect_to_local_db()

    service = HostService()
    host = service.add({
        'username': 'postgres',
        'password': 'master',
        'host_url': '10.2.25.230'})
    print(host)
    disconnect_from_local_db()

if __name__ == "__main__":
    main()
