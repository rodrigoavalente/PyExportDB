import os
import sys
import time
import psycopg2
import subprocess

from configuration import ROOT_PATH
from utils.postgres_tools import pg_dump, pg_restore


class DatabaseManager(object):
    user = None
    host = None
    password = None

    connection = None

    def __init__(self, **kwargs):
        try:
            self.user = kwargs.get("user")
        except KeyError:
            sys.stderr.write("[ERROR] Database user must be provided.")
            sys.stderr.flush()
        try:
            self.host = kwargs.get("host")
        except KeyError:
            sys.stderr.write("[ERROR] Database host must be provided.")
            sys.stderr.flush()
        try:
            self.password = kwargs.get("password")
        except KeyError:
            sys.stderr.write("[ERROR] Database password must be provided.")
            sys.stderr.flush()

    def __connect(self):
        if self.connection is None:
            try:
                self.connection = psycopg2.connect(
                    "user='%s' host='%s' password='%s'" % (self.user, self.host, self.password))
            except:
                sys.stderr.write(
                    "[ERROR] Failed to connect to the provided database.\n")
                sys.stderr.flush()

    def list_databases(self):
        self.__connect()
        cursor = self.connection.cursor()
        cursor.execute(
            "SELECT datname FROM pg_database WHERE datistemplate = false;")
        databases = [database[0] for database in cursor.fetchall()]
        try:
            psql_index = databases.index("postgres")
            del databases[psql_index]
        except:
            pass
        return databases

    def dump_database(self, dbname):
        sys.stdout.write("[INFO] Starting to backup database %s. \n" % dbname)
        process = subprocess.Popen(
            [pg_dump(), "--dbname=postgresql://%s:%s@%s:5432/%s" % (self.user, self.password, self.host, dbname), "-Fc", "--create", "--clean", "--verbose", "--file=%s %s.backup" % (os.path.join(ROOT_PATH, "backups", dbname), time.strftime("%Y-%m-%d"))], stdout=subprocess.PIPE)

        while process.poll() is None:
            line = process.stdout.readline()
            if line:
                sys.stdout.write(line + "\n")
        sys.stdout.flush()

    def restore_database(self, dbname, backup_file):
        sys.stdout.write("[INFO] Restoring database %s. \n" % dbname)
        process = subprocess.Popen(
            [pg_restore(), "--dbname=postgresql://%s:%s@%s:5432" %
             (self.user, self.password, self.host), "--verbose", backup_file]
        )

        while process.poll() is None:
            line = process.stdout.readline()
            if line:
                sys.stdout.write(line + "\n")
        sys.stdout.flush()
