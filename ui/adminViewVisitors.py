# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'adminViewVisitors.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_adminViewVisitors(object):
    def setupUi(self, adminViewVisitors):
        adminViewVisitors.setObjectName("adminViewVisitors")
        adminViewVisitors.resize(680, 465)
        self.centralwidget = QtWidgets.QWidget(adminViewVisitors)
        self.centralwidget.setObjectName("centralwidget")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(1, -1, 668, 427))
        self.widget.setObjectName("widget")
        self.gridLayout = QtWidgets.QGridLayout(self.widget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.homeButton = QtWidgets.QPushButton(self.widget)
        self.homeButton.setMinimumSize(QtCore.QSize(117, 49))
        self.homeButton.setMaximumSize(QtCore.QSize(117, 49))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(15)
        self.homeButton.setFont(font)
        self.homeButton.setObjectName("homeButton")
        self.gridLayout.addWidget(self.homeButton, 0, 0, 1, 2)
        spacerItem = QtWidgets.QSpacerItem(88, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 0, 2, 1, 2)
        self.label_2 = QtWidgets.QLabel(self.widget)
        self.label_2.setMinimumSize(QtCore.QSize(194, 47))
        self.label_2.setMaximumSize(QtCore.QSize(194, 47))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(22)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 0, 4, 1, 4)
        spacerItem1 = QtWidgets.QSpacerItem(224, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 0, 8, 1, 3)
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setMinimumSize(QtCore.QSize(103, 24))
        self.label.setMaximumSize(QtCore.QSize(103, 24))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 1, 0, 1, 2)
        spacerItem2 = QtWidgets.QSpacerItem(526, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem2, 1, 2, 1, 9)
        spacerItem3 = QtWidgets.QSpacerItem(154, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem3, 2, 0, 1, 3)
        self.label_3 = QtWidgets.QLabel(self.widget)
        self.label_3.setMinimumSize(QtCore.QSize(90, 24))
        self.label_3.setMaximumSize(QtCore.QSize(90, 24))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(11)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 2, 3, 1, 2)
        self.username = QtWidgets.QLineEdit(self.widget)
        self.username.setMinimumSize(QtCore.QSize(224, 33))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(11)
        self.username.setFont(font)
        self.username.setObjectName("username")
        self.gridLayout.addWidget(self.username, 2, 5, 1, 4)
        spacerItem4 = QtWidgets.QSpacerItem(146, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem4, 2, 9, 1, 2)
        spacerItem5 = QtWidgets.QSpacerItem(247, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem5, 3, 0, 1, 5)
        self.searchButton = QtWidgets.QPushButton(self.widget)
        self.searchButton.setMinimumSize(QtCore.QSize(93, 33))
        self.searchButton.setMaximumSize(QtCore.QSize(93, 33))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(11)
        self.searchButton.setFont(font)
        self.searchButton.setObjectName("searchButton")
        self.gridLayout.addWidget(self.searchButton, 3, 5, 1, 1)
        spacerItem6 = QtWidgets.QSpacerItem(269, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem6, 3, 6, 1, 5)
        spacerItem7 = QtWidgets.QSpacerItem(85, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem7, 4, 0, 1, 1)
        self.visitorList = QtWidgets.QTableWidget(self.widget)
        self.visitorList.setMinimumSize(QtCore.QSize(454, 171))
        self.visitorList.setObjectName("visitorList")
        self.visitorList.setColumnCount(2)
        self.visitorList.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.visitorList.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.visitorList.setHorizontalHeaderItem(1, item)
        self.gridLayout.addWidget(self.visitorList, 4, 1, 1, 9)
        spacerItem8 = QtWidgets.QSpacerItem(82, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem8, 4, 10, 1, 1)
        spacerItem9 = QtWidgets.QSpacerItem(251, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem9, 5, 0, 1, 5)
        self.deleteVisitorButton = QtWidgets.QPushButton(self.widget)
        self.deleteVisitorButton.setMinimumSize(QtCore.QSize(130, 33))
        self.deleteVisitorButton.setMaximumSize(QtCore.QSize(130, 33))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(11)
        self.deleteVisitorButton.setFont(font)
        self.deleteVisitorButton.setObjectName("deleteVisitorButton")
        self.gridLayout.addWidget(self.deleteVisitorButton, 5, 5, 1, 2)
        spacerItem10 = QtWidgets.QSpacerItem(253, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem10, 5, 7, 1, 4)
        adminViewVisitors.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(adminViewVisitors)
        self.statusbar.setObjectName("statusbar")
        adminViewVisitors.setStatusBar(self.statusbar)

        self.retranslateUi(adminViewVisitors)
        QtCore.QMetaObject.connectSlotsByName(adminViewVisitors)

    def retranslateUi(self, adminViewVisitors):
        _translate = QtCore.QCoreApplication.translate
        adminViewVisitors.setWindowTitle(_translate("adminViewVisitors", "MainWindow"))
        self.homeButton.setText(_translate("adminViewVisitors", "Home"))
        self.label_2.setText(_translate("adminViewVisitors", "View Visitor"))
        self.label.setText(_translate("adminViewVisitors", "Atlanta Zoo"))
        self.label_3.setText(_translate("adminViewVisitors", "Username"))
        self.searchButton.setText(_translate("adminViewVisitors", "Search"))
        item = self.visitorList.horizontalHeaderItem(0)
        item.setText(_translate("adminViewVisitors", "Username"))
        item = self.visitorList.horizontalHeaderItem(1)
        item.setText(_translate("adminViewVisitors", "Email"))
        self.deleteVisitorButton.setText(_translate("adminViewVisitors", "Delete Visitor"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    adminViewVisitors = QtWidgets.QMainWindow()
    ui = Ui_adminViewVisitors()
    ui.setupUi(adminViewVisitors)
    adminViewVisitors.show()
    sys.exit(app.exec_())

