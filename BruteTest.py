from math import *
import test
import config
import subprocess
# import threading
import getopt, sys

class BruteTest:

    def testpossible(self,varsize):
        for op in ["+", "-", "*", "cat"]:
            for i in range(0,varsize):
                for j in range(0, varsize):
                    self.calc_variables(op, i, j)
        # for op in ["==", "!=", "/", "%", "&", "|", "^"]:
        for op in ["==", "!=", "/", "%", "&", "|", "^", "<", "<=", ">", ">="]:
            for i in range(0,varsize):
                 self.calc_variables(op, i, i)
        for op in ["pad", "shl", "shr", "dshl", "dshr"]:
            for i in range(0,varsize):
                for j in range(i):
                    self.calc_variables(op, i, j)
        for op in ["tail", "head"]:
            for i in range(0,varsize):
                isize = config.getbitsize(i)
                for j in range(0,isize):
                    self.calc_variables(op, i, j)
        for op in ["andr", "orr", "xorr"]:
            for i in range(0,varsize):
                self.calc_variables(op, i)
        for op in ["~"]:
            for i in range(0, varsize):
                self.calc_variables(op, i)
        for i in range(2,varsize):
            isize = config.getbitsize(i)
            for h in range(1, isize):
                for l in range(0, h):#change to hize+1
                    self.calc_variables("bits", i,h,l)

    # def testthreeparm(self,  maxbitsize):

if __name__=="__main__":
    t = test.runtests()
    arglist = sys.argv[1:]
    options = "t:s:ch"
    long_options = ["type=", "size=", "clear", "help"]
    maxbit = 1
    try:
        arguments, values = getopt.getopt(arglist, options, long_options)
        for currentArgument, currentValue in arguments:
            if currentArgument in ("-s", "--size"):
                maxbit = 1<<int(currentValue) -1
            elif currentArgument in ("-t", "--type"):
                t.type = currentValue
            elif currentArgument in ("-c", "--clear"):
                t.clear = True
            elif currentArgument in ("-h", "--help"):
                print("usage: BruteTest.py -t [uint/sint] -s <max value>")
                sys.exit()
    except getopt.error as err:
        print (str(err))

    BruteTest.testpossible(t, maxbit)
    print("====================")
    t.printresult()