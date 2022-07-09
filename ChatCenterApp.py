from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.QtCore import *
import sys
from ChatCenterUI import *

class ChatCentre(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui =Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.pushButton.clicked.connect(self.bill)
        self.ui.pushButton_2.clicked.connect(self.reset)
        self.ui.pushButton_3.clicked.connect(self.exit)
    def exit(self):
        sys.exit()
    def reset(self):
        self.ui.label_14.clear()
        self.ui.label_15.clear()
        self.ui.label_17.clear()
        self.ui.label_19.clear()

        self.ui.lineEdit.setText('0')
        self.ui.lineEdit_2.setText('0')
        self.ui.lineEdit_3.setText('0')
        self.ui.lineEdit_4.setText('0')
        self.ui.lineEdit_5.setText('0')
        self.ui.lineEdit_6.setText('0')
        self.ui.lineEdit_7.setText('0')
        self.ui.lineEdit_8.setText('0')
        self.ui.lineEdit_9.setText('0')
        self.ui.lineEdit_10.setText('0')
        
    def bill(self):
        pp = 20*int(self.ui.lineEdit.text())
        mp = 20*int(self.ui.lineEdit_2.text())
        gm = 40*int(self.ui.lineEdit_3.text())
        sc = 35*int(self.ui.lineEdit_4.text())
        ct = 20*int(self.ui.lineEdit_5.text())
        pc = 35*int(self.ui.lineEdit_6.text())
        bp = 30*int(self.ui.lineEdit_7.text())
        sp = 20*int(self.ui.lineEdit_8.text())
        dp = 20*int(self.ui.lineEdit_9.text())
        cd = 20*int(self.ui.lineEdit_10.text())

        bill = pp+mp+gm+sc+ct+pc+bp+sp+dp+cd
        sgst = bill * 0.045
        cgst = bill * 0.045
        totbill = bill + sgst + cgst

        self.ui.label_14.setText("{}".format(bill))
        self.ui.label_15.setText("{:.2f}".format(sgst))
        self.ui.label_17.setText("{:.2f}".format(cgst))
        self.ui.label_19.setText("{:.2f}".format(totbill))


if __name__=="__main__":
    app = QApplication(sys.argv)
    w = ChatCentre()
    w.show()
    sys.exit(app.exec_())
