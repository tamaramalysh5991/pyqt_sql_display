import sqlite3

from exceptions import DatabaseAppError

DEFAULT_CONNECTION = ':memory:'


class AbstractDbConnection:
    """Abstract class for connect to Database and Execute SQL commands"""

    def run(self, query, connection_params=None):
        raise NotImplemented()


class SQLiteConnection(AbstractDbConnection):

    def run(self, query, connection_params=None, ) -> tuple:
        try:
            conn = sqlite3.connect(connection_params or DEFAULT_CONNECTION)
            cursor = conn.execute("SELECT id, name  FROM django_migrations")
            data = cursor.fetchall()
            columns = [description[0] for description in cursor.description]
            conn.close()
            return data, columns
        except sqlite3.DatabaseError as e:
            raise DatabaseAppError(msg=e.args[0])


DB_CONNECTIONS = {
    'sqlite': SQLiteConnection
}
