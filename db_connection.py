import sqlite3
import os
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


class AbstractDBAPIDbConnection(AbstractDbConnection):
    """Class for Relation Database
    Need to encapsulate the general logic for Databases by  Python Database API Specification 2.0
    https://www.python.org/dev/peps/pep-0249/

    """
    client = None
    default_connection = in_memory_sqlite_connection

    def get_connection(self, connection_params: str = None):
        return self.client.connect(connection_params) if connection_params else in_memory_sqlite_connection

    def run(self, query: str, connection_params: str = None) -> tuple:
        """Execute SQL command and return result"""
        try:
            with self.get_connection(connection_params=connection_params) as conn:
                cursor = conn.cursor()
                cursor.execute(query)
                conn.commit()

                data = []
                columns = []

                # if description is empty it means that operations that do not return rows
                if cursor.description:
                    data = cursor.fetchall()
                    columns = [description[0] for description in cursor.description]

                cursor.close()
                return data, columns, cursor.rowcount
        except (sqlite3.DatabaseError, psycopg2.DatabaseError) as e:
            raise DatabaseAppError(msg=e.args[0])


class SQLiteConnection(AbstractDBAPIDbConnection):
    """Connection for SQLite"""

    client = sqlite3
    default_connection = in_memory_sqlite_connection

    def get_connection(self, connection_params: str = None):
        """In default SQLite create the file if it wasn't exist, but we block the file creation to consistent
        (For example, PostgreSQL client don't allow it)"""
        if not connection_params or connection_params == DEFAULT_SQLITE_CONNECTION:
            return super().get_connection(connection_params)
        if not os.path.exists(connection_params):
            raise DatabaseAppError(msg=f"Error! file with name {connection_params} does not exist")
        return super().get_connection(connection_params)


class PostgreSQLConnection(AbstractDBAPIDbConnection):
    """Db Connection to PostgreSQL"""

    client = psycopg2
    default_connection = ''


# available app databases
DB_CONNECTIONS = {
    'sqlite': SQLiteConnection,
    'postgresql': PostgreSQLConnection,
}
