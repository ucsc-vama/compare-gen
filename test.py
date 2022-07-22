import subprocess
import generator
from model_uint import *
from random import randint
from datetime import datetime

################################################## Helper

def getbitsize(var):
    return ceil(log2(var+1))

def calc_variables(folder,filename, op, a, b):
    manual = generator.file(folder,filename)
    manual.runmanual(op,a,b)

list_two = ["+", "-", "*", "<", "<=", ">", ">=", "==", "!=", "&", "|", "^", "cat", "/", "%"]
list_bitwise = ["pad", "shl", "shr", "<<", ">>", "tail", "head"]

##################################################### create variables

def create_randvars(self, n, bitsize):
    li = set()
    for i in range(n):
        var = generator.operation.randcreate(bitsize)
        generator.file.new_uint(self, bitsize, var)
        li.add(var)
    return li

def create_vars(self, n):
    li = set()
    for i in range(n+1):
        if i >= 8:
            generator.file.new_uint(self, getbitsize(i), i)
            li.add(i)
    return li

###################################################### tests

def testpossible(ts,varsize):
    for op in list_two:
        for i in range(8,varsize+1): #testing only after 8. change after fix
            for j in range(8,varsize+1):
                calc_variables(str(ts)+"/brute","test"+ str(i) + ''.join(str(ord(c)) for c in op) + str(j), op, i, j)

def calc_random(ts,op, varsize=0):
    a = randint(8,varsize)#testing only 4 bits
    b = randint(8,varsize)
    calc_variables(str(ts)+"/random", "test"+str(a)+''.join(str(ord(c)) for c in op)+str(b),op,a,b)
    

def calc_two(self, li):
    for op in list_two:
        for i in li:
            for j in li:
                generator.file.docalculate(self,op, i, j)

def calc_bitwise(self, li):
    for op in list_bitwise:
        for i in li:
            for j in range(1,10):
                generator.file.docalculate(self, op, i, j)

def calc_sin(self, li):
    for i in li:
        generator.file.docalculate(self,"~", i)
        generator.file.docalculate(self,"andr", i)
        generator.file.docalculate(self,"orr", i)
        generator.file.docalculate(self,"xorr", i)

def calc_lohi(self, li):
    for i in li:
        for j in range(getbitsize(i)):
            for k in range(j):
                generator.file.docalculate(self,"bits", i, j, k)

def calc_manual(ts,filename, op, a, b):
    calc_variables(str(ts)+"/manual",filename, op, a, b)

########################################################

def testcasemanual(ts):
    calc_manual(ts,"test1", "+", 13, 15)

def testcasebrute(ts,maxsize=0):
    varsize = (1<<maxsize) - 1
    testpossible(ts,varsize)

def testcaserandom(ts,maxsize=0):
    varsize = (1<<maxsize) - 1
    calc_random(ts,"+",varsize)

#########################################################

# def testbrute(maxsize=0):
#     brute = generator.file("Brute1.cpp")
#     brute.settestcase(testcasebrute)
#     brute.runprogram(maxsize)

if __name__=="__main__":
    ts = datetime.timestamp(datetime.now())
    subprocess.call(["mkdir", "testcases/"+str(ts)])
    subprocess.call(["mkdir", "testcases/"+str(ts)+"/brute"])
    subprocess.call(["mkdir", "testcases/"+str(ts)+"/manual"])
    subprocess.call(["mkdir", "testcases/"+str(ts)+"/random"])
    testcasemanual(ts)
    # testcasebrute(ts,4)
    testcaserandom(ts,4)