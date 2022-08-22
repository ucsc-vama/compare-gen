from random import randint
import test
import subprocess
import getopt, sys

class RandomTest:

    def __init__(self):
        self.values = set()

    def findrandoms(self, varsize=0):
        self.values.add((randint(0,varsize), randint(0,varsize)))

    def calc_random(self,op, values):
        self.calc_variables(str(self.ts)+"/random", "test"+str(values[0])+"_" + ''.join(str(ord(c)) for c in op)+"_" + str(values[1]),op,values[0],values[1])

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
                o = currentValue
            elif currentArgument in ("-h", "--help"):
                print("usage: RandomTest.py -n <number of tests> -s <max value> -o \"<operator>\"")
                sys.exit()
    except getopt.error as err:
        print (str(err))

    varsize = (1<<s) - 1
    R = RandomTest()
    while len(R.values) < n:
        R.findrandoms(varsize)
    R.values = list(R.values)
    for i in range(n):
        RandomTest.calc_random(t,o, R.values[i])
    print("====================")
    t.printresult()