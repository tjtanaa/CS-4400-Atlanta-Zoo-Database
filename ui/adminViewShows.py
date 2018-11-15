# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'adminViewShows.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.button_home = QtWidgets.QPushButton(self.centralwidget)
        self.button_home.setGeometry(QtCore.QRect(20, 10, 113, 32))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.button_home.setFont(font)
        self.button_home.setObjectName("button_home")
        self.label_header = QtWidgets.QLabel(self.centralwidget)
        self.label_header.setGeometry(QtCore.QRect(360, 20, 101, 16))
        font = QtGui.QFont()
        font.setFamily("Microsoft Sans Serif")
        font.setPointSize(22)
        self.label_header.setFont(font)
        self.label_header.setObjectName("label_header")
        self.label_title = QtWidgets.QLabel(self.centralwidget)
        self.label_title.setGeometry(QtCore.QRect(40, 50, 91, 16))
        self.label_title.setObjectName("label_title")
        self.label_name = QtWidgets.QLabel(self.centralwidget)
        self.label_name.setGeometry(QtCore.QRect(80, 140, 60, 16))
        self.label_name.setObjectName("label_name")
        self.label_exb = QtWidgets.QLabel(self.centralwidget)
        self.label_exb.setGeometry(QtCore.QRect(80, 200, 60, 16))
        self.label_exb.setObjectName("label_exb")
        self.label_date = QtWidgets.QLabel(self.centralwidget)
        self.label_date.setGeometry(QtCore.QRect(400, 140, 60, 16))
        self.label_date.setObjectName("label_date")
        self.button_search = QtWidgets.QPushButton(self.centralwidget)
        self.button_search.setGeometry(QtCore.QRect(400, 200, 71, 32))
        self.button_search.setObjectName("button_search")
        self.comboBox_exb = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_exb.setGeometry(QtCore.QRect(130, 190, 111, 41))
        self.comboBox_exb.setObjectName("comboBox_exb")
        self.comboBox_exb.addItem("")
        self.comboBox_exb.addItem("")
        self.comboBox_exb.addItem("")
        self.comboBox_exb.addItem("")
        self.comboBox_exb.addItem("")
        self.dateTimeEdit = QtWidgets.QDateTimeEdit(self.centralwidget)
        self.dateTimeEdit.setGeometry(QtCore.QRect(440, 140, 194, 24))
        self.dateTimeEdit.setObjectName("dateTimeEdit")
        self.tableView = QtWidgets.QTableView(self.centralwidget)
        self.tableView.setGeometry(QtCore.QRect(100, 270, 631, 181))
        self.tableView.setObjectName("tableView")
        self.button_rmv_show = QtWidgets.QPushButton(self.centralwidget)
        self.button_rmv_show.setGeometry(QtCore.QRect(340, 470, 113, 32))
        self.button_rmv_show.setObjectName("button_rmv_show")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(130, 140, 113, 21))
        self.lineEdit.setObjectName("lineEdit")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.button_home.setText(_translate("MainWindow", "Home"))
        self.label_header.setText(_translate("MainWindow", "Shows"))
        self.label_title.setText(_translate("MainWindow", "Atlanta Zoo"))
        self.label_name.setText(_translate("MainWindow", "Name"))
        self.label_exb.setText(_translate("MainWindow", "Exhibit"))
        self.label_date.setText(_translate("MainWindow", "Date"))
        self.button_search.setText(_translate("MainWindow", "Search"))
        self.comboBox_exb.setItemText(0, _translate("MainWindow", "Pacific"))
        self.comboBox_exb.setItemText(1, _translate("MainWindow", "Jungle"))
        self.comboBox_exb.setItemText(2, _translate("MainWindow", "Sahara"))
        self.comboBox_exb.setItemText(3, _translate("MainWindow", "Mountainous"))
        self.comboBox_exb.setItemText(4, _translate("MainWindow", "Birds"))
        self.button_rmv_show.setText(_translate("MainWindow", "Remove Show"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

