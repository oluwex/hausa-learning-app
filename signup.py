import sys
import db_connect as connect
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from ui_files import signup

class Signup(QDialog, signup.Ui_Form):
    def __init__(self, parent=None):
        super(Signup, self).__init__(parent)

        self.route = connect.Connect()

        self.setupUi(self)


    @pyqtSlot()
    def on_btn_submit_clicked(self):
        fname = self.fname.text()
        mname = self.mname.text()
        lname = self.lname.text()
        user = self.username.text()
        password = self.password.text()
        user_type = 0
        self.msgbox = QMessageBox()
        if fname == "":
            QMessageBox.critical(self, qApp.tr("Stop"), qApp.tr("First name is blank"))
            return
        if mname == "":
            QMessageBox.critical(self, qApp.tr("Stop"), qApp.tr("Middle name is blank"))
            return
        if lname == "":
            QMessageBox.critical(self, qApp.tr("Stop"), qApp.tr("Last name is blank"))
            return
        if user == "":
            QMessageBox.critical(self, qApp.tr("Stop"), qApp.tr("Username is blank"))
            return
        if password != "":
            if user in self.route.showUsers():
                self.msgbox.critical(self, qApp.tr("Information"),
                                        qApp.tr("Username already exists.\nPlease try another username"))
                return
            if self.route.insert_db(fname,mname,lname,user,password,user_type):
                self.msgbox.information(self, qApp.tr("Success"),
                                        qApp.tr('User ' + user + " successfully added as admin"), QMessageBox.Ok)
                self.close()
            else:
                self.msgbox.critical(self, qApp.tr("Failure"),
                                    qApp.tr('User ' + user + ' failed to create'), QMessageBox.Ok)
        else:
            self.msgbox.critical(self, qApp.tr("Stop"), qApp.tr("Password is blank"))


def main():
    app = QApplication(sys.argv)
    window = Signup()
    window.show()
    app.exec_()

if __name__ == '__main__':
    main()