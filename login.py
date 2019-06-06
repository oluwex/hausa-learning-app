import sys
import signup
import db_connect as conn
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from ui_files import login


class Start(QDialog, login.Ui_Dialog):

    login = pyqtSignal(str, list, int)

    def __init__(self, user, parent=None):
        super(Start, self).__init__(parent)

        self.admin = user

        self.setupUi(self)

        self.userName.setText(user)

        self.password.setFocus()

        #------------------DB connect---------------------------#
        route = conn.Connect()
        self._dbPass = route.query_db('users', self.admin)

    def reset(self):
        self.password.clear()

    @pyqtSlot()
    def on_btn_login_clicked(self):
        passwordd = self.password.text()
        if passwordd != "":
            if self._dbPass.next():
                self.userPass = self._dbPass.value(0)
            if passwordd == self.userPass:
                self.login.emit(self.admin, ["",""], 0)
                QMessageBox.information(self, qApp.tr("Login successful"), qApp.tr(self.admin + " logged in as admin"))
                self.close()
            else:
                QMessageBox.critical(self, qApp.tr("Sign in failed"),
                                     qApp.tr("Passsword is incorrect"))
                self.reset()
        else:
            QMessageBox.critical(self, qApp.tr('Error'), qApp.tr('You failed to enter password'))

    @pyqtSlot()
    def on_btn_signup_clicked(self):
        window = signup.Signup(self)
        window.exec_()

def main():
    app = QApplication(sys.argv)
    window = Start("habeeb")
    window.exec_()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()