import sys
import db_connect as conn
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import QFont
from ui_files import userView

class MyTableModel(QAbstractTableModel):

    def __init__(self, datain, headerdata, parent=None, *args):
        super(MyTableModel, self).__init__(parent)

        self.userData = datain
        self.headerdata = headerdata

    def rowCount(self, parent):
        return len(self.userData)

    def columnCount(self, parent):
        return len(self.userData[0])

    def data(self, index, role):
        if not index.isValid():
            return QVariant()
        elif role != Qt.DisplayRole:
            return QVariant()
        return QVariant(self.userData[index.row()][index.column()])

    def headerData(self, col, orientation, role):
        if orientation == Qt.Horizontal and role == Qt.DisplayRole:
            return QVariant(self.headerdata[col])
        return QVariant()

class UserView(QDialog, userView.Ui_Dialog):
    def __init__(self, usertype, parent=None):
        super(UserView, self).__init__(parent)

        self.userType = usertype
        self.admin = []
        self.normalUsers = []

        self.setupUi(self)

        if self.userType == 0:
            self.tableHeader = ['', 'Username', 'Lastname', 'First Name', 'Middle Name']
            self.initUIAdmin()
        elif self.userType == 1:
            self.tableHeader = ['', 'Username', 'Alphabet percentage complete', 'Numerals percentage complete']
            self.initUIUser()

        self.route = self.connectDB()

        self.createTable()

    def initUIAdmin(self):
        self.label.setText("List of admin users")

    def initUIUser(self):
        self.label.setText("List of users")

    def connectDB(self):
        return conn.Connect()

    def users(self, type):
        ind = 0
        if type == 0:
            result = self.route.queryUsers(0)
            while result.next():
                ind+=1
                self.admin.append([ind, result.value('username'), result.value('lname'), result.value('fname')
                                      , result.value('midname')])
            return self.admin
        elif type == 1:
            result = self.route.queryUser(1)
            while result.next():
                ind+=1
                self.normalUsers.append([ind, result.value('username'), '0%', '0%'])
            return self.normalUsers

    def createTable(self):
        users = self.users(self.userType)

        #   Table View customisation
        self.tableView.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tableView.setAlternatingRowColors(True)

        # set table model
        tm = MyTableModel(users, self.tableHeader, self)
        self.tableView.setModel(tm)

        #   set font
        font = QFont('Calibri', 11)
        self.tableView.setFont(font)

        vh = self.tableView.verticalHeader()
        vh.setVisible(False)

        hh = self.tableView.horizontalHeader()
        hh.setStretchLastSection(True)

        nrows = len(users)
        for row in range(nrows):
            self.tableView.setRowHeight(row, 18)

        self.tableView.resizeColumnToContents(0)

def main():
    app = QApplication(sys.argv)
    window = UserView(1)
    window.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()