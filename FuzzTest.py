from math import *
import test
import config
import getopt, sys

class FuzzTest: #27

    def testpossible(self,varsize):
        for op in ["+", "-", "*", "cat", "==", "!=", "/", "%", "&", "|", "^", "<", "<=", ">", ">="]:
            a = 1
            for _ in range(0,varsize):
                a <<= 1
                b = 1 
                for _ in range(0, varsize):
                    b <<= 1
                    self.calc_variables(op, a, b)
        for op in ["==", "!=", "/", "%", "&", "|", "^", "<", "<=", ">", ">="]:
            for i in range(0,varsize):
                for j in range(0, varsize):
                    self.calc_variables(op, i, j)
        for op in ["pad", "shl", "shr", "dshl", "dshr"]:
            a = 1
            for _ in range(0,varsize):
                a <<= 1
                for b in [0,1,a]:
                  self.calc_variables(op, a, b)
        for op in ["tail", "head"]:
            a = 1
            for _ in range(0,varsize):
                isize = config.getbitsize(a)
                for b in [0, 1, isize]:
                    self.calc_variables(op, a, b)
                a<<= 1
        for op in ["andr", "orr", "xorr", "~"]]:
            a = 1
            for _ in range(0,varsize):
                self.calc_variables(op, a)
                a <<=1
        a = 1
        for _ in range(2,varsize):
            a <<= 1
            isize = config.getbitsize(a)
            for h in [0, 1,isize-1]:
                for l in range(h+1):
                    self.calc_variables("bits", a,h,l)

if __name__=="__main__":
    t = test.runtests()
    arglist = sys.argv[1:]
    options = "t:s:ch"
    long_options = ["type=", "size=", "clear", "help"]
    size = 1
    try:
        arguments, values = getopt.getopt(arglist, options, long_options)
        for currentArgument, currentValue in arguments:
            if currentArgument in ("-s", "--size"):
                size = int(currentValue)
            elif currentArgument in ("-t", "--type"):
                t.type = currentValue
            elif currentArgument in ("-c", "--clear"):
                t.clear = True
            elif currentArgument in ("-h", "--help"):
                print("usage: FuzzTest.py -t [uint/sint] -s <max value>")
                sys.exit()
    except getopt.error as err:
        print (str(err))

    FuzzTest.testpossible(t,size)
    print("====================")
    t.printresult()