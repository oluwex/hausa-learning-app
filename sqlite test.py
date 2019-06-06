import sys
from PyQt5.QtSql import *
from PyQt5.QtCore import *

class DBConnect():

    def __init__(self):
        db = QSqlDatabase.addDatabase("QSQLITE")
        db.setDatabaseName('hausaProject.db')
        if not db.open():
            print("Not open")
            sys.exit()
        print("DB opened!!!")
        print(db.tables())


    def createTableLetters(self):
        query = QSqlQuery()
        qry = "CREATE TABLE letters(letter_id INTEGER PRIMARY KEY AUTOINCREMENT," \
              "letter_description VARCHAR(50) NOT NULL);"
        if query.exec_(qry):
            print("Table letters created successfully")
            return True
        print("Unsuccessful")
        return False


    def createTableNumerals(self):
        query = QSqlQuery()
        qry = "CREATE TABLE numerals(numeral_id INTEGER PRIMARY KEY AUTOINCREMENT," \
              "numeral_english VARCHAR(100) NOT NULL, numeral_hausa VARCHAR(200) NOT NULL);"
        if query.exec_(qry):
            print("Table NUMERALS created successfully")
            return True
        print("Unsuccessful")
        return False


    def createTableWords(self):
        query = QSqlQuery()
        qry = "CREATE TABLE words(word_id INTEGER PRIMARY KEY AUTOINCREMENT, letter_id INTEGER," \
              "word_english VARCHAR(50) NOT NULL, word_hausa VARCHAR(50) NOT NULL, " \
              "word_description VARCHAR(300),image_name VARCHAR(20) DEFAULT ':/images/images/blank.png', " \
              "FOREIGN KEY(letter_id) REFERENCES letters(letter_id));"
        if query.exec_(qry):
            print("Table words created successfully")
            return True
        print("Unsuccessful")
        return False


    def insertIntoLetters(self):
        query = QSqlQuery()
        query.prepare("insert into letters(letter_description) values(?);")
        """r = [[QVariant('A')],[QVariant('B')],[QVariant('C')],[QVariant('D')],
             [QVariant('E')],[QVariant('F')],[QVariant('G')],[QVariant('H')],[QVariant('I')],[QVariant('J')]
                 ,[QVariant('K')],[QVariant('L')],[QVariant('M')],[QVariant('N')],[QVariant('O')]
                 ,[QVariant('R')],[QVariant('S')],[QVariant('T')],[QVariant('U')],[QVariant('W')]
                ,[QVariant('Y')],[QVariant('Z')]]"""
        r = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','R'
            ,'S','T','U','W','Y','Z']
        """for item in r:
            print(item)
            query.addBindValue(QVariant(item))"""
        for item in r:
            query.addBindValue(item)
            if query.exec_():
                print("Successful")
            else:
                print("Failed", query.lastError().text())

    def insertIntoNumerals(self):
        query = QSqlQuery()
        query.prepare("insert into numerals(numeral_english, numeral_hausa) values(?, ?);")
        r = [['one', 'daya'],['two', 'biyu'],['three', 'uku'],['four', 'hudu'],['five', 'biyar'],['six', 'shidda'],
             ['seven', 'bakai'],['eight', 'takwas'],['nine', 'tara'],['ten', 'goma']]
        for item in r:
            query.addBindValue(item[0])
            query.addBindValue(item[1])
            if query.exec_():
                print("Successful")
            else:
                print("Failed", query.lastError().text())


    def retrieve(self):
        query = QSqlQuery()
        if query.exec_("select * from letters"):
            while query.next():
                print(query.value(0), query.value(1))
        else:
            print("Failed")


def main():
    app = QCoreApplication(sys.argv)
    obj = DBConnect()
    #obj.retrieve()
    #obj.createTableNumerals()
    #obj.insertIntoLetters()
    #obj.insertIntoNumerals()
    obj.createTableWords()
    app.exec_()

if __name__ == '__main__':
    main()