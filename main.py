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

    def set_data_to_table_view(self, data, columns):
        """Build model for QTableview and pass data to show"""
        model = table_model.SQLTableViewModel(data=data, columns=columns)
        self.resultTable.setModel(model)

    def get_sql_query(self):
        """Retrieve sql query from `QTextEdit` and check that query was provided"""
        query = self.sqlQuery.toPlainText().strip()
        if not query:
            raise DatabaseAppError(msg='Please, edit the SQL Statement')
        return query

    def retrieve_db_client_by_selected_database(self):
        """Define db client by selected database name"""
        db_name = str(self.selectDatabase.currentText()).lower()
        return get_database(db_name=db_name)

    def get_db_connection_string(self):
        """Retrieve connection string from `QLineEdit`"""
        return self.dbConnection.text().strip()

    def execute_sql_query(self):
        """Get connection param, database name and SQL query from forms and return SQL data
        If it was DML statements, show info message about affected rows
        """
        try:
            db = self.retrieve_db_client_by_selected_database()
            query = self.get_sql_query()
            connection = self.get_db_connection_string()
            db_result = db.run(query=query, connection_params=connection)
            # if columns was not provided it means that operations do not return affected rows
            if not db_result.columns:
                rows_affected_msg = f' Rows affected: {db_result.rows_affected}' if db_result.rows_affected > 0 else ''
                self.show_info_message(f'You have made changes to the database.{rows_affected_msg}')
                return

            self.set_data_to_table_view(data=db_result.data, columns=db_result.columns)
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
