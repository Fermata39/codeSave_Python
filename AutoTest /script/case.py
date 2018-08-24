import subprocess


class TestScript:

    def __init__(self):
        self.out = ''
        pass

    def start_vowifi(self):
        print("vowifi start")
        self.out = subprocess.Popen("ls", shell=True, stdout=subprocess.PIPE)
        print("out: ", self.out)

        return self.out