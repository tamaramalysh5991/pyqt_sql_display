from datetime import datetime

from PyQt5 import QtCore
from PyQt5.QtCore import Qt
from exceptions import DatabaseAppError


class SQLTableViewModel(QtCore.QAbstractTableModel):
    """Define custom model for `QTableView` to display SQL query result
    in QTableView element
    More info:
    https://doc.qt.io/qtforpython/PySide2/QtCore/QAbstractTableModel.html
    """

    default_limit = 1000

    def __init__(self, data, columns=None):
        super().__init__()
        self.cursor = data
        first_batch = self.cursor.fetchmany(self.default_limit)
        self._data = first_batch
        self._columns = columns

    def add_more_data(self):
        """Load more rows to `_data` from db cursor
        The cursor is keeping track of where we are in the series of results,
        and we need to do is call
        fetchmany() again until that produces an empty result
        """
        batch = self.cursor.fetchmany(self.default_limit)
        if not batch:
            raise DatabaseAppError(msg='All data was downloaded')
        self._data = self._data + batch

    def data(self, index, role):
        """Format data if need"""
        if role == Qt.DisplayRole:
            # Get the raw value
            value = self._data[index.row()][index.column()]

            if isinstance(value, datetime):
                # Render time to YYY-MM-DD.
                return value.strftime("%Y-%m-%d")

            if isinstance(value, float):
                return "%.2f" % value

            # Default (anything not captured above: e.g. int)
            return value

    def rowCount(self, index) -> int:
        """Return the length of the outer list."""
        return len(self._data)

    def columnCount(self, index) -> int:
        """The following takes the first sub-list, and returns
        the length (only works if all rows are an equal length)
        """
        return len(self._columns)

    def headerData(self, section, orientation, role):
        """Set headers in table if they was provided"""
        if not self._columns:
            return

        if role == Qt.DisplayRole:
            if orientation == Qt.Horizontal:
                return str(self._columns[section])

            if orientation == Qt.Vertical:
                return str(section)
