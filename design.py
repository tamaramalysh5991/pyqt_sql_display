# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'design.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(588, 699)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.connectionLabel = QtWidgets.QLabel(self.centralwidget)
        self.connectionLabel.setObjectName("connectionLabel")
        self.verticalLayout.addWidget(self.connectionLabel)
        self.dbConnection = QtWidgets.QLineEdit(self.centralwidget)
        self.dbConnection.setObjectName("dbConnection")
        self.verticalLayout.addWidget(self.dbConnection)
        self.sqlQueryLabel = QtWidgets.QLabel(self.centralwidget)
        self.sqlQueryLabel.setObjectName("sqlQueryLabel")
        self.verticalLayout.addWidget(self.sqlQueryLabel)
        self.sqlQuery = QtWidgets.QTextEdit(self.centralwidget)
        self.sqlQuery.setMaximumSize(QtCore.QSize(16777215, 100))
        self.sqlQuery.setObjectName("sqlQuery")
        self.verticalLayout.addWidget(self.sqlQuery)
        self.executeButton = QtWidgets.QPushButton(self.centralwidget)
        self.executeButton.setObjectName("executeButton")
        self.verticalLayout.addWidget(self.executeButton)
        self.resultLabel = QtWidgets.QLabel(self.centralwidget)
        self.resultLabel.setObjectName("resultLabel")
        self.verticalLayout.addWidget(self.resultLabel)
        self.resultTable = QtWidgets.QTableView(self.centralwidget)
        self.resultTable.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContentsOnFirstShow)
        self.resultTable.setObjectName("resultTable")
        self.verticalLayout.addWidget(self.resultTable)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "DB connections"))
        self.connectionLabel.setText(_translate("MainWindow", "sqlite3 connection string"))
        self.dbConnection.setPlaceholderText(_translate("MainWindow", ":memory:"))
        self.sqlQueryLabel.setText(_translate("MainWindow", "SQL query"))
        self.executeButton.setText(_translate("MainWindow", "Run"))
        self.resultLabel.setText(_translate("MainWindow", "Result"))

