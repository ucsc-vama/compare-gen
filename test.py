import subprocess
import generator
from model_uint import *
from random import randint
from datetime import datetime
from math import * 

################################################## Helper

def getbitsize(var):
    if var == 0:
        return 1
    return ceil(log2(var+1))

# list_two = ["+", "-", "*", "<", "<=", ">", ">=", "==", "!=", "&", "|", "^", "cat", "/", "%"]
list_two = ["+", "-", "*", "cat", "/", "%"]
list_bitwise = ["pad", "shl", "shr", "<<", ">>"]
headtail = ["tail", "head"]
binbit = ["andr", "orr", "xorr"]

##################################################### create variables

# def create_randvars(self, n, bitsize):
#     li = set()
#     for i in range(n):
#         var = generator.operation.randcreate(bitsize)
#         generator.file.new_uint(self, bitsize, var)
#         li.add(var)
#     return li

# def create_vars(self, n):
#     li = set()
#     for i in range(n+1):
#         if i >= 8:
#             generator.file.new_uint(self, getbitsize(i), i)
#             li.add(i)
#     return li

###################################################### tests

class runtests:

    def __init__(self):
        self.ts = datetime.timestamp(datetime.now())
        self.createfolder()
        self.completed = 0
        self.count = 0

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

    def testpossible(self, varsize):
        for op in list_two:
            for i in range(0,varsize): #testing only after 8. change after fix
                for j in range(0,varsize):
                    self.calc_variables(str(self.ts)+"/brute","test"+ str(i) + ''.join(str(ord(c)) for c in op) + str(j), op, i, j)
        # for op in list_bitwise:
        #     for i in range(1,varsize):
        #         for j in range(5):
        #             self.calc_variables(str(self.ts)+"/brute","test"+ str(i) + ''.join(str(ord(c)) for c in op) + str(j), op, i, j)
        # for op in headtail:
        #     for i in range(1,varsize):
        #         for j in range(1,i+1):
        #             self.calc_variables(str(self.ts)+"/brute","test"+ str(i) + ''.join(str(ord(c)) for c in op) + str(j), op, i, j)
        # for op in binbit:
        #     for i in range(0,varsize):
        #         self.calc_variables(str(self.ts)+"/brute","test"+ str(i) + ''.join(str(ord(c)) for c in op), op, i)

    def testsquare(self, varsize):
        for op in list_two:
            for i in range(varsize):
                j = 0
                while j < varsize:
                    j = (j << 1) | 1
                    self.calc_variables(str(self.ts)+"/brute","test"+ str(i) + ''.join(str(ord(c)) for c in op) + str(j), op, i, j)

    def calc_random(self,op, varsize=0):
        a = randint(8,varsize)#testing only 4 bits
        b = randint(8,varsize)
        self.calc_variables(str(self.ts)+"/random", "test"+str(a)+''.join(str(ord(c)) for c in op)+str(b),op,a,b)

    def calc_manual(self, filename, op, a, b=0, c=0):
        self.calc_variables(str(self.ts)+"/manual",filename, op, a, b)

    ########################################################

    def testcasemanual(self):
        self.calc_manual("test1", "<", 0,0)

    def testcasebrute(self, maxsize=0):
        varsize = (1<<maxsize) - 1
        self.testpossible( varsize)

    def testcaserandom(self, maxsize=0):
        varsize = (1<<maxsize) - 1
        self.calc_random("+",varsize)

    #########################################################

if __name__=="__main__":
    a = runtests()
    # a.testcasemanual()
    a.testcasebrute(2)
    # a.testcaserandom(4)
    a.printresult()