import sys
from PyQt5.QtSql import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

class Connect(QObject):
    def __init__(self, parent=None):
        super(Connect, self).__init__(parent)

        self.db = QSqlDatabase.addDatabase("QSQLITE")
        self.db.setDatabaseName('hausaProject.db')
        if not self.db.open():
            QMessageBox.critical(self.par, qApp.tr("Cannot open database"),
            qApp.tr("Unable to establish a database connection.\n"
            "This example needs SQLite support. Please read "
            "the Qt SQL driver documentation for information "
            "how to build it.\n\n" "Click Cancel to exit."),
            QMessageBox.Cancel)
            qApp.exit()
        print("connected")

    def queryUser(self, username):
        query = QSqlQuery()
        query.prepare("select * from users where username = ?")
        query.addBindValue(username)

        if query.exec_():
            return query

        print(query.lastError().text())
        return False

    def query_db(self, tbl_name, username=None):
        query = QSqlQuery()
        #query.setForwardOnly(False)
        if username is None:
            if query.exec_("SELECT * FROM " + tbl_name):
                return query
        else:
            query.prepare("select password from " + tbl_name + " where username = ? and user_type = 0;")
            query.addBindValue(username)
            if query.exec_():
                return query
        return False

    def addWord(self, *args):
        query = QSqlQuery()
        query.prepare("insert into words(word_hausa, word_english, hausa_description, english_description, letter_id,"
                      " image_name) values(?,?,?,?,?,?)")

        for item in args:
            query.addBindValue(item)

        if query.exec_():
            return True

        print(query.lastError().text())
        return False

    def collectAlpha(self, alphabet):
        query = QSqlQuery()
        query.prepare("select word_hausa, word_english, hausa_description, english_description, image_name from words "
                      "inner join letters on letters.letter_id = words.letter_id where letter_description = ? ")
        query.addBindValue(alphabet)
        if query.exec_():
            return query
        print(query.lastError().text())

    def updateAlpha(self, *args):
        query = QSqlQuery()
        query.prepare("UPDATE words SET word_hausa = ?, word_english = ?, hausa_description = ?,"
                      " english_description = ?, image_name = ? where word_hausa = ?;")

        for item in args:
            query.addBindValue(item)
        if query.exec_():
            return True

        print(query.lastError().text())
        return False

    def collectNumbers(self):
        query = QSqlQuery()
        query.setForwardOnly(False)
        if query.exec_("SELECT * FROM numerals"):
            return query

    def showUsers(self):
        list_of_usernames = []
        rslt = self.query_db('users')
        while rslt.next():
            list_of_usernames.append(rslt.value(4))
        return list_of_usernames

    def updateUser(self, *args):
        query = QSqlQuery()
        if len(args) == 2:
            query.prepare("UPDATE users SET username = ? where username = ?")
        elif len(args) == 6:
            query.prepare("UPDATE users SET fname = ?,midname = ?,lname = ?,username = ?,password = ? "
                          "WHERE username = ?")
        for item in args:
            query.addBindValue(item)

        if query.exec_():
            return True

        print(query.lastError().text())
        return False

    def insert_db(self, *args):
        query = QSqlQuery()
        if len(args) == 6:
            query.prepare("insert into users(fname,midname,lname,username,password,user_type) values(?,?,?,?,?,?)")
        elif len(args) == 2:
            query.prepare("insert into users(username,user_type) values(?,?)")
        for item in args:
            query.addBindValue(item)

        if query.exec_():
            return query

        print(query.lastError().text())
        return False

    def updateNumerals(self, *args):
        query = QSqlQuery()
        query.prepare("UPDATE numerals SET numeral_english = ?, numeral_hausa = ?  WHERE numeral_hausa = ?;" )
        for item in args:
            query.addBindValue(item)
        if query.exec_():
            return True

        print(query.lastError().text())
        return False

    def addNumerals(self, *args):
        print(len(args))
        query = QSqlQuery()
        query.prepare("INSERT INTO numerals(numeral_number, numeral_english, numeral_hausa)"
                      "VALUES(?, ?, ?)")
        for item in args:
            query.addBindValue(item)
        if query.exec_():
            return True

        print(query.lastError().text())
        return False

    def open_db(self):
        self.db.open()

    def close_db(self):
        self.db.close()
        print("DB closed")

    def delete(self, *args):
        query = QSqlQuery()
        query.prepare("DELETE FROM users WHERE username = ?")
        query.addBindValue(args[0])

        if query.exec_():
            return True
        else:
            return False

    def deleteWord(self, word):
        query = QSqlQuery()
        query.prepare("DELETE FROM words WHERE word_hausa = ?;")
        query.addBindValue(word)
        if query.exec_():
            return True

        print(query.lastError().text())
        return False

    def deleteNumber(self, number):
        query = QSqlQuery()
        query.prepare("DELETE FROM numerals WHERE numeral_hausa = ?;")
        query.addBindValue(number)

        if query.exec_():
            return True

        print(query.lastError().text())
        return False

    def queryUsers(self, type):
        query = QSqlQuery()
        query.prepare("SELECT * FROM users WHERE user_type = ?;")
        query.addBindValue(type)

        if query.exec_():
            return query

        print(query.lastError().text())
        return False

    def saveLastItemViewed(self, user, num=None, word=None):
        query = QSqlQuery()
        if num is None:
            query.prepare("UPDATE users SET lastViewedWord = ? WHERE username = ?")
            query.addBindValue(word)
            query.addBindValue(user)
        elif word is None:
            query.prepare("UPDATE users SET lastViewedNumber = ? WHERE username = ?")
            query.addBindValue(num)
            query.addBindValue(user)
        elif num is not None and word is not None:
            query.prepare("UPDATE users SET lastViewedWord = ?, lastViewedNumber = ? WHERE username = ?")
            query.addBindValue(word)
            query.addBindValue(num)
            query.addBindValue(user)

        if query.exec_():
            return True

        print(query.lastError().text())
        return False

    def getHistory(self, username):
        query = QSqlQuery()

        query.prepare("SELECT entry, entry_type, view_date FROM history WHERE username = ? "
                      "ORDER BY entry ASC, entry_type;")
        query.addBindValue(username)

        if query.exec_():
            return query
                #return query.size()

        print(query.lastError().text())
        return False

    def checkHistory(self, username):
        query = QSqlQuery()
        query.prepare("SELECT entry FROM history WHERE username = ?")
        query.addBindValue(username)

        if query.exec_():
            return query

        print(query.lastError().text())
        return False

    def saveHistory(self, listOfEntries, username, mode):
        query = QSqlQuery()
        if mode == 0:
            query.prepare("INSERT INTO history(entry, entry_type, username, view_date) VALUES(?,?,?,?)")
            for item in listOfEntries:
                query.addBindValue(item[0])
                query.addBindValue(item[1])
                query.addBindValue(username)
                query.addBindValue(item[2])
                if query.exec_():
                    print(True)
                else:
                    print(False)
        elif mode == 1:
            query.prepare("UPDATE history SET viewdate = ? where username=? and entry=?")
            for item in listOfEntries:
                query.addBindValue(item[2])
                query.addBindValue(username)
                query.addBindValue(item[0])
                if query.exec_():
                    print(True)
                else:
                    print(False)


def main():
    app = QCoreApplication(sys.argv)
    obj = Connect()
    print(obj.getHistory('spoon',4))
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()