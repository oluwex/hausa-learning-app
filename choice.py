import sys
import alphaList
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from ui_files import numOrAlpha

class ChoosePg(QDialog, numOrAlpha.Ui_Dialog):

    numeral = pyqtSignal(str)
    alpha = pyqtSignal(str, str)

    def __init__(self, user, userview, parent=None):
        super(ChoosePg, self).__init__(parent)

        self.numberList = []
        self.userview = userview

        self.setupUi(self)

        self.label_2.setText("Choose your preferred choice, " + user)

    @pyqtSlot()
    def on_btn_number_clicked(self):
        self.numeral.emit(self.userview[0])
        #self.hide()

    @pyqtSlot()
    def on_btn_alpha_clicked(self):
        if self.userview[1] is None or len(self.userview[1]) == 0:
            self.alpha.emit(self.userview[1], self.userview[1])
        else:
            self.alpha.emit(self.userview[1][0], self.userview[1])
        #self.hide()

def main():
    app = QApplication(sys.argv)
    window = ChoosePg("Habeeb")
    window.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()