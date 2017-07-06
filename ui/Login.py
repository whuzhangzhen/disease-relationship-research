# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Login.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
from Common_disease import graph
from Symptom import symptom
from distribution import chaxun
from pymongo import *

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_DDAS(object):
    def setupUi(self, DDAS):
        DDAS.setObjectName(_fromUtf8("DDAS"))
        DDAS.resize(1150, 650)
        DDAS.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 255);"))


        '''分布界面
        '''
        #layout = QtGui.QVBoxLayout()
        self.Distribution = QtGui.QWidget(DDAS)
        self.Distribution.setGeometry(QtCore.QRect(0, 0, 1150, 650))
        self.Distribution.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 255);"))
        self.Distribution.setObjectName(_fromUtf8("Distribution"))

        #标题
        self.title4 = QtGui.QLabel(self.Distribution)
        self.title4.setGeometry(QtCore.QRect(0, 0, 1150, 95))
        self.title4.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.title4.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);\n"
"font: 75 29pt \"微软雅黑\";\n"
"background-color: rgb(3, 146, 255)\n"
"\n"
""))
        self.title4.setObjectName(_fromUtf8("title4"))
        # 搜索按钮
        self.searchButton = QtGui.QPushButton(self.Distribution)
        self.searchButton.setGeometry(QtCore.QRect(1000, 110, 70, 30))
        self.searchButton.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);\n"
                                                  "font: 11pt \"微软雅黑\";\n"
                                                  "background-color: rgb(3, 146, 255);"))
        self.searchButton.setObjectName(_fromUtf8("searchButton"))
        self.searchButton.connect(self.searchButton, QtCore.SIGNAL('clicked()'),
                     self.showgraph1)
        # 搜索框
        self.searchText = QtGui.QLineEdit(self.Distribution)
        self.searchText.setGeometry(QtCore.QRect(800, 110, 180, 30))
        self.searchText.setStyleSheet(_fromUtf8("font: 11pt \"微软雅黑\";"))
        self.searchText.setObjectName(_fromUtf8("searchText"))
        #年龄标签
        self.ageLabel = QtGui.QLabel(self.Distribution)
        self.ageLabel.setGeometry(QtCore.QRect(650, 160, 30, 30))
        self.ageLabel.setStyleSheet(_fromUtf8("font: 80 10pt \"微软雅黑\";\n"
                                              "color: rgb(0, 0, 0);"))
        self.ageLabel.setObjectName(_fromUtf8("ageLabel"))
        # 年龄分布起始年龄输入
        self.ageEdit = QtGui.QLineEdit(self.Distribution)
        self.ageEdit.setGeometry(QtCore.QRect(680, 160, 30, 30))
        self.ageEdit.setStyleSheet(_fromUtf8("font: 9pt \"微软雅黑\";"))
        self.ageEdit.setObjectName(_fromUtf8("ageEdit"))
        # 年龄之间的横杠
        self.aLabel = QtGui.QLabel(self.Distribution)
        self.aLabel.setGeometry(QtCore.QRect(710, 160, 10, 30))
        self.aLabel.setStyleSheet(_fromUtf8("color: rgb(0, 0, 0);\n"
                                            "background-color: rgb(255, 255, 255);\n"
                                            "font: 9pt \"微软雅黑\";"))
        self.aLabel.setObjectName(_fromUtf8("aLabel"))
        # 终止年龄
        self.ageEdit2 = QtGui.QLineEdit(self.Distribution)
        self.ageEdit2.setGeometry(QtCore.QRect(720, 160, 30, 30))
        self.ageEdit2.setStyleSheet(_fromUtf8("font: 9pt \"微软雅黑\";"))
        self.ageEdit2.setObjectName(_fromUtf8("ageEdit2"))
        #性别标签
        self.sexLabel = QtGui.QLabel(self.Distribution)
        self.sexLabel.setGeometry(QtCore.QRect(800, 160, 30, 30))
        self.sexLabel.setStyleSheet(_fromUtf8("font: 80 10pt \"微软雅黑\";\n"
                                              "color: rgb(0, 0, 0);"))
        self.sexLabel.setObjectName(_fromUtf8("sexLabel"))
        #性别分布按钮 male、female、all
        self.maleButton = QtGui.QRadioButton(self.Distribution)
        self.maleButton.setGeometry(QtCore.QRect(830, 160, 65, 30))
        self.maleButton.setStyleSheet(_fromUtf8("font: 10pt \"微软雅黑\";"))
        self.maleButton.setObjectName(_fromUtf8("maleButton"))
        self.femaleButton = QtGui.QRadioButton(self.Distribution)
        self.femaleButton.setGeometry(QtCore.QRect(890, 160, 70, 30))
        self.femaleButton.setStyleSheet(_fromUtf8("font: 10pt \"微软雅黑\";"))
        self.femaleButton.setObjectName(_fromUtf8("femaleButton"))
        self.allButton = QtGui.QRadioButton(self.Distribution)
        self.allButton.setGeometry(QtCore.QRect(970, 160, 60, 30))
        self.allButton.setStyleSheet(_fromUtf8("font: 10pt \"微软雅黑\";"))
        self.allButton.setObjectName(_fromUtf8("allButton"))
        # 交叉查询按钮
        self.goButton = QtGui.QPushButton(self.Distribution)
        self.goButton.setGeometry(QtCore.QRect(1050, 160, 30, 30))
        self.goButton.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);\n"
                                              "font: 11pt \"微软雅黑\";\n"
                                              "background-color: rgb(3, 146, 255);"))
        self.goButton.setObjectName(_fromUtf8("goButton"))
        self.goButton.connect(self.goButton, QtCore.SIGNAL('clicked()'),
                                  self.showgraph2)


        # 共病显示框
        self.QLabel = QtGui.QLabel(self.Distribution)
        self.QLabel.setGeometry(QtCore.QRect(20, 190, 330, 330))
        self.QLabel.setObjectName(_fromUtf8("graphicsView2"))
        #症状显示框
        self.QLabel2 = QtGui.QLabel(self.Distribution)
        self.QLabel2.setGeometry(QtCore.QRect(350, 190, 330, 330))
        self.QLabel2.setObjectName(_fromUtf8("graphicsView2"))
        # 年龄性别分布显示框
        self.QLabel3 = QtGui.QLabel(self.Distribution)
        self.QLabel3.setGeometry(QtCore.QRect(680, 190, 400,330))
        self.QLabel3.setObjectName(_fromUtf8("graphicsView3"))

        #welcome
        self.welcomeLabel2 = QtGui.QLabel(self.Distribution)
        self.welcomeLabel2.setGeometry(QtCore.QRect(950, 40, 80, 30))
        self.welcomeLabel2.setStyleSheet(_fromUtf8("font: 12pt \"微软雅黑\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(3, 146, 255);"))
        self.welcomeLabel2.setObjectName(_fromUtf8("welcomeLabel2"))
        #返回
        self.backButton2 = QtGui.QPushButton(self.Distribution)
        self.backButton2.setGeometry(QtCore.QRect(950, 580, 80, 30))
        self.backButton2.setStyleSheet(_fromUtf8("font: 11pt \"微软雅黑\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(3, 146, 255);"))
        self.backButton2.setObjectName(_fromUtf8("backButton2"))

#----------------------------------------------------------------

        '''疾病界面
        '''
        self.Disease = QtGui.QFrame(self.Distribution)
        self.Disease.setGeometry(QtCore.QRect(0, 0, 1150, 650))
        self.Disease.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 255);"))
        self.Disease.setObjectName(_fromUtf8("Disease"))
        #标题
        self.title3 = QtGui.QLabel(self.Disease)
        self.title3.setGeometry(QtCore.QRect(0, 0, 1150, 95))
        self.title3.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.title3.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);\n"
"font: 75 29pt \"微软雅黑\";\n"
"background-color: rgb(3, 146, 255)\n"
"\n"
""))
        self.title3.setObjectName(_fromUtf8("title3"))
        # instruction
        self.instruction = QtGui.QLabel(self.Disease)
        self.instruction.setGeometry(QtCore.QRect(250, 100, 850, 450))
        self.instruction.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.instruction.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);\n"
                                            "font: 75 11pt \"微软雅黑\";\n"
                                            "background-color: rgb(255, 255, 255)\n"
                                            "\n"
                                            ""))
        png = QtGui.QPixmap('instruction.png')
        self.instruction.setPixmap(png)

        #Go
        self.dButton1 = QtGui.QPushButton(self.Disease)
        self.dButton1.setGeometry(QtCore.QRect(800, 580, 80, 30))
        self.dButton1.setStyleSheet(_fromUtf8("background-color: rgb(3, 146, 255);\n"
"font: 11pt \"微软雅黑\";\n"
"color: rgb(255, 255, 255);"))
        self.dButton1.setObjectName(_fromUtf8("dButton1"))


        #welcome
        self.welcomeLabel1 = QtGui.QLabel(self.Disease)
        self.welcomeLabel1.setGeometry(QtCore.QRect(950, 40, 80, 30))
        self.welcomeLabel1.setStyleSheet(_fromUtf8("font: 12pt \"微软雅黑\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(3, 146, 255);"))
        self.welcomeLabel1.setObjectName(_fromUtf8("welcomeLabel1"))
        #返回按钮
        self.backButton1 = QtGui.QPushButton(self.Disease)
        self.backButton1.setGeometry(QtCore.QRect(950, 580, 80, 30))
        self.backButton1.setStyleSheet(_fromUtf8("background-color: rgb(3, 146, 255);\n"
"font: 11pt \"微软雅黑\";\n"
"color: rgb(255, 255, 255);"))
        self.backButton1.setObjectName(_fromUtf8("backButton1"))
#-----------------------------------------------------------------
        '''注册界面
        '''
        self.Register = QtGui.QWidget(self.Disease)
        self.Register.setEnabled(True)
        self.Register.setGeometry(QtCore.QRect(0, 0, 1150, 650))
        self.Register.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 255);"))
        self.Register.setObjectName(_fromUtf8("Register"))
        #标题
        self.title2 = QtGui.QLabel(self.Register)
        self.title2.setGeometry(QtCore.QRect(0, 0, 1150, 95))
        self.title2.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.title2.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);\n"
"font: 75 28pt \"微软雅黑\";\n"
"background-color: rgb(3, 146, 255)\n"
"\n"
""))
        self.title2.setObjectName(_fromUtf8("title2"))
        #用户名
        self.usernameLabel2 = QtGui.QLabel(self.Register)
        self.usernameLabel2.setGeometry(QtCore.QRect(290, 200, 101, 31))
        self.usernameLabel2.setStyleSheet(_fromUtf8("font: 75 12pt \"微软雅黑\";\n"
"color: rgb(3, 146, 255);"))
        self.usernameLabel2.setObjectName(_fromUtf8("usernameLabel2"))
        #密码
        self.passwordLabel2 = QtGui.QLabel(self.Register)
        self.passwordLabel2.setGeometry(QtCore.QRect(300, 270, 91, 31))
        self.passwordLabel2.setStyleSheet(_fromUtf8("font: 75 12pt \"微软雅黑\";\n"
"color: rgb(3, 146, 255);"))
        self.passwordLabel2.setObjectName(_fromUtf8("passwordLabel2"))
        #确认密码
        self.repasswordLabel = QtGui.QLabel(self.Register)
        self.repasswordLabel.setGeometry(QtCore.QRect(230, 340, 161, 31))
        self.repasswordLabel.setStyleSheet(_fromUtf8("font: 75 12pt \"微软雅黑\";\n"
                                                     "color: rgb(3, 146, 255);"))
        self.repasswordLabel.setObjectName(_fromUtf8("repasswordLabel"))
        #创建按钮
        self.creatButton = QtGui.QPushButton(self.Register)
        self.creatButton.setGeometry(QtCore.QRect(340, 420, 221, 31))
        self.creatButton.setStyleSheet(_fromUtf8("background-color: rgb(3, 146, 255);\n"
"font: 75 12pt \"微软雅黑\";\n"
"color: rgb(255, 255, 255);\n"
""))
        self.creatButton.setObjectName(_fromUtf8("creatButton"))
        #已有账户提示
        self.label = QtGui.QLabel(self.Register)
        self.label.setGeometry(QtCore.QRect(580, 40, 201, 21))
        self.label.setStyleSheet(_fromUtf8("background-color: rgb(3, 146, 255);\n"
"font: 11pt \"微软雅黑\";\n"
"color: rgb(255, 255, 255);"))

        #登录按钮
        self.loginButton2 = QtGui.QPushButton(self.Register)
        self.loginButton2.setGeometry(QtCore.QRect(770, 40, 61, 23))
        self.loginButton2.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);\n"
"font: 11pt \"微软雅黑\";\n"
"background-color: rgb(3, 146, 255);"))
        self.loginButton2.setObjectName(_fromUtf8("loginButton2"))

        #用户名输入框
        self.nameText = QtGui.QLineEdit(self.Register)
        self.nameText.setGeometry(QtCore.QRect(410, 200, 221, 31))
        self.nameText.setStyleSheet(_fromUtf8("font: 11pt \"微软雅黑\";"))
        self.nameText.setObjectName(_fromUtf8("nameText"))
        #密码输入
        self.passwordEdit2 = QtGui.QLineEdit(self.Register)
        self.passwordEdit2.setGeometry(QtCore.QRect(410, 270, 221, 31))
        self.passwordEdit2.setStyleSheet(_fromUtf8("font: 11pt \"微软雅黑\";"))
        self.passwordEdit2.setEchoMode(QtGui.QLineEdit.Password)
        self.passwordEdit2.setObjectName(_fromUtf8("passwordEdit2"))
        #密码确认
        self.repasswordEdit = QtGui.QLineEdit(self.Register)
        self.repasswordEdit.setGeometry(QtCore.QRect(410, 340, 221, 31))
        self.repasswordEdit.setStyleSheet(_fromUtf8("font: 11pt \"微软雅黑\";"))
        self.repasswordEdit.setEchoMode(QtGui.QLineEdit.Password)
        self.repasswordEdit.setObjectName(_fromUtf8("repasswordEdit"))
#-----------------------------------------------------------------
        '''登录界面

        '''
        self.Login = QtGui.QFrame(self.Register)
        self.Login.setGeometry(QtCore.QRect(0, 0, 1150, 650))
        self.Login.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 255);"))
        self.Login.setFrameShape(QtGui.QFrame.StyledPanel)
        self.Login.setFrameShadow(QtGui.QFrame.Raised)
        self.Login.setObjectName(_fromUtf8("Login"))
        #标题
        self.title1 = QtGui.QLabel(self.Login)
        self.title1.setGeometry(QtCore.QRect(0, 0, 1150, 95))
        self.title1.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.title1.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);\n"
"font: 75 29pt \"微软雅黑\";\n"
"background-color: rgb(3, 146, 255)\n"
"\n"
""))
        self.title1.setObjectName(_fromUtf8("title1"))
        #系统名
        self.nameLabel = QtGui.QLabel(self.Login)
        self.nameLabel.setGeometry(QtCore.QRect(280, 160, 750, 95))
        self.nameLabel.setStyleSheet(_fromUtf8("color: rgb(0, 0, 0);\n"
"font: 75 25pt \"微软雅黑\";"))
        self.nameLabel.setObjectName(_fromUtf8("nameLabel"))
        #用户名
        self.usernameLabel = QtGui.QLabel(self.Login)
        self.usernameLabel.setGeometry(QtCore.QRect(380, 300, 130, 30))
        self.usernameLabel.setStyleSheet(_fromUtf8("font: 75 13pt \"微软雅黑\";\n"
"color: rgb(3, 146, 255);"))
        self.usernameLabel.setObjectName(_fromUtf8("usernameLabel"))
        # 用户名输入
        self.usernameText = QtGui.QLineEdit(self.Login)
        self.usernameText.setGeometry(QtCore.QRect(500, 300, 250, 35))
        self.usernameText.setStyleSheet(_fromUtf8("font: 13pt \"微软雅黑\";"))
        self.usernameText.setObjectName(_fromUtf8("usernameText"))
        self.usernameText.setText('admin')
        #密码
        self.passwordLabel = QtGui.QLabel(self.Login)
        self.passwordLabel.setGeometry(QtCore.QRect(380, 370, 130, 30))
        self.passwordLabel.setStyleSheet(_fromUtf8("font: 75 13pt \"微软雅黑\";\n"
"color: rgb(3, 146, 255);"))
        self.passwordLabel.setObjectName(_fromUtf8("passwordLabel"))
        # 密码输入
        self.passwordEdit1 = QtGui.QLineEdit(self.Login)
        self.passwordEdit1.setGeometry(QtCore.QRect(500, 370, 250, 35))
        self.passwordEdit1.setStyleSheet(_fromUtf8("font: 13pt \"微软雅黑\";"))
        self.passwordEdit1.setEchoMode(QtGui.QLineEdit.Password)
        self.passwordEdit1.setObjectName(_fromUtf8("passwordEdit1"))
        self.passwordEdit1.setText('admin')

        #登录按钮
        self.loginButton = QtGui.QPushButton(self.Login)
        self.loginButton.setGeometry(QtCore.QRect(530, 450, 150, 35))
        self.loginButton.setStyleSheet(_fromUtf8("background-color: rgb(3, 146, 255);\n"
"font: 75 13pt \"微软雅黑\";\n"
"color: rgb(255, 255, 255);\n"
""))
        self.loginButton.setObjectName(_fromUtf8("loginButton"))
        #绑定监听器
       #self.loginButton.clicked.connect(self.login())




        self.usernameLabel2.raise_()
        self.title2.raise_()
        self.repasswordLabel.raise_()
        self.passwordLabel2.raise_()
        self.label.raise_()
        self.creatButton.raise_()
        self.loginButton2.raise_()
        self.nameText.raise_()
        self.passwordEdit2.raise_()
        self.repasswordEdit.raise_()
        self.Login.raise_()
        self.title4.raise_()
        self.maleButton.raise_()
        self.femaleButton.raise_()
        self.allButton.raise_()
        self.QLabel.raise_()
        self.welcomeLabel2.raise_()
        self.backButton2.raise_()
        self.searchButton.raise_()
        self.goButton.raise_()
        self.ageEdit.raise_()
        self.ageEdit2.raise_()
        self.searchText.raise_()
        self.aLabel.raise_()
        self.QLabel.raise_()
        self.QLabel2.raise_()
        self.QLabel2.raise_()
        self.ageLabel.raise_()
        self.sexLabel.raise_()
        self.Disease.raise_()
        self.usernameText.raise_()
        self.passwordEdit1.raise_()
        #self.instruction.raise_()



        self.retranslateUi(DDAS)

        #点击注册界面的登录按钮返回登录界面
        QtCore.QObject.connect(self.loginButton2, QtCore.SIGNAL(_fromUtf8("clicked()")), self.Login.show)
        #点击创建按钮返回登录界面
        QtCore.QObject.connect(self.creatButton, QtCore.SIGNAL(_fromUtf8("clicked()")), self.Login.show)
        # 点击登录进入疾病页
        QtCore.QObject.connect(self.loginButton, QtCore.SIGNAL(_fromUtf8("clicked()")), self.Register.hide)
        #点击疾病进入分布界面
        QtCore.QObject.connect(self.dButton1, QtCore.SIGNAL(_fromUtf8("clicked()")), self.Disease.hide)
        #点击分布界面返回按钮返回疾病页
        QtCore.QObject.connect(self.backButton2, QtCore.SIGNAL(_fromUtf8("clicked()")), self.Disease.show)
        #点击疾病页返回按钮返回登录页
        QtCore.QObject.connect(self.backButton1, QtCore.SIGNAL(_fromUtf8("clicked()")), self.Register.show)
        QtCore.QObject.connect(self.backButton1, QtCore.SIGNAL(_fromUtf8("clicked()")), self.Login.show)
        QtCore.QMetaObject.connectSlotsByName(DDAS)

    def retranslateUi(self, DDAS):
        DDAS.setWindowTitle(_translate("DDAS", "DDAS - Disease Distribution Analysis System ", None))
        self.title4.setText(_translate("DDAS", "  DDAS - Disease Distribution", None))
        self.maleButton.setText(_translate("DDAS", "male", None))
        self.femaleButton.setText(_translate("DDAS", "female", None))
        self.allButton.setText(_translate("DDAS", "all", None))
        self.welcomeLabel2.setText(_translate("DDAS", "Welcome!", None))
        self.backButton2.setText(_translate("DDAS", "Back", None))
        self.title3.setText(_translate("DDAS", "  DDAS - Disease", None))
        self.dButton1.setText(_translate("DDAS", "Go", None))
        self.welcomeLabel1.setText(_translate("DDAS", "Welcome!", None))
        self.backButton1.setText(_translate("DDAS", "Back", None))
        self.title2.setText(_translate("DDAS", "  DDAS-Register", None))
        self.usernameLabel2.setText(_translate("DDAS", "Your Name :", None))
        self.passwordLabel2.setText(_translate("DDAS", "Password :", None))
        self.creatButton.setText(_translate("DDAS", "Creat Your Account", None))
        self.label.setText(_translate("DDAS", "Already have an account ?", None))
        self.repasswordLabel.setText(_translate("DDAS", "Re-enter Password :", None))
        self.loginButton2.setText(_translate("DDAS", "Login", None))
        self.title1.setText(_translate("DDAS", "  DDAS-Login", None))
        self.nameLabel.setText(_translate("DDAS", "Disease  Distribution  Analysis  System", None))
        self.usernameLabel.setText(_translate("DDAS", "User Name :", None))
        self.passwordLabel.setText(_translate("DDAS", "Password :", None))
        self.loginButton.setText(_translate("DDAS", "Login", None))
        self.searchButton.setText(_translate("DDAS", "Search", None))
        self.goButton.setText(_translate("DDAS", "Go!", None))
        self.aLabel.setText(_translate("DDAS", "—", None))
        self.ageLabel.setText(_translate("DDAS", "Age：", None))
        self.sexLabel.setText(_translate("DDAS", "Sex：", None))



    def register(self):
        pass



    '''def login(self):

        #连接数据库
        #用户登陆

        client = MongoClient()
        db = client.patientinfo_db
        collections = db.usr
        name=self.usernameText.text()
        password=self.passwordEdit1.text()
        result=collections.find({'name':str(name)})['password']
        if password==result:
            # 点击注册显示注册界面
            QtCore.QObject.connect(self.registerButton, QtCore.SIGNAL(_fromUtf8("clicked()")), self.Login.hide)
        else:

            QtGui.QMessageBox.critical(self, 'Error', 'User name or password error')
    '''

    def showgraph1(self):
        #响应搜索界面
        name=self.searchText.text()
        print name
        graph.common_disease(name)

        png1 = QtGui.QPixmap('disease.png')
        # 在label里面，调用setPixmap命令，建立一个图像存放框，并将之前的图像png存放在这个框框里。
        png2 = QtGui.QPixmap('symptom.png')
        self.QLabel.setPixmap(png1)
        self.QLabel2.setPixmap(png2)

    def showgraph2(self):
        #响应分布界面
        name = self.searchText.text()
        print name
        age1=self.ageEdit.text()
        print age1
        age2=self.ageEdit2.text()
        print age2
        sex=''
        if self.femaleButton.isChecked():
                sex='F'
                chaxun.distribution(name, sex, age1, age2)
        elif self.maleButton.isChecked():
                sex='M'
                chaxun.distribution(name, sex, age1, age2)
        print sex
        png = QtGui.QPixmap('distribution.png')
        # 在l1里面，调用setPixmap命令，建立一个图像存放框，并将之前的图像png存放在这个框框里。
        self.QLabel3.setPixmap(png)