import sys
import signup
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

class EditAdmin(signup.Signup):
    def __init__(self, username = None, parent=None):
        super(EditAdmin, self).__init__(parent)

        self.usernamee = username

        self.setWindowTitle("Edit Admin profile")

        self.updateUI()


    def updateUI(self):
        if self.usernamee is not None:
            rslt = self.route.queryUser(self.usernamee)
            if rslt.next():
                self.fname.setText(rslt.value(1))
                self.mname.setText(rslt.value(2))
                self.lname.setText(rslt.value(3))
                self.username.setText(rslt.value(4))
                self.password.setText(rslt.value(5))

    @pyqtSlot()
    def on_btn_submit_clicked(self):
        fname = self.fname.text()
        mname = self.mname.text()
        lname = self.lname.text()
        user = self.username.text()
        password = self.password.text()
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
            if user != self.usernamee:
                if user in self.route.showUsers():
                    self.msgbox.critical(self, qApp.tr("Information"),
                                        qApp.tr("Username already exists.\nPlease try another username"))
                    return
            if self.route.updateUser(fname,mname,lname,user,password,self.usernamee):
                self.msgbox.information(self, qApp.tr("Success"),
                                        qApp.tr("Admin profile successfully changed"), QMessageBox.Ok)
                self.close()
            else:
                self.msgbox.critical(self, qApp.tr("Failure"),
                                    qApp.tr("Admin profile failed to update"), QMessageBox.Ok)
        else:
            self.msgbox.critical(self, qApp.tr("Stop"), qApp.tr("Password is blank"))

def main():
    app = QApplication(sys.argv)
    window = EditAdmin("habeeb")
    window.show()
    app.exec()

if __name__ == "__main__":
    main()