import os
from PyQt5.uic import compileUiDir

try:
    compileUiDir(os.getcwd()+'\\ui_files')
    #compileUiDir(os.getcwd()+'\\resources')
except Exception as err:
    print(err)