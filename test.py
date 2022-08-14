import subprocess
import generator
from model_uint import *
from BruteTest import *
from RandomTest import *
from FuzzyTest import *
from random import randint
from datetime import datetime
from math import * 
from hypothesis import example, given, strategies as st

################################################## Helper

def getbitsize(var):
    if var == 0:
        return 1
    return ceil(log2(var+1))

# NEEDED: bits, ~
# list_two = ["+", "-", "*", "<", "<=", ">", ">=", "==", "!=", "&", "|", "^", "cat", "/", "%"]
list_two = ["+", "-", "*", "cat", "/", "%"]
list_bitwise = ["pad", "shl", "shr", "<<", ">>"]
headtail = ["tail", "head"]
binbit = ["andr", "orr", "xorr"]
sins = ["~"]
threeparm = ["bits"]

class runtests:

    def __init__(self):
        self.ts = datetime.timestamp(datetime.now())
        self.createfolder()
        self.completed = 0
        self.count = 0
        self.fuzzylist = []

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
        self.calc_manual("test1", "==", 7, 9)

    def testcasebrute(self, maxsize=0):
        varsize = (1<<maxsize) - 1
        BruteTest.testpossible(self, varsize)

    def testcaserandom(self, maxsize=0):
        varsize = (1<<maxsize) - 1
        RandomTest.calc_random(self,"+",varsize)

    def testcasefuzzy(self, op):
        FuzzyTest.calc_fuzzy(self)
        for a,b in self.fuzzylist:
            self.calc_variables(str(self.ts)+"/fuzzy","test"+ str(a) +op + str(b), op, a, b)

    #########################################################

if __name__=="__main__":
    a = runtests()
    # a.testcasemanual()
    # a.testcasebrute(2)
    # a.testcaserandom(4)
    a.testcasefuzzy("+")
    a.printresult()