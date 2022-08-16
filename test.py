import subprocess
import generator
from model_uint import *
from BruteTest import *
from RandomTest import *
from FuzzyTest import *
import settings
from datetime import datetime
from math import * 

class runtests:

    def __init__(self):
        self.ts = datetime.timestamp(datetime.now())
        self.createfolder()
        self.completed = 0
        self.count = 0
        self.fuzzyset = set()

    def printresult(self):
        print("tests completed:", self.completed)
        print("tests count:", self.count)

    def calc_variables(self, folder,filename, op, a, b=0, c=0):
        manual = generator.file(folder,filename)
        manual.runmanual(op,a,b,c)
        self.completed += manual.getcompletedcount()
        self.count += 1

    def createfolder(self):
        subprocess.call(["mkdir", "testcases/"+str(self.ts)])
        subprocess.call(["mkdir", "testcases/"+str(self.ts)+"/brute"])
        subprocess.call(["mkdir", "testcases/"+str(self.ts)+"/manual"])
        subprocess.call(["mkdir", "testcases/"+str(self.ts)+"/random"])
        subprocess.call(["mkdir", "testcases/"+str(self.ts)+"/fuzzy"])

    def calc_manual(self, filename, op, a, b=0, c=0):
        self.calc_variables(str(self.ts)+"/manual",filename, op, a, b)

    ########################################################

    def testcasemanual(self):
        # self.calc_manual("test1", "bits", 3, 0, 0)
        self.calc_manual("test1", "==", 8, 9)

    def testcasebrute(self, maxsize=0):
        varsize = (1<<maxsize) - 1
        BruteTest.testpossible(self, varsize)

    def testcaserandom(self, maxsize=0):
        varsize = (1<<maxsize) - 1
        RandomTest.calc_random(self,"+",varsize)

    def testcasefuzzy(self, op):
        FuzzyTest.calc_fuzzy(self)
        for a,b in self.fuzzyset:
            self.calc_variables(str(self.ts)+"/fuzzy","test"+ str(a) +op + str(b), op, a, b)

    #########################################################

    def getandmanual(self, i, a = 0, b=0, c=0):
        if b in settings.list_two:
            self.calc_manual("test"+str(i), b, int(a), int(c))
        else:
            print("invalid operator")


if __name__=="__main__":
    test = runtests()
    # a.testcasemanual()
    # a.testcasebrute(2)
    # a.testcaserandom(4)
    # a.testcasefuzzy("+")

    manualsize = int(input("number of manual tests: ")) or 0
    for i in range(manualsize):
        inp = input()
        test.getandmanual(i, *inp.split())
    print("====================")
    randomsize = int(input("number of random tests: ")) or 0
    if randomsize > 0:
        op = input("operation: ")
        upperlimit = int(input("max bitlength: "))
        for i in range(randomsize):
            RandomTest.calc_random(test,op,upperlimit)
    print("====================")
    testbrute = input("test brute force? (y/n): ") or "n"
    if testbrute == "y":
        upperlimit = int(input("max bitlength: "))
        BruteTest.testpossible(test,upperlimit)
    print("====================")
    testfuzzy = input("test fuzzy? (y/n): ") or "n"
    if testfuzzy == "y":
        fuzzysize = int(input("number of fuzzy tests: "))
        op = input("enter operation: ")
        if op in settings.list_two:
            FuzzyTest.calc_fuzzy(test, fuzzysize)
            for a, b in test.fuzzyset:
                test.calc_variables(str(test.ts)+"/fuzzy","test"+ str(a) +"_"+''.join(str(ord(c)) for c in op)+"_" + str(b), op, a, b)
        else:
            print("invalid operator")
    print("====================")
    test.printresult()