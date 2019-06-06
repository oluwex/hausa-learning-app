# -*- coding: utf-8 -*-

import sys
import db_connect as conn
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from ui_files import alphalist2


class AlphaList(QDialog, alphalist2.Ui_Dialog):

    letter = pyqtSignal(str)

    def __init__(self, word=None, parent=None):
        super(AlphaList, self).__init__(parent)

        self.route = conn.Connect()
        self.rslt = self.route.query_db('letters')

        self.buttonList = []


        """if len(self.word) != 0:
            self.goToWord()"""

        self.setupUi(self)
        self.setUI()

    @pyqtSlot()
    def goToWord(self):
        self.letter.emit(self.word[0].upper())
        self.accept()

    def setUI(self):
        row = 0
        ind = 0
        self.grid = QGridLayout()
        self.grid.setSpacing(20)
        self.grid.setContentsMargins(20, 6, 6, 6)
        self.grid.setVerticalSpacing(20)
        self.grid.setHorizontalSpacing(50)
        self.gridwidget = QWidget()
        self.gridwidget.setLayout(self.grid)
        self.scrollArea.setWidget(self.gridwidget)
        while self.rslt.next():
            for col in range(3):
                ind+=1
                if self.rslt.value(1):
                    self.alpha_btn = QPushButton(self.rslt.value(1), self)
                    self.alpha_btn.resize(120, 130)
                    self.alpha_btn.setMinimumSize(120, 130)
                    self.alpha_btn.setMaximumSize(120, 130)
                    self.alpha_btn.setObjectName("alpha_btn" + str(ind))
                    self.buttonList.append(self.alpha_btn)
                    self.grid.addWidget(self.alpha_btn, row, col)
                if col != 2:
                    self.rslt.next()
            row += 1
        for button in self.buttonList:
            button.clicked.connect(self.button_clicked)


    @pyqtSlot()
    def button_clicked(self):
        self.letter.emit(self.sender().text())
        self.accept()


def main():
    app = QApplication(sys.argv)
    window = AlphaList()
    window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
