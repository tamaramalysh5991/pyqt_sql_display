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
        MainWindow.resize(623, 819)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)
        self.selectDatabase = QtWidgets.QComboBox(self.centralwidget)
        self.selectDatabase.setObjectName("selectDatabase")
        self.selectDatabase.addItem("")
        self.selectDatabase.addItem("")
        self.verticalLayout.addWidget(self.selectDatabase)
        self.connectionLabel = QtWidgets.QLabel(self.centralwidget)
        self.connectionLabel.setObjectName("connectionLabel")
        self.verticalLayout.addWidget(self.connectionLabel)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.dbConnection = QtWidgets.QLineEdit(self.centralwidget)
        self.dbConnection.setText("")
        self.dbConnection.setPlaceholderText("")
        self.dbConnection.setObjectName("dbConnection")
        self.verticalLayout.addWidget(self.dbConnection)
        self.sqlQueryLabel = QtWidgets.QLabel(self.centralwidget)
        self.sqlQueryLabel.setObjectName("sqlQueryLabel")
        self.verticalLayout.addWidget(self.sqlQueryLabel)
        self.sqlQuery = QtWidgets.QTextEdit(self.centralwidget)
        self.sqlQuery.setMaximumSize(QtCore.QSize(16777215, 100))
        self.sqlQuery.setInputMethodHints(QtCore.Qt.ImhMultiLine)
        self.sqlQuery.setAutoFormatting(QtWidgets.QTextEdit.AutoAll)
        self.sqlQuery.setAcceptRichText(False)
        self.sqlQuery.setObjectName("sqlQuery")
        self.verticalLayout.addWidget(self.sqlQuery)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.executeButton = QtWidgets.QPushButton(self.centralwidget)
        self.executeButton.setAutoFillBackground(False)
        self.executeButton.setCheckable(False)
        self.executeButton.setAutoDefault(True)
        self.executeButton.setDefault(False)
        self.executeButton.setFlat(False)
        self.executeButton.setObjectName("executeButton")
        self.verticalLayout.addWidget(self.executeButton)
        self.resultLabel = QtWidgets.QLabel(self.centralwidget)
        self.resultLabel.setObjectName("resultLabel")
        self.verticalLayout.addWidget(self.resultLabel)
        self.resultTable = QtWidgets.QTableView(self.centralwidget)
        self.resultTable.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.resultTable.setObjectName("resultTable")
        self.verticalLayout.addWidget(self.resultTable)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusBar = QtWidgets.QStatusBar(MainWindow)
        self.statusBar.setObjectName("statusBar")
        MainWindow.setStatusBar(self.statusBar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "DB connections"))
        self.label_3.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:600;\">Database</span></p></body></html>"))
        self.selectDatabase.setItemText(0, _translate("MainWindow", "SQLite"))
        self.selectDatabase.setItemText(1, _translate("MainWindow", "PostgreSQL"))
        self.connectionLabel.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:600;\">Database connection string</span></p></body></html>"))
        self.label_2.setText(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-style:italic;\">Fill connection parameters to connect to database.</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-style:italic;\">For Example:</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-style:italic;\">For PostgreSQL : dbname=test user=postgres password=secret</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-style:italic;\">For SQLite: db.sqlite (or :memory:*)</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-style:italic;\">:memory: is default connection for SQLite</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-style:italic;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-style:italic;\">* :memory: means that you can create the SQLite database in RAM</span></p></body></html>"))
        self.sqlQueryLabel.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:600;\">SQL Statement:</span></p></body></html>"))
        self.label.setText(_translate("MainWindow", "Edit the SQL Statement, and click \"Run SQL\" to see the result."))
        self.executeButton.setText(_translate("MainWindow", "Run SQL"))
        self.resultLabel.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:600;\">Result:</span></p></body></html>"))

