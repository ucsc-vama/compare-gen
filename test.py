import subprocess
import generator
from model_uint import *
from random import randint
from datetime import datetime

################################################## Helper

def getbitsize(var):
    return ceil(log2(var+1))

list_two = ["+", "-", "*", "<", "<=", ">", ">=", "==", "!=", "&", "|", "^", "cat", "/", "%"]
list_bitwise = ["pad", "shl", "shr", "<<", ">>", "tail", "head"]

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
        self.count = 0

    def printresult(self):
        print("tests completed:", self.count)

    def calc_variables(self, folder,filename, op, a, b):
        manual = generator.file(folder,filename)
        manual.runmanual(op,a,b)
        self.count += 1

    def createfolder(self):
        subprocess.call(["mkdir", "testcases/"+str(self.ts)])
        subprocess.call(["mkdir", "testcases/"+str(self.ts)+"/brute"])
        subprocess.call(["mkdir", "testcases/"+str(self.ts)+"/manual"])
        subprocess.call(["mkdir", "testcases/"+str(self.ts)+"/random"])

    def testpossible(self, varsize):
        for op in list_two:
            for i in range(8,varsize): #testing only after 8. change after fix
                for j in range(8,varsize):
                    self.calc_variables(str(self.ts)+"/brute","test"+ str(i) + ''.join(str(ord(c)) for c in op) + str(j), op, i, j)

    def calc_random(self,op, varsize=0):
        a = randint(8,varsize)#testing only 4 bits
        b = randint(8,varsize)
        self.calc_variables(str(self.ts)+"/random", "test"+str(a)+''.join(str(ord(c)) for c in op)+str(b),op,a,b)

    def calc_manual(self, filename, op, a, b):
        self.calc_variables(str(self.ts)+"/manual",filename, op, a, b)

    ########################################################

    def testcasemanual(self):
        self.calc_manual("test1", "+", 13, 15)

    def testcasebrute(self, maxsize=0):
        varsize = (1<<maxsize) - 1
        self.testpossible( varsize)

    def testcaserandom(self, maxsize=0):
        varsize = (1<<maxsize) - 1
        self.calc_random("+",varsize)

    #########################################################

if __name__=="__main__":
    a = runtests()
    a.testcasemanual()
    # a.testcasebrute(4)
    a.testcaserandom(4)
    a.printresult()