import sys, os, time
import choose_user, choice, signup, addWord, editWord, alphaList, history, editUser, editAdmin, users, normalUsers
import db_connect as conn
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from ui_files import mainwindow

_translate = QCoreApplication.translate


class MainWindow(QMainWindow, mainwindow.Ui_MainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)

        self._lastViewedNum = None
        self._lastViewedWord = None
        self.nums = []
        self.words = []
        self.view = None
        self.route = None
        self.alphabet = ""
        #self.history = deque()
        self.history = list()
        self.index = -1
        self.userview = None

        self.userwindow = choose_user.ChooseUser()
        self.userwindow.user[str,list,int].connect(self.loadUI)
        self.userwindow.exec_()
        self.userwindow.isStart = False

        QTimer.singleShot(100, self.showChoosepg)
        self.setWindowFlags(Qt.WindowMinimizeButtonHint | Qt.WindowCloseButtonHint)

        self.setDisabled(True)

        #self.itemList.setHidden(True)

        #self.itemList.setFocus()

    def showChoosepg(self):
        self.choose = choice.ChoosePg(self.username, self.userview)
        self.choose.numeral[str].connect(self.numToList)
        self.choose.alpha[str, str].connect(self.selectLetter)
        self.choose.exec_()

    def connect(self):
        return conn.Connect()

    def center(self):
        frameGm = self.frameGeometry()
        screen = QApplication.desktop().screenNumber(QApplication.desktop().cursor().pos())
        centerPoint = QApplication.desktop().screenGeometry(screen).center()
        frameGm.moveCenter(centerPoint)
        self.move(frameGm.topLeft())

    """def populateAlphaList(self, item):
        #self.itemList.addItem(item)
        return"""

    def reset(self):
        self.setDisabled(True)
        for item in self.findChildren((QLabel, QListWidget, QTextBrowser)):
            item.clear()
        self.history.clear()

    @pyqtSlot()
    def closeEvent(self, close):
        msgBox = QMessageBox()
        clickedButton = msgBox.question(self, qApp.tr("Confirm Exit"),
                               qApp.tr("Are you sure you want to exit Yin Koiyo Hausa?"))
        if clickedButton == QMessageBox.Yes:
            if self.user_type == 1:
                self.saveHistory()
        else:
            close.ignore()

    @pyqtSlot()
    def saveHistory(self):
        if self.user_type == 1:
            viewedNums = []
            viewedAlphas = []
            entries = []
            newHist1 = []   #   List of entries to be updated
            newHist2 = []   #   List of entries to be inserted
            result = self.route.checkHistory(self.username)
            while result.next():
                entries.append(result.value('entry'))
            for item in self.history:
                if item[0] in entries: #    viewedAlphas or item in viewedNums:
                    #mode = 1  #   Mode 1 means update is needed not insertion in db
                    newHist1.append(item)
                else:
                    #mode = 0
                    newHist2.append(item)

        #   Save History
            self.route.saveHistory(newHist1, self.username, 1)
            self.route.saveHistory(newHist2, self.username, 0)

        #   save last item viewed
            if self.route.saveLastItemViewed(self.username, self._lastViewedNum, self._lastViewedWord):
                pass
            else:
                print("last viewed not saved")
        #print(self.history)

    @pyqtSlot(int)
    def setItemInfo(self, ind):
        """
        This method sets the information of the highlighted row on the other widget
        :return: None
        """
        pix = QPixmap()
        if self.view == 1:
            if len(self.nums) != 0:
                self.itemDisp.setText(self.nums[ind][1] + " (" + self.nums[ind][0] + ")")

                #   Load number pix
                self.pixDisp.setText(self.nums[ind][2])
                self.label_example.clear()
                """if pix.load(os.getcwd() + "\\resources\images\\blank.png"):
                    self.pixDisp.setPixmap(pix)"""

                #   Add number entry to history
                for item in self.history:
                    if self.nums[ind][1] in item:
                        self.history.remove(item)
                #if [self.nums[ind][0], "Numeral"] in self.history:
                    #self.history.remove([self.nums[ind][0], 'Numeral'])
                self.history.append([self.nums[ind][1], 'Numeral', time.strftime('%d-%m-%y')])

                self._lastViewedNum = self.nums[ind][1]

        elif self.view == 0:
            if len(self.words) != 0:
                self.itemDisp.setText(self.words[ind][0] + " (" + self.words[ind][1] + ")")
                example = "<font color = 'brown'>" + self.words[ind][2] + "</font> (" + self.words[ind][3] + ")"
                self.label_example.setText("Example: " + example)

                if pix.load(os.getcwd() + self.words[ind][4]):
                    self.pixDisp.setPixmap(pix)

                #   Add word to history
                for item in self.history:
                    if self.words[ind][0] in item:
                        self.history.remove(item)
                self.history.append([self.words[ind][0], 'Word', time.strftime('%d-%m-%y')])
                """if not [self.words[ind][0], "Word"] in self.history:
                    self.history.appendleft([self.words[ind][0], "Word"])"""

                self._lastViewedWord = self.words[ind][0]
            #self.itemDisp.setText(self.words[row][1])
        #self.textBrowser.append("Numeral: <font color='black'>" + str(row+1) + '</font>')

    @pyqtSlot(str, list, int)
    def loadUI(self, user, views, user_type):
        self.index = -1
        self.username = user
        self.userview = views
        self._lastViewedNum = self.userview[0]
        self._lastViewedWord = self.userview[1]
        print('last viewed word is ' + self._lastViewedWord)
        self.user_type = user_type
        if self.view is None:
            self.setupUi(self)
        widgets = [self.actionAdd_new_user,
            self.actionAdd_Word,
            self.actionEdit_Word,
            self.actionRemove_word]
        self.actionUser.setDisabled(True)
        self.center()
        if user_type == 0:
            for item in widgets:
                item.setVisible(True)
            self.actionAdd_new_user.setDisabled(False)
            self.actionAdd_Word.setDisabled(False)
            self.actionEdit_Word.setDisabled(False)
            self.actionRemove_word.setDisabled(False)
            self.actionLogout.setText('Logout')
            self.actionAdd_new_user.setText("Add new admin")
            self.menu.setHidden(False)
        else:
            for item in widgets:
                item.setVisible(False)
            self.actionLogout.setText("Switch Users")
            self.menu.setHidden(True)
        self.actionUser.setText(self.username)
        self.actionUser.setToolTip(self.username)
        self.sender().hide()

    @pyqtSlot(str, str)
    def selectLetter(self, view=None, view2=None):
        if view is None or len(view) == 0:
            alphaPg = alphaList.AlphaList()
            alphaPg.letter[str].connect(self.alphaToList)
            return alphaPg.exec()
        else:
            self.alphaToList(self._lastViewedWord[0].upper())

    @pyqtSlot(str)
    def numToList(self, num=None):
        self._lastViewedNum = num
        self.index = -1
        self.choose.hide()
        self.setDisabled(False)
        self.view = 1
        self.actionAdd_Word.setText("Add Number")
        self.actionAdd_Word.setToolTip("Click to add number")
        self.actionEdit_Word.setText("Edit Number")
        self.actionEdit_Word.setToolTip("Click to edit selected number")
        self.actionRemove_word.setText("Remove Number")
        self.actionRemove_word.setToolTip("Click to remove selected number")
        self.btn_goBack.setText("Switch to Alphabets")
        self.btn_chooseAlpha.setHidden(True)
        #self.itemList.clear()
        self.itemDisp.clear()
        self.nums.clear()
        if self.route is None:
            self.route = self.connect()
        result = self.route.collectNumbers()
        while result.next():
            self.nums.append([result.value('numeral_english'),
                              result.value('numeral_hausa'), result.value('numeral_number')])
            if result.value('numeral_hausa') == self._lastViewedNum:
                self.index = int(result.value(3)) - 2
            #self.itemList.addItem(result.value(2))
        self.label.setText("Numbers: <font color='brown'>daya</font><font size='15px'> zuwa </font>"
                           + "<font color='brown'>" + self.nums[len(self.nums)-1][1] + "</font>")
        """if num is not None:goma sha daya
            self.index = self.nums[]"""
        self.index += 1
        self.setItemInfo(self.index)
        #self.itemList.setFocus()
        self.label.setAlignment(Qt.AlignLeft|Qt.AlignVCenter)
    

    @pyqtSlot(str)
    def alphaToList(self, txt):
        self.index = -1
        self.choose.hide()
        self.setDisabled(False)
        self.view = 0
        self.alphabet = txt
        print('alphabet is ' + self.alphabet)
        self.actionAdd_Word.setText("Add word")
        self.actionAdd_Word.setToolTip("Click to add word")
        self.actionEdit_Word.setText("Edit word")
        self.actionEdit_Word.setToolTip("Click to edit selected word")
        self.actionRemove_word.setText("Remove word")
        self.actionRemove_word.setToolTip("Click to remove selected number")
        self.btn_goBack.setText("Switch to numerals")
        self.btn_chooseAlpha.setHidden(False)
        self.itemDisp.clear()
        self.pixDisp.clear()
        self.label_example.clear()
        self.words.clear()
        self.label.setText("Alphabet: <font color='brown'>" + txt + "</font>")
        if self.route is None:
            self.route = self.connect()
        result = self.route.collectAlpha(txt)
        ind = 0
        while result.next():
            self.words.append([result.value(0), result.value(1), result.value(2), result.value(3), result.value(4)])
            if result.value(0) == self._lastViewedWord:
                self.index = ind - 1
                ind+=1
            ind+=1
            #self.itemList.addItem(result.value(0))
        self.label.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        self.index += 1
        self.setItemInfo(self.index)
        #self.itemList.setFocus()
        

    @pyqtSlot(str)
    def userChanged(self, newUsername):
        self.username = newUsername
        self.actionUser.setText(self.username)

    @pyqtSlot()
    def on_btn_chooseAlpha_clicked(self):
        self.selectLetter(None)

    @pyqtSlot()
    def on_btn_previous_clicked(self):
        listt = None
        if self.view == 0:
            listt = self.words
        elif self.view == 1:
            listt = self.nums
        if 0 < self.index < len(listt):
            self.index -= 1
            self.setItemInfo(self.index)
        #self.itemList.setCurrentRow(self.index)

    @pyqtSlot()
    def on_btn_next_clicked(self):
        listt = None
        if self.view == 0:
            listt = self.words
        elif self.view == 1:
            listt = self.nums
        if -1 <= self.index < len(listt) - 1:
            self.index += 1
            self.setItemInfo(self.index)
        #self.itemList.setCurrentRow(self.index)

    @pyqtSlot()
    def on_btn_goBack_clicked(self):
        if self.view == 0:
            QMessageBox.information(self, qApp.tr("View Changed"), qApp.tr("App view changed to numerals"))
            self.numToList(self._lastViewedNum)
        elif self.view == 1:
            if len(self._lastViewedWord) != 0:
                QMessageBox.information(self, qApp.tr("View change"), qApp.tr("App view changed to alphabets"))
                self.alphaToList(self._lastViewedWord[0].upper())
            else:
                if self.selectLetter():
                    QMessageBox.information(self, qApp.tr("View change"), qApp.tr("App view changed to alphabets"))

    @pyqtSlot()
    def on_actionAdd_new_user_triggered(self):
        window = signup.Signup()
        window.exec_()

    @pyqtSlot()
    def on_actionEdit_triggered(self):
        if self.user_type == 0:
            window = editAdmin.EditAdmin(self.username)
            window.exec_()
        elif self.user_type == 1:
            window = editUser.UserEdit(self.username)
            window.newUser[str].connect(self.userChanged)
            window.setWindowTitle("Edit username")
            window.exec_()

    @pyqtSlot()
    def on_actionRemove_triggered(self):
        clickedButton = QMessageBox.No
        msgbox = QMessageBox()
        if self.user_type == 0:
            clickedButton = msgbox.question(self, qApp.tr("Confirm"),
                                            qApp.tr("Are you sure you want to delete your admin profile?"))
        elif self.user_type == 1:
            clickedButton = msgbox.question(self, qApp.tr("Confirm"),
                                                 qApp.tr("Are you sure you want to delete this user profile?"))
        if clickedButton == QMessageBox.Yes:
            if self.route.delete(self.username):
                print("admin is " + self.username)
                msgbox.information(self, qApp.tr("Success"),
                                         qApp.tr(self.username + " successfully deleted!"))
                self.reset()
                self.userwindow.reset()
                self.userwindow.exec_()
            else:
                msgbox.information(self, 'Failed', self.username + ' failed to remove!\nTry again!')

    @pyqtSlot()
    def on_actionHistory_triggered(self):
        self.history.reverse()
        window = history.History(self.history)
        window.exec_()

    @pyqtSlot()
    def on_actionAdd_Word_triggered(self):
        if self.view == 0:
            window = addWord.AddWord(self.view, self.alphabet)
            if window.exec_():
                QMessageBox.information(self, qApp.tr("Success!"), qApp.tr("Word successfully saved"))
                self.alphaToList(self.alphabet)
            else:
                QMessageBox.information(self, qApp.tr("Failed"), qApp.tr("Addition failed"))
        elif self.view == 1:
            window = addWord.AddWord(self.view)
            if window.exec_():
                QMessageBox.information(self, qApp.tr("Success!"), qApp.tr("Number successfully saved"))
                self.numToList()
            else:
                QMessageBox.information(self, qApp.tr("Failed"), qApp.tr("Addition failed"))

    @pyqtSlot()
    def on_actionEdit_Word_triggered(self):
        #currItem = self.itemList.currentItem()
        #if currItem:
        if self.view == 0:
            window = editWord.EditWord(self.view, self.words[self.index], self.alphabet)
            if window.exec_():
                QMessageBox.information(self, qApp.tr("Success!"), qApp.tr("Word successfully updated"))
                self.alphaToList(self.alphabet)
            else:
                QMessageBox.information(self, qApp.tr("Failed"), qApp.tr("Update cancelled"))
        elif self.view == 1:
            window = editWord.EditWord(self.view, self.nums[self.index])
            if window.exec_():
                QMessageBox.information(self, qApp.tr("Success!"), qApp.tr("Number successfully updated"))
                self.numToList()
            else:
               QMessageBox.information(self, qApp.tr("Failed"), qApp.tr("Update cancelled"))
        else:
            QMessageBox.information(self, qApp.tr("Information"), qApp.tr("Select an item from the list to edit"))

    @pyqtSlot()
    def on_actionRemove_word_triggered(self):
        #currItem = self.itemList.currentItem()
        #if currItem:
        msgbox = QMessageBox()
        if self.view == 0:
            clickedButton = msgbox.question(self, qApp.tr("Remove word?"),
                            qApp.tr("Do you want to remove the entry \"" + self.words[self.index][0] + "\""))
            if clickedButton == QMessageBox.Yes:
                if self.route.deleteWord(self.words[self.index][0]):
                    QMessageBox.information(self, qApp.tr("Success"), qApp.tr("Removal successful"))

                    #   Delete image
                    if os.path.exists(os.getcwd() + "\\resources\\images\\" + self.words[self.index][4]):
                        os.remove(os.getcwd() + self.words[self.index][4])

                    #   Refresh Alphabets
                    self.alphaToList(self.alphabet)
                else:
                    msgbox.information(self, qApp.tr("Failed"), qApp.tr("Remove error. \nTry again"))
        elif self.view == 1:
            clickedButton = msgbox.question(self, qApp.tr("Remove number?"),
                            qApp.tr("Do you want to remove the entry \"" + self.nums[self.index][1] + "\""))
            if clickedButton == QMessageBox.Yes:
                print(self.nums[self.index][1])
                if self.route.deleteNumber(self.nums[self.index][1]):
                    msgbox.information(self, qApp.tr("Success"), qApp.tr("Removal successful"))
                    self.numToList()
                else:
                    msgbox.information(self, qApp.tr("Failed", qApp.tr("Remove error. \nTry again")))
        else:
            msgbox.information(self, qApp.tr("Information"), qApp.tr("Select an item from the list to delete"))

    @pyqtSlot()
    def on_actionLogout_triggered(self):
        if self.user_type == 1:
            self.userwindow.reset()
            if not self.userwindow.exec():
                self.saveHistory()
                self.reset()
                QMessageBox.information(self, qApp.tr("User change successful"),
                                    qApp.tr("User changed to ") + self.username)
                self.showChoosepg()
        elif self.user_type == 0:
            msgbox = QMessageBox()
            clickedButton = msgbox.question(self, qApp.tr("Logout"), qApp.tr("Are you sure you want to logout?"))
            if clickedButton == QMessageBox.Yes:
                self.reset()
                self.actionUser.setText("")
                QMessageBox.information(self, qApp.tr("Success"), qApp.tr("Logout successful"))
                self.userwindow.reset()
                if not self.userwindow.exec_():
                    self.showChoosepg()

    @pyqtSlot()
    def on_actionView_admin_triggered(self):
        window = users.UserView(0, self)
        window.exec_()

    @pyqtSlot()
    def on_actionView_users_triggered(self):
        window = normalUsers.NormalUsers()
        window.exec_()

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
