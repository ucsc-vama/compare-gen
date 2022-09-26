from random import randint
import test
import subprocess
import getopt, sys

class RandomTest:

    def __init__(self):
        self.values = set()

    def findrandoms(self, varsize=0):
        return randint(0,varsize)

    def calc_random(self,op, a, b=0, c=0):
        self.calc_variables(str(self.ts)+"/random", op,a,b,c)

if __name__=="__main__":
    t = test.runtests()
    subprocess.call(["mkdir", "testcases/"+str(t.ts)+"/random"])
    arglist = sys.argv[1:]
    options = "n:s:o:h"
    long_options = ["number=", "size=", "operator=", "help"]
    n = 1
    s = 1
    op = "+"
    try:
        arguments, values = getopt.getopt(arglist, options, long_options)
        for currentArgument, currentValue in arguments:
            if currentArgument in ("-n", "--numbers"):
                n = int(currentValue)
            elif currentArgument in ("-s", "--size"):
                s = int(currentValue)
            elif currentArgument in ("-o", "--operator"):
                op = currentValue
            elif currentArgument in ("-h", "--help"):
                print("usage: RandomTest.py -n <number of tests> -s <max value> -o \"<operator>\"")
                sys.exit()
    except getopt.error as err:
        print (str(err))

    varsize = (1<<s) - 1
    R = RandomTest()
    for i in range(n):
        a = R.findrandoms(varsize)
        b = R.findrandoms(varsize)
        c = R.findrandoms(varsize)
        RandomTest.calc_random(t,op, a, b, c)
    print("====================")
    t.printresult()