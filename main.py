import sys
import platform
from dbmanager.dbmanager import DatabaseManager

from utils.postgres_tools import pg_dump, pg_restore


def main():
    try:
        pg_dump()
    except Exception, e:
        sys.stderr.write(str(e) + "\n")
        sys.stderr.flush()
        return -1
    try:
        pg_restore()
    except Exception, e:
        sys.stderr.write(str(e) + "\n")
        sys.stderr.flush()
        return -1

    manager = DatabaseManager(
        user="postgres", password="master", host="10.2.25.230")
    # manager.dump_database("DBa1a2419fd4de4a3f8cbb594c86b44fb8")
    manager.restore_database("DBa1a2419fd4de4a3f8cbb594c86b44fb8" ,"backups\\DBa1a2419fd4de4a3f8cbb594c86b44fb8 2018-03-28.backup")


if __name__ == "__main__":
    main()
