import sqlite3
import os
from abc import ABC
from exceptions import DatabaseAppError
import psycopg2
from collections import namedtuple

# need to keep result of DB query and data about columns and number of rows that the .execute() produced
DBResults = namedtuple('DBResults', 'data columns affected_rows')

# sqlite connection string for `in memory` connection
DEFAULT_SQLITE_CONNECTION = ':memory:'
# define `in memory` connection for SQLite as default connection
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
    default_connection = None
    # need to avoid freezing
    # TODO: need to implement the better solution
    query_limit = 100000

    def get_connection(self, connection_params: str = None):
        """Try to connect to db via passed param or by default params"""
        return self.client.connect(connection_params) if connection_params else self.default_connection

    def run(self, query: str, connection_params: str = None) -> tuple:
        """Execute SQL command and return result"""
        try:
            with self.get_connection(connection_params=connection_params) as conn:
                cursor = conn.cursor()
                cursor.execute(query)
                conn.commit()

                data = []
                columns = []

                # if description is empty it means that operations do not return affected rows
                if cursor.description:
                    data = cursor.fetchmany(self.query_limit)
                    columns = [description[0] for description in cursor.description]

                cursor.close()
                return DBResults(data=data, columns=columns, affected_rows=cursor.rowcount)
        except (sqlite3.DatabaseError, psycopg2.DatabaseError) as e:
            raise DatabaseAppError(msg=e.args[0])


class SQLiteConnection(AbstractDBAPIDbConnection):
    """Connection for SQLite"""

    client = sqlite3
    default_connection = in_memory_sqlite_connection

    def get_connection(self, connection_params: str = None):
        """In default SQLite create the file if it wasn't exist, but we block the file creation to consistent with
        other databases
        (For example, PostgreSQL client don't allow it)"""
        if not connection_params or connection_params == DEFAULT_SQLITE_CONNECTION:
            return super().get_connection(connection_params)
        if not os.path.exists(connection_params):
            raise DatabaseAppError(msg=f"Error! file with name {connection_params} does not exist")
        return super().get_connection(connection_params)


class PostgreSQLConnection(AbstractDBAPIDbConnection):
    """Db Connection for PostgreSQL"""

    client = psycopg2
    default_connection = ''


# available app databases
DB_CONNECTIONS = {
    'sqlite': SQLiteConnection,
    'postgresql': PostgreSQLConnection,
}
