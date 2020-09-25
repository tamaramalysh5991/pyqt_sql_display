import sqlite3
from abc import ABC
from exceptions import DatabaseAppError

import psycopg2

DEFAULT_SQLITE_CONNECTION = ':memory:'
# define `in memory` connection for SQLite
in_memory_sqlite_connection = sqlite3.connect(DEFAULT_SQLITE_CONNECTION)


class AbstractDbConnection(ABC):
    """Abstract class for connect to Database and Execute SQL commands"""

    def run(self, query: str, connection_params: str = None):
        """Connect and execute SQL query"""
        raise NotImplementedError()


class SQLiteConnection(AbstractDbConnection):
    """Connection for SQLite"""

    def run(self, query: str, connection_params: str = None) -> tuple:
        """Connect to SQLite db and execute sql command
        If connection params weren't provided, we use `in-memory` connection to create database in RAM
        More info:
        https://docs.python.org/3/library/sqlite3.html#module-sqlite3
        """
        conn = None
        try:

            conn = sqlite3.connect(connection_params) if connection_params else in_memory_sqlite_connection
            cursor = conn.execute(query)
            data = cursor.fetchall()

            columns = []
            if cursor.description:
                columns = [description[0] for description in cursor.description]

            return data, columns
        except sqlite3.DatabaseError as e:
            if conn:
                conn.close()
            raise DatabaseAppError(msg=e.args[0])


class PostgreSQLConnection(AbstractDbConnection):
    """Connection to PostgreSQL"""

    def run(self, query: str, connection_params: str = None):
        try:
            conn = psycopg2.connect(connection_params)
            cursor = conn.cursor()
            cursor.execute(query)
            conn.commit()
            data = cursor.fetchall()

            columns = []
            if cursor.description:
                columns = [desc[0] for desc in cursor.description]

            return data, columns
        except psycopg2.DatabaseError as e:
            cursor.close()
            conn.close()
            raise DatabaseAppError(msg=e.args[0])
        finally:
            cursor.close()
            conn.close()


# available app databases
DB_CONNECTIONS = {
    'sqlite': SQLiteConnection,
    'postgresql': PostgreSQLConnection,
}
