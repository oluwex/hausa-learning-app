import sys
import db_connect as conn
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from ui_files import user_reg

class User_reg(QDialog, user_reg.Ui_Dialog):
    login = pyqtSignal(str, list, int)

    def __init__(self, parent=None):
        super(User_reg, self).__init__(parent)

        self.setupUi(self)

        self.route = conn.Connect()
        self.users = self.route.showUsers()

        self.setWindowFlags(Qt.WindowCloseButtonHint)

        self.name.setFocus()

    def createUser(self, username, user_type):
        return self.route.insert_db(username, user_type)

    def accept(self):
        self.msgbox = QMessageBox()
        username = self.name.text()
        if username:
            if username not in self.users:
                if self.createUser(username, 1):
                    self.msgbox.information(self, qApp.tr("Success"), qApp.tr("User " + username + " has been created!"),
                                                      QMessageBox.Ok)
                    self.login.emit(username, ['', ''], 1)
                    self.close()
                else:
                    self.msgbox.critical(self, qApp.tr("Error!"), qApp.tr("User '" + username + "' failed to create!"),
                                                      QMessageBox.Ok)
                    self.close()
            else:
                self.msgbox.critical(self, qApp.tr("Error!"), qApp.tr("User '" + username + "' already exists!"),
                                                      QMessageBox.Ok)

def main():
    app = QApplication(sys.argv)
    window = User_reg()
    window.show()
    app.exec_()

if __name__ == "__main__":
    main()