# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'staffAnimalCare.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_staffAnimalCare(object):
    def setupUi(self, staffAnimalCare):
        staffAnimalCare.setObjectName("staffAnimalCare")
        staffAnimalCare.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(staffAnimalCare)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.HomePushButton = QtWidgets.QPushButton(self.centralwidget)
        self.HomePushButton.setMinimumSize(QtCore.QSize(95, 43))
        self.HomePushButton.setMaximumSize(QtCore.QSize(95, 43))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(15)
        self.HomePushButton.setFont(font)
        self.HomePushButton.setObjectName("HomePushButton")
        self.gridLayout.addWidget(self.HomePushButton, 0, 0, 1, 1)
        self.AnimalDetail = QtWidgets.QLabel(self.centralwidget)
        self.AnimalDetail.setMinimumSize(QtCore.QSize(221, 41))
        self.AnimalDetail.setMaximumSize(QtCore.QSize(221, 41))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(22)
        self.AnimalDetail.setFont(font)
        self.AnimalDetail.setObjectName("AnimalDetail")
        self.gridLayout.addWidget(self.AnimalDetail, 0, 1, 1, 2)
        self.AtlantaZoo = QtWidgets.QLabel(self.centralwidget)
        self.AtlantaZoo.setMinimumSize(QtCore.QSize(271, 31))
        self.AtlantaZoo.setMaximumSize(QtCore.QSize(271, 31))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(15)
        self.AtlantaZoo.setFont(font)
        self.AtlantaZoo.setObjectName("AtlantaZoo")
        self.gridLayout.addWidget(self.AtlantaZoo, 1, 0, 1, 3)
        self.Name = QtWidgets.QLabel(self.centralwidget)
        self.Name.setMinimumSize(QtCore.QSize(99, 56))
        self.Name.setMaximumSize(QtCore.QSize(99, 56))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.Name.setFont(font)
        self.Name.setObjectName("Name")
        self.gridLayout.addWidget(self.Name, 2, 0, 1, 1)
        self.NameLineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.NameLineEdit.setMinimumSize(QtCore.QSize(119, 34))
        self.NameLineEdit.setMaximumSize(QtCore.QSize(119, 34))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(11)
        self.NameLineEdit.setFont(font)
        self.NameLineEdit.setReadOnly(True)
        self.NameLineEdit.setObjectName("NameLineEdit")
        self.gridLayout.addWidget(self.NameLineEdit, 2, 1, 1, 1)
        self.Species = QtWidgets.QLabel(self.centralwidget)
        self.Species.setMinimumSize(QtCore.QSize(119, 56))
        self.Species.setMaximumSize(QtCore.QSize(119, 56))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.Species.setFont(font)
        self.Species.setObjectName("Species")
        self.gridLayout.addWidget(self.Species, 2, 2, 1, 1)
        self.SpeciesLineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.SpeciesLineEdit.setMinimumSize(QtCore.QSize(157, 38))
        self.SpeciesLineEdit.setMaximumSize(QtCore.QSize(157, 38))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(11)
        self.SpeciesLineEdit.setFont(font)
        self.SpeciesLineEdit.setReadOnly(True)
        self.SpeciesLineEdit.setObjectName("SpeciesLineEdit")
        self.gridLayout.addWidget(self.SpeciesLineEdit, 2, 3, 1, 1)
        self.Age = QtWidgets.QLabel(self.centralwidget)
        self.Age.setMinimumSize(QtCore.QSize(76, 39))
        self.Age.setMaximumSize(QtCore.QSize(76, 39))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.Age.setFont(font)
        self.Age.setObjectName("Age")
        self.gridLayout.addWidget(self.Age, 2, 4, 1, 1)
        self.AgeLineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.AgeLineEdit.setMinimumSize(QtCore.QSize(157, 38))
        self.AgeLineEdit.setMaximumSize(QtCore.QSize(157, 38))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(11)
        self.AgeLineEdit.setFont(font)
        self.AgeLineEdit.setReadOnly(True)
        self.AgeLineEdit.setObjectName("AgeLineEdit")
        self.gridLayout.addWidget(self.AgeLineEdit, 2, 5, 1, 1)
        self.Exhibit = QtWidgets.QLabel(self.centralwidget)
        self.Exhibit.setMinimumSize(QtCore.QSize(99, 56))
        self.Exhibit.setMaximumSize(QtCore.QSize(99, 56))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.Exhibit.setFont(font)
        self.Exhibit.setObjectName("Exhibit")
        self.gridLayout.addWidget(self.Exhibit, 3, 0, 1, 1)
        self.ExhibitLineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.ExhibitLineEdit.setMinimumSize(QtCore.QSize(119, 34))
        self.ExhibitLineEdit.setMaximumSize(QtCore.QSize(119, 34))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(11)
        self.ExhibitLineEdit.setFont(font)
        self.ExhibitLineEdit.setReadOnly(True)
        self.ExhibitLineEdit.setObjectName("ExhibitLineEdit")
        self.gridLayout.addWidget(self.ExhibitLineEdit, 3, 1, 1, 1)
        self.Type = QtWidgets.QLabel(self.centralwidget)
        self.Type.setMinimumSize(QtCore.QSize(119, 56))
        self.Type.setMaximumSize(QtCore.QSize(119, 56))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.Type.setFont(font)
        self.Type.setObjectName("Type")
        self.gridLayout.addWidget(self.Type, 3, 2, 1, 1)
        self.TypeLineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.TypeLineEdit.setMinimumSize(QtCore.QSize(157, 38))
        self.TypeLineEdit.setMaximumSize(QtCore.QSize(157, 38))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(11)
        self.TypeLineEdit.setFont(font)
        self.TypeLineEdit.setReadOnly(True)
        self.TypeLineEdit.setObjectName("TypeLineEdit")
        self.gridLayout.addWidget(self.TypeLineEdit, 3, 3, 1, 1)
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.NoteTextEdit = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.NoteTextEdit.setMinimumSize(QtCore.QSize(536, 121))
        self.NoteTextEdit.setMaximumSize(QtCore.QSize(536, 121))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(12)
        self.NoteTextEdit.setFont(font)
        self.NoteTextEdit.setObjectName("NoteTextEdit")
        self.gridLayout_2.addWidget(self.NoteTextEdit, 0, 0, 1, 1)
        self.LogNotesPushButton = QtWidgets.QPushButton(self.centralwidget)
        self.LogNotesPushButton.setMinimumSize(QtCore.QSize(151, 51))
        self.LogNotesPushButton.setMaximumSize(QtCore.QSize(151, 51))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(11)
        self.LogNotesPushButton.setFont(font)
        self.LogNotesPushButton.setObjectName("LogNotesPushButton")
        self.gridLayout_2.addWidget(self.LogNotesPushButton, 0, 1, 1, 1)
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setMinimumSize(QtCore.QSize(721, 192))
        self.tableWidget.setMaximumSize(QtCore.QSize(721, 192))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(9)
        self.tableWidget.setFont(font)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(3)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        self.gridLayout_2.addWidget(self.tableWidget, 1, 0, 1, 2)
        self.gridLayout.addLayout(self.gridLayout_2, 4, 0, 1, 6)
        self.gridLayout_3.addLayout(self.gridLayout, 0, 0, 1, 1)
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
        self.AnimalDetail.setText(_translate("staffAnimalCare", "Care"))
        self.AtlantaZoo.setText(_translate("staffAnimalCare", "Atlanta Zoo"))
        self.Name.setText(_translate("staffAnimalCare", "Name:"))
        self.Species.setText(_translate("staffAnimalCare", "Species:"))
        self.Age.setText(_translate("staffAnimalCare", "Age:"))
        self.Exhibit.setText(_translate("staffAnimalCare", "Exhibit:"))
        self.Type.setText(_translate("staffAnimalCare", "Type:"))
        self.LogNotesPushButton.setText(_translate("staffAnimalCare", "Log Notes"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("staffAnimalCare", "Staff Member"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("staffAnimalCare", "Note"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("staffAnimalCare", "Time"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    staffAnimalCare = QtWidgets.QMainWindow()
    ui = Ui_staffAnimalCare()
    ui.setupUi(staffAnimalCare)
    staffAnimalCare.show()
    sys.exit(app.exec_())

