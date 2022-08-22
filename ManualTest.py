from math import *
import test
import config
import subprocess

class ManualTest:

    def getandmanual(self, i, a = 0, b=0, c=0):
        if b in config.list_two:
            self.calc_manual("test"+str(i), b, int(a), int(c))
        elif b in config.list_bitwise:
            self.calc_manual("test"+str(i), b, int(a), int(c))
        elif b in config.headtail:
            self.calc_manual("test"+str(i), b, int(a), int(c))
        else:
            print("invalid operator")

if __name__=="__main__":
    t = test.runtests()
    subprocess.call(["mkdir", "testcases/"+str(t.ts)+"/manual"])
    manualsize = int(input("number of manual tests: ")) or 0
    for i in range(manualsize):
        inp = input()
        ManualTest.getandmanual(t, i, *inp.split())
    print("====================")
    t.printresult()