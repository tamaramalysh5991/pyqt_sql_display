import sys
from exceptions import DatabaseAppError

import db_connection
import design
import table_model
from PyQt5 import QtWidgets


def get_database(db_name: str) -> db_connection.AbstractDbConnection:
    """Get available database connection by name"""
    try:
        return db_connection.DB_CONNECTIONS[db_name]()
    except KeyError:
        raise DatabaseAppError(msg=f'Database with name {db_name} does not exist')


class DatabaseApp(QtWidgets.QMainWindow, design.Ui_MainWindow):
    """A class to represent the database app"""

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        # bound button with executing of SQL query
        self.executeButton.clicked.connect(self.execute_sql_query)

    def show_error(self, error_msg: str):
        """Prepared and display error message"""
        msg = QtWidgets.QMessageBox()
        msg.setIcon(QtWidgets.QMessageBox.Critical)
        msg.setText(error_msg)
        msg.setWindowTitle("Error")
        msg.exec_()

    def show_info_message(self, info_msg: str):
        """Prepared and display info message"""
        msg = QtWidgets.QMessageBox()
        msg.setIcon(QtWidgets.QMessageBox.Information)
        msg.setText(info_msg)
        msg.setWindowTitle("Info")
        msg.exec_()

    def execute_sql_query(self):
        """Get connection param, database name and SQL query from forms and return SQL data"""
        try:
            db_name = str(self.selectDatabase.currentText()).lower()
            db = get_database(db_name=db_name)

            query = self.sqlQuery.toPlainText().strip()
            if not query:
                self.show_error(error_msg='Please, edit the SQL Statement')
                return

            connection = self.dbConnection.text().strip()
            data, columns, rows_affected = db.run(query=query, connection_params=connection)
            if not columns:
                rows_affected_msg = f' Rows affected: {rows_affected}' if rows_affected > 0 else ''
                self.show_info_message(f'You have made changes to the database.{rows_affected_msg}')
                return

            model = table_model.SQLTableViewModel(data=data, columns=columns)
            self.resultTable.setModel(model)
        except DatabaseAppError as e:
            self.show_error(error_msg=e.msg)


def main():
    """Create app and execute"""
    app = QtWidgets.QApplication(sys.argv)
    window = DatabaseApp()
    window.show()
    app.exec()


if __name__ == '__main__':  # if we're running file directly and not importing it
    main()  # run the main function
