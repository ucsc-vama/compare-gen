from math import *
import test
import config
import subprocess
# import threading
import getopt, sys

class BruteTest:

    def testpossible(self,varsize):
        # for op in ["+", "-", "*", "cat"]:
        #     for i in range(0,varsize):
        #         for j in range(0, varsize):
        #             self.calc_variables(op, i, j)
        # for op in ["==", "!=", "/", "%", "&", "|", "^"]:
        #     for i in range(0,varsize):
        #          self.calc_variables(op, i, i)
        # for op in config.list_bitwise:
        #     for i in range(0,varsize):
        #         for j in range(i):
        #             print(op, i, j)
        #             self.calc_variables(op, i, j)
        for op in config.headtail:
            for i in range(0,varsize):
                isize = config.getbitsize(i)
                for j in range(0,isize):
                    self.calc_variables(op, i, j)
        # for op in config.binbit:
        #     for i in range(0,varsize):
        #         self.calc_variables(str(self.ts)+"/brute", op, i)
        # for op in config.sins:
        #     for i in range(0, varsize):
        #         self.calc_variables(str(self.ts)+"/brute", op, i)

    # def testthreeparm(self,  maxbitsize):
    #     for i in range(2,maxbitsize):
    #         isize = config.getbitsize(i)
    #         for h in range(0, isize):
    #             for l in range(0, h):#change to hize+1
    #                 self.calc_variables(str(self.ts)+"/brute", "bits", i,h,l)

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