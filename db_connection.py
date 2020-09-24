import sqlite3

from exceptions import DatabaseAppError

DEFAULT_SQLITE_CONNECTION = ':memory:'
# define in memory connection for SQLite
in_memory_sqlite_connection = sqlite3.connect(DEFAULT_SQLITE_CONNECTION)


class AbstractDbConnection:
    """Abstract class for connect to Database and Execute SQL commands"""

    def run(self, query: str, connection_params=None):
        """Connect and execute SQL query"""
        raise NotImplementedError()


class SQLiteConnection(AbstractDbConnection):
    """Connection for SQLite"""

    def run(self, query: str, connection_params=None, ) -> tuple:
        try:

            conn = sqlite3.connect(connection_params) if connection_params else in_memory_sqlite_connection
            cursor = conn.execute(query)
            data = cursor.fetchall()

            columns = []
            if cursor.description:
                columns = [description[0] for description in cursor.description]

            return data, columns
        except sqlite3.DatabaseError as e:
            conn.close()
            raise DatabaseAppError(msg=e.args[0])


DB_CONNECTIONS = {
    'sqlite': SQLiteConnection
}
