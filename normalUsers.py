import sys
import db_connect as conn
from ui_files import normalUserView
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

class MyTableModel(QAbstractTableModel):

    def __init__(self, datain, headerdata, parent=None, *args):
        super(MyTableModel, self).__init__(parent)

        self.historyData = datain
        self.headerdata = headerdata

    def rowCount(self, parent):
        return len(self.historyData)

    def columnCount(self, parent):
        return len(self.historyData[0])

    def data(self, index, role):
        if not index.isValid():
            return QVariant()
        elif role != Qt.DisplayRole:
            return QVariant()
        return QVariant(self.historyData[index.row()][index.column()])

    def headerData(self, col, orientation, role):
        if orientation == Qt.Horizontal and role == Qt.DisplayRole:
            return QVariant(self.headerdata[col])
        return QVariant()


class NormalUsers(QDialog, normalUserView.Ui_Dialog):
    def __init__(self, parent=None):
        super(NormalUsers, self).__init__(parent)

        self.users = []
        self.words = []
        self.numbers = []

        self.numbersHeaderData = ['Number', 'Date Viewed']
        self.alphaHeaderData = ['Word', 'Alphabet', 'Date Viewed']

        self.setupUi(self)
        self.comboBox.activated[str].connect(self.setUserInfo)

        self.route = self.connectDB()

        self.populateComboBox()

    def connectDB(self):
        return conn.Connect()

    def retrieveUsers(self):
        result = self.route.queryUsers(1)
        while result.next():
            self.users.append([result.value('username')])

    def populateComboBox(self):
        self.retrieveUsers()
        self.comboBox.addItem("Choose...")
        for user in self.users:
            self.comboBox.addItem(user[0])

    @pyqtSlot(str)
    def setUserInfo(self, user):
        self.alphaTable.reset()
        self.numberTable.reset()
        result = self.route.getHistory(user)
        while result.next():
            if result.value('entry_type') == 'Word':
                word = result.value('entry')
                self.words.append([result.value('entry'), word[0].upper(), result.value('view_date')])
            else:
                self.numbers.append([result.value('entry'), result.value('view_date')])

        if len(self.words) != 0:
            self.createTableAlpha()
        if len(self.numbers) != 0:
            self.createTableNumeral()

    def createTableAlpha(self):
        self.alphaTable.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.alphaTable.setAlternatingRowColors(True)

        tm = MyTableModel(self.words, self.alphaHeaderData)
        self.alphaTable.setModel(tm)

        #   set font
        font = QFont('Calibri', 11)
        self.alphaTable.setFont(font)

        vh = self.alphaTable.verticalHeader()
        vh.setVisible(False)

        hh = self.alphaTable.horizontalHeader()
        hh.setStretchLastSection(True)

        nrows = len(self.words)
        for row in range(nrows):
            self.alphaTable.setRowHeight(row, 18)

        self.alphaTable.resizeColumnToContents(0)
        self.alphaTable.setColumnWidth(1, 60)

    def createTableNumeral(self):
        self.numberTable.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.numberTable.setAlternatingRowColors(True)

        tm = MyTableModel(self.numbers, self.numbersHeaderData)
        self.numberTable.setModel(tm)

        #   set font
        font = QFont('Calibri', 11)
        self.numberTable.setFont(font)

        vh = self.numberTable.verticalHeader()
        vh.setVisible(False)

        hh = self.numberTable.horizontalHeader()
        hh.setStretchLastSection(True)

        nrows = len(self.numbers)
        for row in range(nrows):
            self.numberTable.setRowHeight(row, 18)
            self.numberTable.setColumnWidth(0, 15)

        self.numberTable.resizeColumnToContents(0)


def main():
    app = QApplication(sys.argv)
    window = NormalUsers()
    window.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()