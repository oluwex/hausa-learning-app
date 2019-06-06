import sys, time
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import QFont
from ui_files import history


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


class History(QDialog, history.Ui_Dialog):
    def __init__(self, history=None, parent=None):
        super(History, self).__init__(parent)

        self.history = history
        self.tableHeader = ["Item", "Type", 'Date Viewed']

        self.setupUi(self)
        self.createTable()

    def createTable(self):

        #   Table View customisation
        self.tableView.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tableView.setAlternatingRowColors(True)

        # set table model
        tm = MyTableModel(self.history, self.tableHeader, self)
        self.tableView.setModel(tm)

        #self.tableView.setShowGrid(False)

        #   set font
        font = QFont('Calibri', 11)
        self.tableView.setFont(font)

        vh = self.tableView.verticalHeader()
        vh.setVisible(False)

        hh = self.tableView.horizontalHeader()
        hh.setStretchLastSection(True)

        nrows = len(self.history)
        for row in range(nrows):
            self.tableView.setRowHeight(row, 18)

        #self.tableView.resizeColumnToContents(0)

def main():
    app = QApplication(sys.argv)
    window = History([["aduwa", "Alphabet"]])
    window.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()