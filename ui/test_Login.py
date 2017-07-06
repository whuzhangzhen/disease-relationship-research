#coding:utf-8

import sys
import random

from PyQt4 import  QtCore,QtGui
from Login import *



class MyForm(QtGui.QWidget):
    def __init__(self,parent=None):
        QtGui.QWidget.__init__(self,parent)
        #创建Ui_DDAS对象
        self.ui=Ui_DDAS()
        #调用实例方法
        self.ui.setupUi(self)

if __name__ == '__main__':
    app=QtGui.QApplication(sys.argv)
    myapp=MyForm()
    myapp.show()
    sys.exit(app.exec_())


