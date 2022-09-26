from math import *
import test
import config
import subprocess
import threading
import getopt, sys

class BruteTest:

    def testpossible(self, varsize):
        for op in config.list_two:
            for i in range(0,varsize):
                for j in range(0,varsize):
                    self.calc_variables(str(self.ts)+"/brute", op, i, j)
        # for op in config.list_bitwise:
        #     for i in range(0,varsize):
        #         for j in range(5):
        #             self.calc_variables(str(self.ts)+"/brute", op, i, j)
        # for op in config.headtail:
        #     for i in range(0,varsize):
        #         isize = config.getbitsize(i)
        #         for j in range(0,isize):
        #             self.calc_variables(str(self.ts)+"/brute", op, i, j)
        # for op in config.binbit:
        #     for i in range(0,varsize):
        #         self.calc_variables(str(self.ts)+"/brute", op, i)
        # for op in config.sins:
        #     for i in range(0, varsize):
        #         self.calc_variables(str(self.ts)+"/brute", op, i)

    def testthreeparm(self,  maxbitsize):
        for i in range(2,maxbitsize):
            isize = config.getbitsize(i)
            for h in range(0, isize):
                for l in range(0, h):#change to hize+1
                    self.calc_variables(str(self.ts)+"/brute", "bits", i,h,l)

if __name__=="__main__":
    t = test.runtests()
    subprocess.call(["mkdir", "testcases/"+str(t.ts)+"/brute"])
    arglist = sys.argv[1:]
    options = "s:h"
    long_options = ["size=", "help"]
    maxbit = 1
    try:
        arguments, values = getopt.getopt(arglist, options, long_options)
        for currentArgument, currentValue in arguments:
            if currentArgument in ("-s", "--size"):
                maxbit = int(currentValue)
            elif currentArgument in ("-h", "--help"):
                print("usage: BruteTest.py -s <max value>")
                sys.exit()
    except getopt.error as err:
        print (str(err))

    maxbit = 1<<maxbit -1

    t1 = threading.Thread(target=BruteTest.testpossible, args=(t, maxbit,))
    # t2 = threading.Thread(target=BruteTest.testthreeparm, args=(t, maxbit,))
    t1.start()
    # t2.start()
    t1.join()
    # t2.join()
    # BruteTest.testpossible(t,upperlimit)
    print("====================")
    t.printresult()