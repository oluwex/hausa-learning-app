import sys
import user_reg, login
import db_connect
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from ui_files import selectUser


class ChooseUser(QDialog, selectUser.Ui_Dialog):

    user = pyqtSignal(str, list, int)

    def __init__(self, parent=None):
        super(ChooseUser, self).__init__(parent)

        self.setupUi(self)

        self.setWindowFlags(Qt.WindowCloseButtonHint | Qt.WindowMinimizeButtonHint)

        self.userList.itemClicked[QListWidgetItem].connect(self.listUse)
        self.userList.itemChanged[QListWidgetItem].connect(self.edited)
        self.adminList.itemClicked[QListWidgetItem].connect(self.listUse)
        self.userList.itemDoubleClicked.connect(self.accept)
        self.adminList.itemDoubleClicked.connect(self.accept)
        self.tabWidget.currentChanged[int].connect(self.updateUI)

        self.conn = db_connect.Connect()

        self.populateList()

        self.isStart = True

    def populateList(self):
        global users
        global views
        users = []
        admin = []
        views = []
        result = self.conn.query_db('users')
        while result.next():
            if result.value(6) == 0:
                admin.append(result.value(4))
            else:
                users.append(result.value(4))
                views.append([result.value('lastViewedNumber'),result.value('lastViewedWord')])


        self.userList.addItems(users)
        self.adminList.addItems(admin)

    def closeEvent(self, close):
        if self.isStart:
            sys.exit()
        else:
            self.done(1)

    def reset(self):
        self.userList.clear()
        self.adminList.clear()
        self.populateList()

    @pyqtSlot(int)
    def updateUI(self, ind):
        if ind == 1:
            self.btn_continue.setText('Login')
            self.btn_new.setHidden(True)
            self.btn_edit.setHidden(True)
            self.btn_remove.setHidden(True)
        else:
            self.btn_continue.setText('Continue')
            self.btn_new.setHidden(False)
            self.btn_edit.setHidden(False)
            self.btn_remove.setHidden(False)

    @pyqtSlot(QListWidgetItem)
    def listUse(self, item):
        self.btn_continue.setDisabled(False)
        self.btn_edit.setDisabled(False)
        self.btn_remove.setDisabled(False)
        self.userdata = item

    @pyqtSlot()
    def accept(self):
        if self.userdata.listWidget().objectName() == "userList":
            self.user.emit(self.userdata.text(), views[users.index(self.userdata.text())], 1)
            self.hide()
        else:
            window = login.Start(self.userdata.text())
            window.login[str, list, int].connect(self.user)
            window.exec_()

        self.conn.close_db()

    @pyqtSlot()
    def on_btn_new_clicked(self):
        window = user_reg.User_reg()
        window.login[str, list, int].connect(self.user)
        window.exec_()

    @pyqtSlot()
    def on_btn_edit_clicked(self):
        self.userdata.setFlags(self.userdata.flags() | Qt.ItemIsEditable)
        self.userList.editItem(self.userdata)

    @pyqtSlot(QListWidgetItem)
    def edited(self, item):
        print(item.text())

    @pyqtSlot()
    def on_btn_remove_clicked(self):
        user = self.userdata.text()
        conn = db_connect.Connect()
        if conn.delete(user):
            QMessageBox.information(self, qApp.tr("Success"), qApp.tr(user + " successfully removed!"))
            self.reset()
        else:
            QMessageBox.information(self, 'Failed', user + ' failed to removed!\nTry again!')

    @pyqtSlot()
    def on_btn_exit_clicked(self):
        sys.exit()

def main():
    app = QApplication(sys.argv)
    window = ChooseUser()
    window.show()
    app.exec_()

if __name__ == '__main__':
    main()