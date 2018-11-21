# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'staffAnimalCare.ui'
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

import util

import time

import sys
app = QtWidgets.QApplication(sys.argv)
################################################################################################
class Ui_staffAnimalCare(object):
    def setupUi(self, staffAnimalCare):
        staffAnimalCare.setObjectName("staffAnimalCare")
        staffAnimalCare.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(staffAnimalCare)
        self.centralwidget.setObjectName("centralwidget")
        self.HomePushButton = QtWidgets.QPushButton(self.centralwidget)
        self.HomePushButton.setGeometry(QtCore.QRect(0, 0, 95, 43))
        self.HomePushButton.setMinimumSize(QtCore.QSize(95, 43))
        self.HomePushButton.setMaximumSize(QtCore.QSize(95, 43))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(15)
        self.HomePushButton.setFont(font)
        self.HomePushButton.setObjectName("HomePushButton")
        self.AnimalDetail = QtWidgets.QLabel(self.centralwidget)
        self.AnimalDetail.setGeometry(QtCore.QRect(270, 30, 221, 41))
        self.AnimalDetail.setMinimumSize(QtCore.QSize(221, 41))
        self.AnimalDetail.setMaximumSize(QtCore.QSize(221, 41))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(22)
        self.AnimalDetail.setFont(font)
        self.AnimalDetail.setObjectName("AnimalDetail")
        self.AtlantaZoo = QtWidgets.QLabel(self.centralwidget)
        self.AtlantaZoo.setGeometry(QtCore.QRect(40, 80, 271, 31))
        self.AtlantaZoo.setMinimumSize(QtCore.QSize(271, 31))
        self.AtlantaZoo.setMaximumSize(QtCore.QSize(271, 31))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(15)
        self.AtlantaZoo.setFont(font)
        self.AtlantaZoo.setObjectName("AtlantaZoo")
        self.NoteTextEdit = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.NoteTextEdit.setGeometry(QtCore.QRect(40, 250, 536, 121))
        self.NoteTextEdit.setMinimumSize(QtCore.QSize(536, 121))
        self.NoteTextEdit.setMaximumSize(QtCore.QSize(536, 121))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(12)
        self.NoteTextEdit.setFont(font)
        self.NoteTextEdit.setObjectName("NoteTextEdit")
        self.LogNotesPushButton = QtWidgets.QPushButton(self.centralwidget)
        self.LogNotesPushButton.setGeometry(QtCore.QRect(600, 280, 151, 51))
        self.LogNotesPushButton.setMinimumSize(QtCore.QSize(151, 51))
        self.LogNotesPushButton.setMaximumSize(QtCore.QSize(151, 51))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(11)
        self.LogNotesPushButton.setFont(font)
        self.LogNotesPushButton.setObjectName("LogNotesPushButton")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(40, 380, 721, 192))
        self.tableWidget.setMinimumSize(QtCore.QSize(721, 192))
        self.tableWidget.setMaximumSize(QtCore.QSize(721, 192))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(3)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(240, 120, 121, 121))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.Species = QtWidgets.QLabel(self.layoutWidget)
        self.Species.setMinimumSize(QtCore.QSize(119, 56))
        self.Species.setMaximumSize(QtCore.QSize(119, 56))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.Species.setFont(font)
        self.Species.setObjectName("Species")
        self.verticalLayout_3.addWidget(self.Species)
        self.Type = QtWidgets.QLabel(self.layoutWidget)
        self.Type.setMinimumSize(QtCore.QSize(119, 56))
        self.Type.setMaximumSize(QtCore.QSize(119, 56))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.Type.setFont(font)
        self.Type.setObjectName("Type")
        self.verticalLayout_3.addWidget(self.Type)
        self.layoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget_2.setGeometry(QtCore.QRect(360, 120, 141, 121))
        self.layoutWidget_2.setObjectName("layoutWidget_2")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.layoutWidget_2)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.SpeciesName = QtWidgets.QLabel(self.layoutWidget_2)
        self.SpeciesName.setMinimumSize(QtCore.QSize(139, 56))
        self.SpeciesName.setMaximumSize(QtCore.QSize(139, 56))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(11)
        self.SpeciesName.setFont(font)
        self.SpeciesName.setObjectName("SpeciesName")
        self.verticalLayout_4.addWidget(self.SpeciesName)
        self.TypeName = QtWidgets.QLabel(self.layoutWidget_2)
        self.TypeName.setMinimumSize(QtCore.QSize(139, 56))
        self.TypeName.setMaximumSize(QtCore.QSize(139, 56))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(11)
        self.TypeName.setFont(font)
        self.TypeName.setObjectName("TypeName")
        self.verticalLayout_4.addWidget(self.TypeName)
        self.layoutWidget1 = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget1.setGeometry(QtCore.QRect(40, 120, 101, 121))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget1)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.Name = QtWidgets.QLabel(self.layoutWidget1)
        self.Name.setMinimumSize(QtCore.QSize(99, 56))
        self.Name.setMaximumSize(QtCore.QSize(99, 56))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.Name.setFont(font)
        self.Name.setObjectName("Name")
        self.verticalLayout.addWidget(self.Name)
        self.Exhibit = QtWidgets.QLabel(self.layoutWidget1)
        self.Exhibit.setMinimumSize(QtCore.QSize(99, 56))
        self.Exhibit.setMaximumSize(QtCore.QSize(99, 56))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.Exhibit.setFont(font)
        self.Exhibit.setObjectName("Exhibit")
        self.verticalLayout.addWidget(self.Exhibit)
        self.layoutWidget2 = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget2.setGeometry(QtCore.QRect(141, 120, 101, 121))
        self.layoutWidget2.setObjectName("layoutWidget2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.layoutWidget2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.AnimalName = QtWidgets.QLabel(self.layoutWidget2)
        self.AnimalName.setMinimumSize(QtCore.QSize(99, 56))
        self.AnimalName.setMaximumSize(QtCore.QSize(99, 56))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(11)
        self.AnimalName.setFont(font)
        self.AnimalName.setObjectName("AnimalName")
        self.verticalLayout_2.addWidget(self.AnimalName)
        self.ExhibitName = QtWidgets.QLabel(self.layoutWidget2)
        self.ExhibitName.setMinimumSize(QtCore.QSize(99, 56))
        self.ExhibitName.setMaximumSize(QtCore.QSize(99, 56))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(11)
        self.ExhibitName.setFont(font)
        self.ExhibitName.setObjectName("ExhibitName")
        self.verticalLayout_2.addWidget(self.ExhibitName)
        self.layoutWidget3 = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget3.setGeometry(QtCore.QRect(500, 120, 161, 41))
        self.layoutWidget3.setMinimumSize(QtCore.QSize(161, 41))
        self.layoutWidget3.setMaximumSize(QtCore.QSize(161, 41))
        self.layoutWidget3.setObjectName("layoutWidget3")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget3)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.Age = QtWidgets.QLabel(self.layoutWidget3)
        self.Age.setMinimumSize(QtCore.QSize(76, 39))
        self.Age.setMaximumSize(QtCore.QSize(76, 39))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.Age.setFont(font)
        self.Age.setObjectName("Age")
        self.horizontalLayout.addWidget(self.Age)
        self.AgeName = QtWidgets.QLabel(self.layoutWidget3)
        self.AgeName.setMinimumSize(QtCore.QSize(76, 39))
        self.AgeName.setMaximumSize(QtCore.QSize(76, 39))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(11)
        self.AgeName.setFont(font)
        self.AgeName.setObjectName("AgeName")
        self.horizontalLayout.addWidget(self.AgeName)
        staffAnimalCare.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(staffAnimalCare)
        self.statusbar.setObjectName("statusbar")
        staffAnimalCare.setStatusBar(self.statusbar)

        self.retranslateUi(staffAnimalCare)
        QtCore.QMetaObject.connectSlotsByName(staffAnimalCare)

    def retranslateUi(self, staffAnimalCare):
        _translate = QtCore.QCoreApplication.translate
        staffAnimalCare.setWindowTitle(_translate("staffAnimalCare", "MainWindow"))
        self.HomePushButton.setText(_translate("staffAnimalCare", "Home"))
        self.AnimalDetail.setText(_translate("staffAnimalCare", "Animal Detail"))
        self.AtlantaZoo.setText(_translate("staffAnimalCare", "Atlanta Zoo"))
        self.LogNotesPushButton.setText(_translate("staffAnimalCare", "Log Notes"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("staffAnimalCare", "Staff Member"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("staffAnimalCare", "Note"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("staffAnimalCare", "Time"))
        self.Species.setText(_translate("staffAnimalCare", "Species:"))
        self.Type.setText(_translate("staffAnimalCare", "Type:"))
        self.SpeciesName.setText(_translate("staffAnimalCare", "GoldFish"))
        self.TypeName.setText(_translate("staffAnimalCare", "Fish"))
        self.Name.setText(_translate("staffAnimalCare", "Name:"))
        self.Exhibit.setText(_translate("staffAnimalCare", "Exhibit:"))
        self.AnimalName.setText(_translate("staffAnimalCare", "Goldy"))
        self.ExhibitName.setText(_translate("staffAnimalCare", "Pacific"))
        self.Age.setText(_translate("staffAnimalCare", "Age:"))
        self.AgeName.setText(_translate("staffAnimalCare", "1 year"))

def render():
    __main__.state = -10
    staffAnimalCare = QtWidgets.QMainWindow()
    ui = Ui_staffAnimalCare()
    ui.setupUi(staffAnimalCare)
    staffAnimalCare.show()
    app.exec_()
    # close the staffAnimalCare window
    staffAnimalCare.close()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    staffAnimalCare = QtWidgets.QMainWindow()
    ui = Ui_staffAnimalCare()
    ui.setupUi(staffAnimalCare)
    staffAnimalCare.show()
    sys.exit(app.exec_())

