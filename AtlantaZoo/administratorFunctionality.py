# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'administratorFunctionality.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
#################### MUST HAVE #################################################################
# import the connection_pool established in the connect.py
from __main__ import connection_pool
# import the __main__ object to access the global variables: status, state, arg, loginIdentity
import __main__

import sys
app = QtWidgets.QApplication(sys.argv)
################################################################################################
class Ui_adminFunctionality(object):
    def setupUi(self, adminFunctionality):
        adminFunctionality.setObjectName("adminFunctionality")
        adminFunctionality.resize(705, 470)
        adminFunctionality.setMinimumSize(QtCore.QSize(0, 0))
        adminFunctionality.setBaseSize(QtCore.QSize(200, 200))
        self.centralwidget = QtWidgets.QWidget(adminFunctionality)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_9 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_9.setObjectName("gridLayout_9")
        self.gridLayout_7 = QtWidgets.QGridLayout()
        self.gridLayout_7.setObjectName("gridLayout_7")
        spacerItem = QtWidgets.QSpacerItem(155, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_7.addItem(spacerItem, 0, 0, 1, 1)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setEnabled(True)
        self.label.setMinimumSize(QtCore.QSize(115, 35))
        self.label.setBaseSize(QtCore.QSize(20, 20))
        self.label.setObjectName("label")
        self.gridLayout_7.addWidget(self.label, 0, 1, 1, 1)
        self.gridLayout_9.addLayout(self.gridLayout_7, 0, 0, 1, 1)
        self.gridLayout_8 = QtWidgets.QGridLayout()
        self.gridLayout_8.setObjectName("gridLayout_8")
        spacerItem1 = QtWidgets.QSpacerItem(101, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_8.addItem(spacerItem1, 0, 0, 1, 1)
        self.homeButton = QtWidgets.QPushButton(self.centralwidget)
        self.homeButton.setMinimumSize(QtCore.QSize(0, 0))
        self.homeButton.setMaximumSize(QtCore.QSize(95, 29))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.homeButton.setFont(font)
        self.homeButton.setObjectName("homeButton")
        self.gridLayout_8.addWidget(self.homeButton, 0, 1, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(155, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_8.addItem(spacerItem2, 0, 2, 1, 1)
        self.gridLayout_9.addLayout(self.gridLayout_8, 0, 1, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(20, 119, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_9.addItem(spacerItem3, 1, 0, 1, 1)
        spacerItem4 = QtWidgets.QSpacerItem(20, 119, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_9.addItem(spacerItem4, 1, 1, 1, 1)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        spacerItem5 = QtWidgets.QSpacerItem(155, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem5, 0, 0, 1, 1)
        self.viewVisitorsButton = QtWidgets.QPushButton(self.centralwidget)
        self.viewVisitorsButton.setMinimumSize(QtCore.QSize(135, 35))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.viewVisitorsButton.setFont(font)
        self.viewVisitorsButton.setObjectName("viewVisitorsButton")
        self.gridLayout.addWidget(self.viewVisitorsButton, 0, 1, 1, 1)
        self.gridLayout_9.addLayout(self.gridLayout, 2, 0, 1, 1)
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.viewStaffButton = QtWidgets.QPushButton(self.centralwidget)
        self.viewStaffButton.setMinimumSize(QtCore.QSize(125, 35))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.viewStaffButton.setFont(font)
        self.viewStaffButton.setObjectName("viewStaffButton")
        self.gridLayout_2.addWidget(self.viewStaffButton, 0, 0, 1, 1)
        spacerItem6 = QtWidgets.QSpacerItem(115, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem6, 0, 1, 1, 1)
        self.gridLayout_9.addLayout(self.gridLayout_2, 2, 1, 1, 1)
        self.gridLayout_5 = QtWidgets.QGridLayout()
        self.gridLayout_5.setObjectName("gridLayout_5")
        spacerItem7 = QtWidgets.QSpacerItem(155, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_5.addItem(spacerItem7, 0, 0, 1, 1)
        self.viewShowsButton = QtWidgets.QPushButton(self.centralwidget)
        self.viewShowsButton.setMinimumSize(QtCore.QSize(135, 35))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.viewShowsButton.setFont(font)
        self.viewShowsButton.setObjectName("viewShowsButton")
        self.gridLayout_5.addWidget(self.viewShowsButton, 0, 1, 1, 1)
        self.gridLayout_9.addLayout(self.gridLayout_5, 3, 0, 1, 1)
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.viewAnimalsButton = QtWidgets.QPushButton(self.centralwidget)
        self.viewAnimalsButton.setMinimumSize(QtCore.QSize(125, 35))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.viewAnimalsButton.setFont(font)
        self.viewAnimalsButton.setObjectName("viewAnimalsButton")
        self.gridLayout_3.addWidget(self.viewAnimalsButton, 0, 0, 1, 1)
        spacerItem8 = QtWidgets.QSpacerItem(98, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem8, 0, 1, 1, 1)
        self.gridLayout_9.addLayout(self.gridLayout_3, 3, 1, 1, 1)
        self.gridLayout_6 = QtWidgets.QGridLayout()
        self.gridLayout_6.setObjectName("gridLayout_6")
        spacerItem9 = QtWidgets.QSpacerItem(155, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_6.addItem(spacerItem9, 0, 0, 1, 1)
        self.addShowButton = QtWidgets.QPushButton(self.centralwidget)
        self.addShowButton.setMinimumSize(QtCore.QSize(135, 35))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.addShowButton.setFont(font)
        self.addShowButton.setObjectName("addShowButton")
        self.gridLayout_6.addWidget(self.addShowButton, 0, 1, 1, 1)
        self.gridLayout_9.addLayout(self.gridLayout_6, 4, 0, 1, 1)
        self.gridLayout_4 = QtWidgets.QGridLayout()
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.logOutButton = QtWidgets.QPushButton(self.centralwidget)
        self.logOutButton.setMinimumSize(QtCore.QSize(125, 35))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.logOutButton.setFont(font)
        self.logOutButton.setObjectName("logOutButton")
        self.gridLayout_4.addWidget(self.logOutButton, 0, 0, 1, 1)
        spacerItem10 = QtWidgets.QSpacerItem(98, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_4.addItem(spacerItem10, 0, 1, 1, 1)
        self.gridLayout_9.addLayout(self.gridLayout_4, 4, 1, 1, 1)
        spacerItem11 = QtWidgets.QSpacerItem(20, 119, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_9.addItem(spacerItem11, 5, 0, 1, 1)
        spacerItem12 = QtWidgets.QSpacerItem(20, 119, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_9.addItem(spacerItem12, 5, 1, 1, 1)
        adminFunctionality.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(adminFunctionality)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 705, 20))
        self.menubar.setObjectName("menubar")
        adminFunctionality.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(adminFunctionality)
        self.statusbar.setObjectName("statusbar")
        adminFunctionality.setStatusBar(self.statusbar)

        self.userDefinedInitialization()

        self.retranslateUi(adminFunctionality)
        QtCore.QMetaObject.connectSlotsByName(adminFunctionality)

    def retranslateUi(self, adminFunctionality):
        _translate = QtCore.QCoreApplication.translate
        adminFunctionality.setWindowTitle(_translate("adminFunctionality", "adminfunctionality"))
        self.label.setText(_translate("adminFunctionality", "<html><head/><body><p align=\"center\"><span style=\" font-size:16pt;\">Atlanta Zoo</span></p></body></html>"))
        self.homeButton.setText(_translate("adminFunctionality", "Home"))
        self.viewVisitorsButton.setText(_translate("adminFunctionality", "View Visitors"))
        self.viewStaffButton.setText(_translate("adminFunctionality", "View Staff"))
        self.viewShowsButton.setText(_translate("adminFunctionality", "View Shows"))
        self.viewAnimalsButton.setText(_translate("adminFunctionality", "View Animals"))
        self.addShowButton.setText(_translate("adminFunctionality", "Add Show"))
        self.logOutButton.setText(_translate("adminFunctionality", "Log out"))

    def userDefinedInitialization(self):
        # self.addAnimalsButton.clicked.connect(self.addAnimals)
        self.viewShowsButton.clicked.connect(self.viewShows)
        self.viewStaffButton.clicked.connect(self.viewStaff)
        self.viewVisitorsButton.clicked.connect(self.viewVisitors)
        self.viewAnimalsButton.clicked.connect(self.viewAnimals)
        self.addShowButton.clicked.connect(self.addShows)
        self.logOutButton.clicked.connect(self.logout)

    def viewShows(self):
        __main__.status = __main__.statusDef['Normal']
        __main__.state = __main__.adminUIs['adminViewShows']
        app.exit()

    def viewStaff(self):
        __main__.status = __main__.statusDef['Normal']
        __main__.state = __main__.adminUIs["adminViewStaff"]
        app.exit()

    def viewVisitors(self):
        __main__.status = __main__.statusDef['Normal']
        __main__.state = __main__.adminUIs["adminViewVisitors"]
        app.exit()

    def addAnimals(self):
        __main__.status = __main__.statusDef['Normal']
        __main__.state = __main__.adminUIs["adminAddAnimals"]
        app.exit()

    def addShows(self):
        __main__.status = __main__.statusDef['Normal']
        __main__.state = __main__.adminUIs["adminAddShows"]
        app.exit()

    def viewAnimals(self):
        __main__.status = __main__.statusDef['Normal']
        __main__.state = __main__.adminUIs["adminViewAnimals"]
        app.exit() 

    def logout(self):
        __main__.status = __main__.statusDef['Normal']
        __main__.state = __main__.adminUIs['logout']
        app.exit()     

def render():
    __main__.state = -10
    adminFunctionality = QtWidgets.QMainWindow()
    ui = Ui_adminFunctionality()
    ui.setupUi(adminFunctionality)
    adminFunctionality.show()
    app.exec_()
    # close the windows
    adminFunctionality.close()
    
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    adminFunctionality = QtWidgets.QMainWindow()
    ui = Ui_adminFunctionality()
    ui.setupUi(adminFunctionality)
    adminFunctionality.show()
    sys.exit(app.exec_())

