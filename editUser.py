import sys
import user_reg
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

class UserEdit(user_reg.User_reg):

    newUser = pyqtSignal(str)

    def __init__(self, username, parent=None):
        super(UserEdit, self).__init__(parent)

        self.oldUsername = username

        self.changeUI()

        self.name.setFocus()

    def changeUI(self):
        self.label.clear()
        self.label.setText("Enter new username")
        self.name.setText(self.oldUsername)

    def saveNewUsername(self):
        return self.route.updateUser(self.newUsername, self.oldUsername)

    def accept(self):
        self.newUsername = self.name.text()
        msgbox = QMessageBox()
        if self.newUsername != "":
            if self.newUsername == self.oldUsername:
                msgbox.information(self, qApp.tr("Information"), qApp.tr("Old username same as new username"))
            else:
                clickedButton = msgbox.question(self, qApp.tr("Confirm"), qApp.tr("Click yes to confirm username change"))
                if clickedButton == QMessageBox.Yes:
                    if self.saveNewUsername():
                        msgbox.information(self, qApp.tr("Success"), qApp.tr("Username successfully changed"))
                        self.newUser.emit(self.newUsername)
                        self.close()
        else:
            msgbox.critical(self, qApp.tr("Error"), qApp.tr("Username field is empty"))


def main():
    app = QApplication(sys.argv)
    window = UserEdit()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()