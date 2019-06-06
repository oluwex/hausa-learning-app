import sys, os, shutil
import addWord
import db_connect as conn
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *


class EditWord(addWord.AddWord):
    def __init__(self, mode, item=None, alphabet = None, parent=None):
        super(EditWord, self).__init__(parent)

        self.alphabet = alphabet
        self.mode = mode
        self.currItem = item
        self.pixFile = ()
        self.image_name = "\\resources\images\\blank.png"

        #print(self.buttonBox.button(Qt.Save))

        if mode == 1:
            self.initUINums()
        else:
            self.initUIAlpha()

    def initUINums(self):
        self.disp.setText("Edit number")
        self.label.setText("Number digits")
        self.label_2.setText("Hausa number")
        self.label_3.setText("English number")
        self.label_4.setHidden(True)
        self.eExample.setHidden(True)
        self.label_5.setHidden(True)
        self.imageFileName.setHidden(True)
        self.btn_browse.setHidden(True)
        self.hExample.setText(self.currItem[0])
        self.hWord.setText(self.currItem[2])
        self.eWord.setText(self.currItem[1])

    def initUIAlpha(self):
        self.disp.setText("Edit Word")
        self.hWord.setText(self.currItem[0])
        self.eWord.setText(self.currItem[1])
        self.hExample.setText(self.currItem[2])
        self.eExample.setText(self.currItem[3])
        self.imageFileName.setText(self.currItem[4])

    def updateNum(self, route):
        if self.hWord.text() != self.currItem[1] or self.eWord.text() != self.currItem[0]:
            return route.updateNumerals(self.eWord.text(), self.hWord.text(), self.currItem[1])

    def updateWord(self, route):
        if self.hWord.text() != "" and self.eWord.text() != "":
            if self.hWord.text().startswith(self.alphabet) or self.hWord.text().startswith(self.alphabet.lower()):
                if len(self.pixFile) != 0:
                    extension = self.pixFile[0].split(".")[1]
                    self.image_name = "\\resources\images\\" + self.hWord.text() + "." + extension
                if route.updateAlpha(self.hWord.text().lower(), self.eWord.text().lower(),
                                 self.hExample.toPlainText().lower(), self.eExample.toPlainText().lower(),
                                 self.image_name, self.currItem[0]):

                    # This line of code copies the image into the images folder in resources directory
                    if len(self.pixFile) != 0:
                        if len(self.pixFile[0]):
                            print(self.pixFile)
                            shutil.copy2(self.pixFile[0], os.getcwd() + self.image_name)
                    return True
                else:
                    return False
            else:
                msgbox = QMessageBox()
                msgbox.critical(self, qApp.tr("Error!"),
                                qApp.tr(self.hWord.text()[0] + " does not start with \"" + self.alphabet + "\""))
        else:
            QMessageBox.information(self, qApp.tr("Warning!"),
                                    qApp.tr("Hausa word field or English gloss field should not be left empty!"))

    @pyqtSlot()
    def accept(self):
        route = conn.Connect()
        if self.mode == 0:
            if self.updateWord(route):
                self.done(1)
            else:
                self.done(0)
        else:
            if self.updateNum(route):
                self.done(1)
            else:
                self.done(0)

def main():
    app = QApplication(sys.argv)
    window = EditWord(0)
    window.show()
    app.exec_()

if __name__ == '__main__':
    main()