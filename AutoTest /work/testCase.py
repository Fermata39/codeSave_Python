import subprocess

from PyQt5.QtCore import QThread, pyqtSlot, pyqtSignal

from script.case import TestScript


class TestCase(QThread):
    testcase_signal = pyqtSignal(subprocess.Popen)

    def __init__(self, option):
        QThread.__init__(self)

        self.working = False
        self.option = option
        self.testcase = TestScript()
        self.output = None

        pass

    def run(self):
        print("enter run")

        while self.working == True:

            if (self.option == "Case1"):
                print("enter case1")
                self.output = self.testcase.start_vowifi()
                print("output: ", self.output)


                if(self.output != None):
                    print("stop thread")
                    self.testcase_signal.emit(self.output)
                    # self.sec_changed.emit('time (secs)：{}'.format(self.sec))
                pass
