# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'visitorFunctionality.ui'
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
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(783, 401)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(12, 12, 755, 361))
        self.widget.setObjectName("widget")
        self.gridLayout = QtWidgets.QGridLayout(self.widget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        spacerItem = QtWidgets.QSpacerItem(20, 46, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout.addItem(spacerItem, 0, 3, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(250, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 1, 0, 1, 2)
        self.label_header = QtWidgets.QLabel(self.widget)
        self.label_header.setMinimumSize(QtCore.QSize(202, 44))
        self.label_header.setMaximumSize(QtCore.QSize(202, 44))
        font = QtGui.QFont()
        font.setFamily("Microsoft Sans Serif")
        font.setPointSize(22)
        self.label_header.setFont(font)
        self.label_header.setObjectName("label_header")
        self.gridLayout.addWidget(self.label_header, 1, 2, 1, 2)
        spacerItem2 = QtWidgets.QSpacerItem(274, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem2, 1, 4, 1, 2)
        spacerItem3 = QtWidgets.QSpacerItem(77, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem3, 2, 0, 1, 1)
        self.button_ser_exb = QtWidgets.QPushButton(self.widget)
        self.button_ser_exb.setMinimumSize(QtCore.QSize(248, 41))
        self.button_ser_exb.setMaximumSize(QtCore.QSize(248, 41))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(15)
        self.button_ser_exb.setFont(font)
        self.button_ser_exb.setObjectName("button_ser_exb")
        self.gridLayout.addWidget(self.button_ser_exb, 2, 1, 1, 2)
        self.button_view_exb_his = QtWidgets.QPushButton(self.widget)
        self.button_view_exb_his.setMinimumSize(QtCore.QSize(248, 41))
        self.button_view_exb_his.setMaximumSize(QtCore.QSize(248, 41))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(15)
        self.button_view_exb_his.setFont(font)
        self.button_view_exb_his.setObjectName("button_view_exb_his")
        self.gridLayout.addWidget(self.button_view_exb_his, 2, 3, 1, 2)
        spacerItem4 = QtWidgets.QSpacerItem(132, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem4, 2, 5, 1, 1)
        spacerItem5 = QtWidgets.QSpacerItem(81, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem5, 3, 0, 1, 1)
        self.button_ser_show = QtWidgets.QPushButton(self.widget)
        self.button_ser_show.setMinimumSize(QtCore.QSize(244, 39))
        self.button_ser_show.setMaximumSize(QtCore.QSize(244, 39))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(15)
        self.button_ser_show.setFont(font)
        self.button_ser_show.setObjectName("button_ser_show")
        self.gridLayout.addWidget(self.button_ser_show, 3, 1, 1, 2)
        self.button_view_show_his = QtWidgets.QPushButton(self.widget)
        self.button_view_show_his.setMinimumSize(QtCore.QSize(246, 39))
        self.button_view_show_his.setMaximumSize(QtCore.QSize(246, 39))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(15)
        self.button_view_show_his.setFont(font)
        self.button_view_show_his.setObjectName("button_view_show_his")
        self.gridLayout.addWidget(self.button_view_show_his, 3, 3, 1, 2)
        spacerItem6 = QtWidgets.QSpacerItem(130, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem6, 3, 5, 1, 1)
        spacerItem7 = QtWidgets.QSpacerItem(80, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem7, 4, 0, 1, 1)
        self.button_ser_anm = QtWidgets.QPushButton(self.widget)
        self.button_ser_anm.setMinimumSize(QtCore.QSize(243, 45))
        self.button_ser_anm.setMaximumSize(QtCore.QSize(243, 45))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(15)
        self.button_ser_anm.setFont(font)
        self.button_ser_anm.setObjectName("button_ser_anm")
        self.gridLayout.addWidget(self.button_ser_anm, 4, 1, 1, 2)
        self.button_lgo = QtWidgets.QPushButton(self.widget)
        self.button_lgo.setMinimumSize(QtCore.QSize(243, 44))
        self.button_lgo.setMaximumSize(QtCore.QSize(243, 44))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(15)
        self.button_lgo.setFont(font)
        self.button_lgo.setObjectName("button_lgo")
        self.gridLayout.addWidget(self.button_lgo, 4, 3, 1, 2)
        spacerItem8 = QtWidgets.QSpacerItem(136, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem8, 4, 5, 1, 1)
        spacerItem9 = QtWidgets.QSpacerItem(20, 41, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout.addItem(spacerItem9, 5, 1, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.userDefinedInitialization()

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_header.setText(_translate("MainWindow", "Atlanta Zoo"))
        self.button_ser_exb.setText(_translate("MainWindow", "Search Exhibits"))
        self.button_view_exb_his.setText(_translate("MainWindow", "View Exhibit History"))
        self.button_ser_show.setText(_translate("MainWindow", "Search Show"))
        self.button_view_show_his.setText(_translate("MainWindow", "View Show History"))
        self.button_ser_anm.setText(_translate("MainWindow", "Search for Animals"))
        self.button_lgo.setText(_translate("MainWindow", "Logout"))



    def userDefinedInitialization(self):
        self.button_lgo.clicked.connect(self.logout)
        self.button_ser_anm.clicked.connect(self.searchAnimals)
        self.button_ser_show.clicked.connect(self.searchShow)
        self.button_ser_exb.clicked.connect(self.searchExhibit)
        self.button_view_show_his.clicked.connect(self.showHistory)
        self.button_view_exb_his.clicked.connect(self.exhibitHistory)

    def searchExhibit(self):
        __main__.status = __main__.statusDef['Normal']
        __main__.state = __main__.visitorUIs['visitorSearchExhibit']
        app.exit()

    def searchShow(self):
        __main__.status = __main__.statusDef['Normal']
        __main__.state = __main__.visitorUIs['visitorSearchShow']
        app.exit()

    def searchAnimals(self):
        __main__.status = __main__.statusDef['Normal']
        __main__.state = __main__.visitorUIs['visitorSearchAnimals']
        app.exit()

    def showHistory(self):
        __main__.status = __main__.statusDef['Normal']
        __main__.state = __main__.visitorUIs['visitorShowHistory']
        app.exit()

    def exhibitHistory(self):
        __main__.status = __main__.statusDef['Normal']
        __main__.state = __main__.visitorUIs['visitorExhibitHistory']
        app.exit()

    def logout(self):
        __main__.status = __main__.statusDef['Normal']
        __main__.state = __main__.visitorUIs['logout']
        app.exit()

def render():
    __main__.state = -10
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    app.exec_()
    # close the windows
    MainWindow.close()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

