from datetime import datetime

from PyQt5 import QtCore
from PyQt5.QtCore import Qt


class SQLTableViewModel(QtCore.QAbstractTableModel):
    """Define custom model for `QTableView` to display SQL query results
    More info:
    https://doc.qt.io/qtforpython/PySide2/QtCore/QAbstractTableModel.html
    """

    def __init__(self, data, columns=None):
        super(SQLTableViewModel, self).__init__()
        self._data = data
        self._columns = columns

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

    def rowCount(self, index):
        """Return the length of the outer list."""
        return len(self._data)

    def columnCount(self, index):
        """The following takes the first sub-list, and returns
        the length (only works if all rows are an equal length)
        """
        if not self._data:
            return 0
        return len(self._data[0])

    def headerData(self, section, orientation, role):
        """Set headers in table if they was provided"""
        if not self._columns:
            return

        if role == Qt.DisplayRole:
            if orientation == Qt.Horizontal:
                return str(self._columns[section])

            if orientation == Qt.Vertical:
                return str(section)
