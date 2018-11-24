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

import re
class Ui_adminFunctionality(object):
    def setupUi(self, adminFunctionality):
        adminFunctionality.setObjectName("adminFunctionality")
        adminFunctionality.resize(588, 470)
        adminFunctionality.setMinimumSize(QtCore.QSize(0, 0))
        adminFunctionality.setBaseSize(QtCore.QSize(200, 200))
        self.centralwidget = QtWidgets.QWidget(adminFunctionality)
        self.centralwidget.setObjectName("centralwidget")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(11, 12, 553, 420))
        self.widget.setObjectName("widget")
        self.gridLayout = QtWidgets.QGridLayout(self.widget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        spacerItem = QtWidgets.QSpacerItem(186, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 0, 0, 1, 2)
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setEnabled(True)
        self.label.setMinimumSize(QtCore.QSize(153, 40))
        self.label.setMaximumSize(QtCore.QSize(153, 40))
        self.label.setBaseSize(QtCore.QSize(20, 20))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(22)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 2, 1, 4)
        spacerItem1 = QtWidgets.QSpacerItem(176, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 0, 6, 1, 2)
        spacerItem2 = QtWidgets.QSpacerItem(20, 73, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout.addItem(spacerItem2, 1, 3, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(155, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem3, 2, 0, 1, 1)
        self.viewVisitorsButton = QtWidgets.QPushButton(self.widget)
        self.viewVisitorsButton.setMinimumSize(QtCore.QSize(135, 35))
        self.viewVisitorsButton.setMaximumSize(QtCore.QSize(135, 35))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(12)
        self.viewVisitorsButton.setFont(font)
        self.viewVisitorsButton.setObjectName("viewVisitorsButton")
        self.gridLayout.addWidget(self.viewVisitorsButton, 2, 1, 1, 3)
        self.viewStaffButton = QtWidgets.QPushButton(self.widget)
        self.viewStaffButton.setMinimumSize(QtCore.QSize(125, 35))
        self.viewStaffButton.setMaximumSize(QtCore.QSize(125, 35))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(12)
        self.viewStaffButton.setFont(font)
        self.viewStaffButton.setObjectName("viewStaffButton")
        self.gridLayout.addWidget(self.viewStaffButton, 2, 4, 1, 3)
        spacerItem4 = QtWidgets.QSpacerItem(138, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem4, 2, 7, 1, 1)
        spacerItem5 = QtWidgets.QSpacerItem(155, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem5, 3, 0, 1, 1)
        self.viewShowsButton = QtWidgets.QPushButton(self.widget)
        self.viewShowsButton.setMinimumSize(QtCore.QSize(135, 35))
        self.viewShowsButton.setMaximumSize(QtCore.QSize(135, 35))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(12)
        self.viewShowsButton.setFont(font)
        self.viewShowsButton.setObjectName("viewShowsButton")
        self.gridLayout.addWidget(self.viewShowsButton, 3, 1, 1, 3)
        self.viewAnimalsButton = QtWidgets.QPushButton(self.widget)
        self.viewAnimalsButton.setMinimumSize(QtCore.QSize(125, 35))
        self.viewAnimalsButton.setMaximumSize(QtCore.QSize(125, 35))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(12)
        self.viewAnimalsButton.setFont(font)
        self.viewAnimalsButton.setObjectName("viewAnimalsButton")
        self.gridLayout.addWidget(self.viewAnimalsButton, 3, 4, 1, 3)
        spacerItem6 = QtWidgets.QSpacerItem(137, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem6, 3, 7, 1, 1)
        spacerItem7 = QtWidgets.QSpacerItem(155, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem7, 4, 0, 1, 1)
        self.addShowButton = QtWidgets.QPushButton(self.widget)
        self.addShowButton.setMinimumSize(QtCore.QSize(135, 35))
        self.addShowButton.setMaximumSize(QtCore.QSize(135, 35))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(12)
        self.addShowButton.setFont(font)
        self.addShowButton.setObjectName("addShowButton")
        self.gridLayout.addWidget(self.addShowButton, 4, 1, 1, 3)
        self.addAnimalButton = QtWidgets.QPushButton(self.widget)
        self.addAnimalButton.setMinimumSize(QtCore.QSize(125, 35))
        self.addAnimalButton.setMaximumSize(QtCore.QSize(125, 35))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(12)
        self.addAnimalButton.setFont(font)
        self.addAnimalButton.setObjectName("addAnimalButton")
        self.gridLayout.addWidget(self.addAnimalButton, 4, 4, 1, 3)
        spacerItem8 = QtWidgets.QSpacerItem(135, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem8, 4, 7, 1, 1)
        spacerItem9 = QtWidgets.QSpacerItem(221, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem9, 5, 0, 1, 3)
        self.logOutButton = QtWidgets.QPushButton(self.widget)
        self.logOutButton.setMinimumSize(QtCore.QSize(93, 33))
        self.logOutButton.setMaximumSize(QtCore.QSize(93, 33))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.logOutButton.setFont(font)
        self.logOutButton.setObjectName("logOutButton")
        self.gridLayout.addWidget(self.logOutButton, 5, 3, 1, 2)
        spacerItem10 = QtWidgets.QSpacerItem(217, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem10, 5, 5, 1, 3)
        adminFunctionality.setCentralWidget(self.centralwidget)
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
        self.viewVisitorsButton.setText(_translate("adminFunctionality", "View Visitors"))
        self.viewStaffButton.setText(_translate("adminFunctionality", "View Staff"))
        self.viewShowsButton.setText(_translate("adminFunctionality", "View Shows"))
        self.viewAnimalsButton.setText(_translate("adminFunctionality", "View Animals"))
        self.addShowButton.setText(_translate("adminFunctionality", "Add Show"))
        self.addAnimalButton.setText(_translate("adminFunctionality", "Add Animal"))
        self.logOutButton.setText(_translate("adminFunctionality", "Log Out"))

    # initialize all the pushbutton and link corresponding page
    def userDefinedInitialization(self):
        # self.addAnimalsButton.clicked.connect(self.addAnimals)
        self.viewShowsButton.clicked.connect(self.viewShows)
        self.viewStaffButton.clicked.connect(self.viewStaff)
        self.viewVisitorsButton.clicked.connect(self.viewVisitors)
        self.viewAnimalsButton.clicked.connect(self.viewAnimals)
        self.addAnimalButton.clicked.connect(self.addAnimal)
        self.addShowButton.clicked.connect(self.addShows)
        self.logOutButton.clicked.connect(self.logout)

    def viewShows(self):
        __main__.status = __main__.statusDef['Normal']
        __main__.state = __main__.adminUIs['adminViewShows']
        app.exit()

    # link the viewStaff page
    def viewStaff(self):
        __main__.status = __main__.statusDef['Normal']
        __main__.state = __main__.adminUIs["adminViewStaff"]
        app.exit()

    def viewVisitors(self):
        __main__.status = __main__.statusDef['Normal']
        __main__.state = __main__.adminUIs["adminViewVisitors"]
        app.exit()

    def addAnimal(self):
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

