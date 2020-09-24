import sys
from PyQt5 import QtWidgets
import design
import table_model
from exceptions import DatabaseAppError
import db_connection


def get_database(db_name: str) -> db_connection.AbstractDbConnection:
    """Get available database connection by name"""
    try:
        return db_connection.DB_CONNECTIONS[db_name]
    except KeyError:
        raise DatabaseAppError(msg=f'Database with name {db_name} does not exist')


class DatabaseApp(QtWidgets.QMainWindow, design.Ui_MainWindow):
    """This class define the database app"""

    # default db connection
    default_db = db_connection.SQLiteConnection

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        # bound button with executing of SQL query
        self.executeButton.clicked.connect(self.execute_sql_query)

    def show_error(self, error_msg: str):
        """Show error message"""
        msg = QtWidgets.QMessageBox()
        msg.setIcon(QtWidgets.QMessageBox.Critical)
        msg.setText(error_msg)
        msg.setWindowTitle("Error")
        msg.exec_()

    def show_info_message(self, info_msg: str):
        """Show info message"""
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
            data, columns = db.run(query=query, connection_params=connection)
            if not data and not columns:
                self.show_info_message('You have made changes to the database.')
                return

            model = table_model.TableModel(data=data, columns=columns)
            self.resultTable.setModel(model)
            self.resultTable.resizeColumnsToContents()
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
