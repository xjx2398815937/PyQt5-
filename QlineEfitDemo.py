
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import Qt

import sys

class QlinEditDemo(QWidget):
    def __init__(self):
        super(QlinEditDemo,self).__init__()
        self.initUi()
    def initUi(self):
        edit1 = QLineEdit()
        # 使用校验器
        edit1.setValidator(QIntValidator())
        # 不超过9999
        edit1.setMaxLength(4)
        edit1.setAlignment(Qt.AlignRight)
        edit1.setFont(QFont("Arial", 20))

        edit2 = QLineEdit()
        edit2.setValidator(QDoubleValidator(0.99,99.99,2))

        edit3 = QLineEdit()
        edit3.setInputMask('99_999_999999;#')

        edit4 = QLineEdit()
        edit4.textChanged.connect(self.textChange)

        edit5 = QLineEdit()
        edit5.setEchoMode(QLineEdit.Password)
        edit5.editingFinished.connect(self.enterPress)

        edit6 = QLineEdit("Hello PyQt5")
        edit6.setReadOnly(True)

        formLayout = QFormLayout()
        formLayout.addRow("整数校验",edit1)
        formLayout.addRow("浮点数校验", edit2)
        formLayout.addRow("掩码校验", edit3)
        formLayout.addRow("文本变化", edit4)
        formLayout.addRow("密码", edit5)
        formLayout.addRow("只读", edit6)

        self.setLayout(formLayout)
        self.setWindowTitle("QlineEdit综合案例")

        # 文本变化触发事件
    def textChange(self,text):
        print("输入内容" + text)
    def enterPress(self):
        print("已输入值")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = QlinEditDemo()
    main.show()
    sys.exit(app.exec_())

