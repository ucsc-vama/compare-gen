from math import *
import test
import config
import subprocess
import getopt, sys

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
    arglist = sys.argv[1:][0]

    subprocess.call(["mkdir", "testcases/"+str(t.ts)+"/manual"])
    ManualTest.getandmanual(t, 1, *arglist.split())
    print("====================")
    t.printresult()