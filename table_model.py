from PyQt5 import QtCore
from PyQt5.QtCore import Qt
from datetime import datetime


class TableModel(QtCore.QAbstractTableModel):
    """Define custom model for `QTableView`"""

    def __init__(self, data, columns=None):
        super(TableModel, self).__init__()
        self._data = data
        self._columns = columns

    def data(self, index, role):
        """Format data if need"""
        if role == Qt.DisplayRole:
            # Get the raw value
            value = self._data[index.row()][index.column()]

            # Perform per-type checks and render accordingly.
            if isinstance(value, datetime):
                # Render time to YYY-MM-DD.
                return value.strftime("%Y-%m-%d")

            if isinstance(value, float):
                # Render float to 2 dp
                return "%.2f" % value

            # Default (anything not captured above: e.g. int)
            return value

    def rowCount(self, index):
        """Return the length of the outer list."""
        return len(self._data)

    def columnCount(self, index):
        """The following takes the first sub-list, and returns
        the length (only works if all rows are an equal length)"""
        return len(self._data[0])

    def headerData(self, section, orientation, role):
        """Set header in table if they was provided

        :param section: is the index of the column/row.
        :param orientation: can be Horizontal or Vertical
        :param role: current role, we define header only for `Qt.DisplayRole`
        :return: header for Horizontal (sql column) or Vertical (number)
        """
        if not self._columns:
            return

        if role == Qt.DisplayRole:
            if orientation == Qt.Horizontal:
                return str(self._columns[section])

            if orientation == Qt.Vertical:
                return str(section)
