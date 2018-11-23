

from PyQt5 import QtCore, QtGui, QtWidgets
from __main__ import connection_pool
# import the __main__ object to access the global variables: status, state, arg, loginIdentity
import __main__

import sys
app = QtWidgets.QApplication(sys.argv)
import util
class Ui_staffSearchAnimals(object):
    def setupUi(self, staffSearchAnimals):
        staffSearchAnimals.setObjectName("staffSearchAnimals")
        staffSearchAnimals.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(staffSearchAnimals)
        self.centralwidget.setObjectName("centralwidget")
        self.AtlantaZoo = QtWidgets.QLabel(self.centralwidget)
        self.AtlantaZoo.setGeometry(QtCore.QRect(10, 40, 391, 41))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(22)
        font.setBold(True)
        font.setWeight(75)
        self.AtlantaZoo.setFont(font)
        self.AtlantaZoo.setObjectName("AtlantaZoo")
        self.Name = QtWidgets.QLabel(self.centralwidget)
        self.Name.setGeometry(QtCore.QRect(30, 110, 71, 31))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.Name.setFont(font)
        self.Name.setObjectName("Name")
        self.Species = QtWidgets.QLabel(self.centralwidget)
        self.Species.setGeometry(QtCore.QRect(30, 200, 91, 31))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.Species.setFont(font)
        self.Species.setObjectName("Species")
        self.Type = QtWidgets.QLabel(self.centralwidget)
        self.Type.setGeometry(QtCore.QRect(420, 200, 81, 31))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.Type.setFont(font)
        self.Type.setObjectName("Type")
        self.Exhibit = QtWidgets.QLabel(self.centralwidget)
        self.Exhibit.setGeometry(QtCore.QRect(420, 30, 71, 31))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.Exhibit.setFont(font)
        self.Exhibit.setObjectName("Exhibit")
        self.Age = QtWidgets.QLabel(self.centralwidget)
        self.Age.setGeometry(QtCore.QRect(420, 110, 81, 31))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.Age.setFont(font)
        self.Age.setObjectName("Age")
        self.NameLineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.NameLineEdit.setGeometry(QtCore.QRect(130, 110, 181, 31))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(12)
        self.NameLineEdit.setFont(font)
        self.NameLineEdit.setText("")
        self.NameLineEdit.setObjectName("NameLineEdit")
        self.SpeciesLineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.SpeciesLineEdit.setGeometry(QtCore.QRect(130, 200, 181, 31))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(12)
        self.SpeciesLineEdit.setFont(font)
        self.SpeciesLineEdit.setText("")
        self.SpeciesLineEdit.setObjectName("SpeciesLineEdit")
        self.ExhibitComboBox = QtWidgets.QComboBox(self.centralwidget)
        self.ExhibitComboBox.setGeometry(QtCore.QRect(510, 30, 121, 31))
        self.ExhibitComboBox.setObjectName("ExhibitComboBox")
        self.ExhibitComboBox.addItem("")
        self.ExhibitComboBox.addItem("")
        self.ExhibitComboBox.addItem("")
        self.ExhibitComboBox.addItem("")
        self.ExhibitComboBox.addItem("")
        self.ExhibitComboBox.addItem("")
        self.Min = QtWidgets.QLabel(self.centralwidget)
        self.Min.setGeometry(QtCore.QRect(506, 93, 61, 20))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.Min.setFont(font)
        self.Min.setObjectName("Min")
        self.Max = QtWidgets.QLabel(self.centralwidget)
        self.Max.setGeometry(QtCore.QRect(586, 93, 51, 20))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.Max.setFont(font)
        self.Max.setObjectName("Max")
        self.MinSpinBox = QtWidgets.QSpinBox(self.centralwidget)
        self.MinSpinBox.setGeometry(QtCore.QRect(501, 120, 81, 31))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(11)
        self.MinSpinBox.setFont(font)
        self.MinSpinBox.setMinimum(0)
        #self.MinSpinBox.setMaximum(8)
        self.MinSpinBox.setObjectName("MinSpinBox")
        self.MaxSpinBox = QtWidgets.QSpinBox(self.centralwidget)
        self.MaxSpinBox.setGeometry(QtCore.QRect(590, 120, 71, 31))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(11)
        self.MaxSpinBox.setFont(font)
        self.MaxSpinBox.setMinimum(0)
        #self.MaxSpinBox.setMaximum(8)
        self.MaxSpinBox.setProperty("value", 0)
        self.MaxSpinBox.setObjectName("MaxSpinBox")
        self.TypeComboBox = QtWidgets.QComboBox(self.centralwidget)
        self.TypeComboBox.setGeometry(QtCore.QRect(510, 200, 121, 31))
        self.TypeComboBox.setObjectName("TypeComboBox")
        self.TypeComboBox.addItem("")
        self.TypeComboBox.addItem("")
        self.TypeComboBox.addItem("")
        self.TypeComboBox.addItem("")
        self.TypeComboBox.addItem("")
        self.HomePushButton = QtWidgets.QPushButton(self.centralwidget)
        self.HomePushButton.setGeometry(QtCore.QRect(0, 0, 75, 23))
        self.HomePushButton.setObjectName("HomePushButton")
        self.SearchPushButton = QtWidgets.QPushButton(self.centralwidget)
        self.SearchPushButton.setGeometry(QtCore.QRect(670, 200, 111, 31))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.SearchPushButton.setFont(font)
        self.SearchPushButton.setObjectName("SearchPushButton")
        self.AnimalTable = QtWidgets.QTableWidget(self.centralwidget)
        self.AnimalTable.setGeometry(QtCore.QRect(20, 270, 761, 281))
        self.AnimalTable.setObjectName("AnimalTable")
        self.AnimalTable.setColumnCount(5)
        self.AnimalTable.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.AnimalTable.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.AnimalTable.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.AnimalTable.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.AnimalTable.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.AnimalTable.setHorizontalHeaderItem(4, item)
        staffSearchAnimals.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(staffSearchAnimals)
        self.statusbar.setObjectName("statusbar")
        staffSearchAnimals.setStatusBar(self.statusbar)

        #ADDED
        self.userDefinedInitialization()

        self.retranslateUi(staffSearchAnimals)
        QtCore.QMetaObject.connectSlotsByName(staffSearchAnimals)

    def retranslateUi(self, staffSearchAnimals):
        _translate = QtCore.QCoreApplication.translate
        staffSearchAnimals.setWindowTitle(_translate("staffSearchAnimals", "Search Animals"))
        self.AtlantaZoo.setText(_translate("staffSearchAnimals", "Atlanta Zoo "))
        self.Name.setText(_translate("staffSearchAnimals", "Name"))
        self.Species.setText(_translate("staffSearchAnimals", "Species"))
        self.Type.setText(_translate("staffSearchAnimals", "Type"))
        self.Exhibit.setText(_translate("staffSearchAnimals", "Exhibit"))
        self.Age.setText(_translate("staffSearchAnimals", "Age"))
        self.ExhibitComboBox.setItemText(0, _translate("staffSearchAnimals", "All"))
        self.ExhibitComboBox.setItemText(1, _translate("staffSearchAnimals", "Pacific"))
        self.ExhibitComboBox.setItemText(2, _translate("staffSearchAnimals", "Jungle"))
        self.ExhibitComboBox.setItemText(3, _translate("staffSearchAnimals", "Sahara"))
        self.ExhibitComboBox.setItemText(4, _translate("staffSearchAnimals", "Mountainous"))
        self.ExhibitComboBox.setItemText(5, _translate("staffSearchAnimals", "Birds"))
        self.Min.setText(_translate("staffSearchAnimals", "Min"))
        self.Max.setText(_translate("staffSearchAnimals", "Max"))
        self.TypeComboBox.setItemText(0, _translate("staffSearchAnimals", "All"))
        self.TypeComboBox.setItemText(1, _translate("staffSearchAnimals", "Fish"))
        self.TypeComboBox.setItemText(2, _translate("staffSearchAnimals", "Amphibian"))
        self.TypeComboBox.setItemText(3, _translate("staffSearchAnimals", "Mammal"))
        self.TypeComboBox.setItemText(4, _translate("staffSearchAnimals", "Bird"))
        self.HomePushButton.setText(_translate("staffSearchAnimals", "Home"))
        self.SearchPushButton.setText(_translate("staffSearchAnimals", "Search"))
        item = self.AnimalTable.horizontalHeaderItem(0)
        item.setText(_translate("staffSearchAnimals", "Name"))
        item = self.AnimalTable.horizontalHeaderItem(1)
        item.setText(_translate("staffSearchAnimals", "Species"))
        item = self.AnimalTable.horizontalHeaderItem(2)
        item.setText(_translate("staffSearchAnimals", "Exhibit"))
        item = self.AnimalTable.horizontalHeaderItem(3)
        item.setText(_translate("staffSearchAnimals", "Age"))
        item = self.AnimalTable.horizontalHeaderItem(4)
        item.setText(_translate("staffSearchAnimals", "Type"))

    def userDefinedInitialization(self):
        self.SearchPushButton.clicked.connect(self.SearchAnimals)
        self.HomePushButton.clicked.connect(self.home)
        self.AnimalTable.cellClicked.connect(self.highlightRowOrToAnimal)

    def SearchAnimals(self):
        Name = self.NameLineEdit.text()
        Species = self.SpeciesLineEdit.text()
        Exhibit = self.ExhibitComboBox.currentText()
        Type = self.TypeComboBox.currentText()
        MaxAge = self.MaxSpinBox.value()
        MinAge = self.MinSpinBox.value()

        if (Exhibit == "All"):
            Exhibit = ""
        if (Type == "All"):
            Type = ""
        if (MaxAge == 0 and MinAge == 0):
            MaxAge = ''
            MinAge = ''
        listTuple = [("Name", Name, "str"), ("Species", Species, "str"),("Exhibit",Exhibit, "str"),("Type", Type, "str"),("MinAge", MinAge, "int"),("MaxAge", MaxAge, "int")]
        cmd1 = "SELECT Name, Species, Exhibit,Age, Type FROM ANIMAL"
        cmd1 = util.addWHERE(cmd1,listTuple)
        connection_object = connection_pool.get_connection()
        if connection_object.is_connected():
            db_Info = connection_object.get_server_info()
            print("Connected to MySQL database using connection pool ... MySQL Server version on ",db_Info)

        cursor = connection_object.cursor()
        cursor.execute(cmd1)
        record = cursor.fetchall()

        print(record)
        self.AnimalTable.setRowCount(0)
        for row_number, row_data in enumerate(record):
            self.AnimalTable.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.AnimalTable.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))



        if(connection_object.is_connected()):
            cursor.close()
            connection_object.close()
            print("MySQL connection is closed")

    def highlightRowOrToAnimal(self,row, column):
        self.AnimalTable.selectRow(row)
        if (column == 0 ):
            Name = str(self.AnimalTable.item(row,column).text())
            Species = str(self.AnimalTable.item(row,column+1).text())
            __main__.arg = [("Name", Name, "str"), ("Species", Species, "str")]
            __main__.status = __main__.statusDef["Normal"]
            __main__.state = __main__.staffUIs["staffAnimalCare"]
            app.exit()


    def home(self):
        __main__.status = __main__.statusDef['Normal']
        __main__.state = __main__.staffUIs['staffFunctionality'] # Login Page
        app.exit()

def render():
    __main__.state = -10
    staffSearchAnimals = QtWidgets.QMainWindow()
    ui = Ui_staffSearchAnimals()
    ui.setupUi(staffSearchAnimals)
    staffSearchAnimals.show()
    app.exec_()
    # close the WINDOWS
    staffSearchAnimals.close()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    staffSearchAnimals = QtWidgets.QMainWindow()
    ui = Ui_staffSearchAnimals()
    ui.setupUi(staffSearchAnimals)
    staffSearchAnimals.show()
    app.exec_()
    staffSearchAnimals.close()