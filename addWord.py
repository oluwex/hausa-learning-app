import sys, shutil, os
import db_connect as conn
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from ui_files import addWord

class AddWord(QDialog, addWord.Ui_Form):
    def __init__(self, mode, alphabet=None, parent=None):
        super(AddWord, self).__init__(parent)

        self.alphabet = alphabet
        self.mode = mode
        self.pixFile = ()
        self.image_name = "\\resources\images\\blank.png"

        self.foreignKeys = {"A":1,"B":2,"C":3,"D":4,"E":5,"F":6,"G":7,"H":8,"I":9,"J":10
            ,"K":11,"L":12,"M":13,"N":14,"O":15,"R":16,"S":17,"T":18,"U":19,"W":20,"Y":21,"Z":22}

        self.setupUi(self)

        self.fileBrowser = QFileDialog()

        self.buttonBox.button(self.buttonBox.Save).clicked.connect(self.accept)
        self.buttonBox.button(self.buttonBox.Cancel).clicked.connect(self.close)

        if mode == 1:
            self.initUINums()

    def initUINums(self):
        self.disp.setText("Add number")
        self.label.setText("Enter number digit(s)")
        self.label_2.setText("Hausa number")
        self.label_3.setText("English number")
        self.label_4.setHidden(True)
        self.eExample.setHidden(True)
        self.label_5.setHidden(True)
        self.imageFileName.setHidden(True)
        self.btn_browse.setHidden(True)

    def addAlpha(self, route):
        if self.hWord.text() != "" and self.eWord.text() != "":
            if self.hWord.text().startswith(self.alphabet) or self.hWord.text().startswith(self.alphabet.lower()):
                if len(self.pixFile) != 0:
                    extension = self.pixFile[0].split(".")[1]
                    self.image_name = "\\resources\images\\" + self.hWord.text() + "." + extension
                if route.addWord(self.hWord.text().lower(), self.eWord.text().lower(),
                                     self.hExample.toPlainText().lower(), self.eExample.toPlainText().lower(),
                                     self.foreignKeys[self.hWord.text()[0].upper()], self.image_name):

                    # This line of code copies the image into the images folder in resources directory
                    if len(self.pixFile) != 0:
                        shutil.copy2(self.pixFile[0], os.getcwd() + self.image_name)
                    return True
                else:
                    return False
            else:
                msgbox = QMessageBox()
                msgbox.critical(self, qApp.tr("Error!"),
                                qApp.tr("Select letter \"" + self.hWord.text()[0] + "\" and add word from there"))
        else:
            QMessageBox.information(self, qApp.tr("Warning!"),
                                    qApp.tr("Hausa word field or English gloss field should not be left empty!"))

    def addNum(self, route):
        if self.hWord.text() != "" and self.eWord.text() != "":
            if self.hWord.text().isdigit():
                return route.addNumerals(self.hWord.text(), self.hExample.toPlainText().lower(), self.eWord.text())
            else:
                QMessageBox.critical(self, qApp.tr("Stop!"), qApp.tr("Alphabet inputted in number digit field"))
                return False
        else:
            QMessageBox.critical(self, qApp.tr("Stop"), qApp.tr("Hausa number field or English number field is blank"))

    @pyqtSlot()
    def on_btn_browse_clicked(self):
        self.pixFile = QFileDialog.getOpenFileName(self, qApp.tr("Select Image"), QDir.homePath() + "/Pictures",
                                              qApp.tr("Image (*.png *.jpg *.jpeg)"))
        self.imageFileName.setText(self.pixFile[0].split("/")[-1])

    def accept(self):
        route = conn.Connect()
        if self.mode == 0:
            if self.addAlpha(route):
                self.done(1)
            """else:
                self.done(0)"""
        elif self.mode == 1:
            if self.addNum(route):
                self.done(1)
            """else:
                self.done(0)"""

def main():
    app = QApplication(sys.argv)
    window = AddWord(1)
    window.show()
    app.exec_()

if __name__ == '__main__':
    main()