import sys
from PyQt5 import QtWidgets
import design
import table_model
from exceptions import DatabaseAppError
import db_connection


class DatabaseApp(QtWidgets.QMainWindow, design.Ui_MainWindow):
    """This class define the database app"""

    # default db connection
    default_db = db_connection.SQLiteConnection

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        # bound button with executing of SQL query
        self.executeButton.clicked.connect(self.execute_sql_query)

    def show_error(self, error_msg):
        """Show error message"""
        msg = QtWidgets.QMessageBox()
        msg.setIcon(QtWidgets.QMessageBox.Critical)
        msg.setText(error_msg)
        msg.setWindowTitle("Error")
        msg.exec_()

    def execute_sql_query(self):
        try:
            # TODO: add other database support
            db = self.default_db()
            connection = self.dbConnection.text().strip()
            query = self.sqlQuery.toPlainText().strip()
            if not query:
                self.show_error(error_msg='Please, edit the SQL Statement')
                return

            data, columns = db.run(query=query, connection_params=connection)
            if not data:
                data = [('You have made changes to the database.',), ]

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
