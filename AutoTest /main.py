from subprocess import Popen

from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

from thread.Worker import Worker
from work.testCase import TestCase


class MyMainGUI(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.qtxt1 = QTextEdit(self)
        self.btn1 = QPushButton("Start", self)
        self.btn2 = QPushButton("Stop", self)
        self.btn3 = QPushButton("add 100", self)
        self.btn4 = QPushButton("send instance", self)
        self.btn5 = QPushButton("run Test Case", self)

        vbox = QVBoxLayout()
        vbox.addWidget(self.qtxt1)
        vbox.addWidget(self.btn1)
        vbox.addWidget(self.btn2)
        vbox.addWidget(self.btn3)
        vbox.addWidget(self.btn4)
        vbox.addWidget(self.btn5)

        self.setLayout(vbox)

        self.setGeometry(100, 50, 300, 300)


class Test:
    def __init__(self):
        name = ""


class MyMain(MyMainGUI):
    add_sec_signal = pyqtSignal()
    send_instance_singal = pyqtSignal("PyQt_PyObject")

    test_signal = pyqtSignal()

    def __init__(self, parent=None):
        super().__init__(parent)

        self.btn1.clicked.connect(self.time_start)
        self.btn2.clicked.connect(self.time_stop)
        self.btn3.clicked.connect(self.add_sec)
        self.btn4.clicked.connect(self.send_instance)

        self.btn5.clicked.connect(self.runTestCase)

        self.th = Worker(parent=self)
        self.th.sec_changed.connect(self.time_update)  # custom signal from worker thread to main thread

        self.add_sec_signal.connect(self.th.add_sec)  # custom signal from main thread to worker thread
        self.send_instance_singal.connect(self.th.recive_instance_singal)

        self.option = ''
        self.testThread = None
        self.out = None

        # self.test_signal.connect(self.testThread.test)

        self.show()

    def runTestCase(self):
        print("Enter runTestCase")
        self.startThread()
        pass

    def startThread(self):
        print("start Thread")
        self.option = "Case1"
        self.testThread = TestCase(self.option)
        self.testThread.testcase_signal.connect(self.stopThread)
        # thread 에 있는 signal 과 함수를 연결시키는 코드
        # testcase_signal 이 emit되는 순간 stopThread 가 call 되어짐

        self.testThread.start()
        self.testThread.working = True

        print("working: ", self.testThread.working)

        pass

    @pyqtSlot(Popen)
    def stopThread(self, output):
        print("enter stopThread")
        self.testThread.working = False
        self.out = output

        print("th output1: ", output)
        print("th output2: ", self.out.communicate())
        print("working2: ", self.testThread.working)

        pass
    # testcase_signal 이 emit 되어지면 call 됨
    # 이때 thread 에서 던진 return 값들도 받아옴


    @pyqtSlot()
    def time_start(self):
        self.th.start()
        self.th.working = True

    @pyqtSlot()
    def time_stop(self):
        self.th.working = False

    @pyqtSlot()
    def add_sec(self):
        print(".... add singal emit....")
        self.add_sec_signal.emit()

    @pyqtSlot(str)
    def time_update(self, msg):
        self.qtxt1.append(msg)

    @pyqtSlot()
    def send_instance(self):
        t1 = Test()
        t1.name = "SuperPower!!!"
        self.send_instance_singal.emit(t1)


if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    form = MyMain()
    app.exec_()
