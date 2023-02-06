from math import *
import test
import config
import subprocess
import getopt, sys

class ManualTest:

    def getandmanual(self, type, a = 0, b=0, c=0, d=0):
        if b in config.list_two:
            self.calc_manual(type, b, int(a), int(c))
        elif b in config.list_bitwise:
            self.calc_manual(type, b, int(a), int(c))
        elif b in config.headtail:
            self.calc_manual(type, b, int(a), int(c))
        elif a in config.binbit:
            self.calc_manual(type, a, int(b))
        elif a in config.sins:
            self.calc_manual(type, a, int(b))
        elif b in config.threeparm:
            self.calc_manual(type, b, int(a), int(c), int(d))
        else:
            print("invalid operator")

if __name__=="__main__":
    t = test.runtests()
    if len(sys.argv) == 1:
        print("Usage: ManualTest.py -h <help>")
        sys.exit()

    arglist = sys.argv[1:]
    options = "h"
    long_options = ["help"]
    try:
        arguments, values = getopt.getopt(arglist, options, long_options)
        for currentArgument, currentValue in arguments:
            if currentArgument in ("-h", "--help"):
                print("syntax:")
                print("python3 ManualTest.py [sint/uint] [operand1] [+, -, *, /, pad, shl, shr, <<, >>] [operand2]")
                print("python3 ManualTest.py [sint/uint] [operand1] [head, tail] [operand2]")
                print("python3 ManualTest.py [sint/uint] [andr, orr, xoor, ~] [operand]")
                print("python3 ManualTest.py [sint/uint] [operand] bits [high] [low]")
                sys.exit()
    except getopt.error as err:
        print (str(err))

    subprocess.call(["mkdir", "testcases/"+str(t.ts)+"/manual"])
    ManualTest.getandmanual(t, *arglist)
    print("====================")
    t.printresult()