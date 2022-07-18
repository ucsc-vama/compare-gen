#import subprocess
import generator
from my_uint import *

################################################## Helper

def getbitsize(var):
    return len(bin(var)[2:])

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

def testpossible(varsize):
    for op in list_two:
        for i in range(8,varsize+1): #testing only after 8. change after fix
            for j in range(8,varsize+1):
                calc_variables("brute","test"+ str(i) + op + str(j), op, i, j)

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

def calc_manual(filename, op, a, b):
    calc_variables("manual",filename, op, a, b)

########################################################

def testcasemanual():
    calc_manual("test1", "+", 13, 15)
    calc_manual("test2", "+", 14, 11)
    calc_manual("test3", "+", 9, 12)

def testcasebrute(maxsize=0):
    varsize = (1<<maxsize) - 1
    testpossible(varsize)

#########################################################

# def testbrute(maxsize=0):
#     brute = generator.file("Brute1.cpp")
#     brute.settestcase(testcasebrute)
#     brute.runprogram(maxsize)

if __name__=="__main__":
    testcasemanual()
    testcasebrute(4)
    #subprocess.call(["rm", "Runner.cpp"])
    # a = generator.file("Runner1.cpp",testcase1)
    # a.runprogram()
    # b = generator.file("Runner2.cpp",testcase2)
    # b.runprogram()
    # c = generator.file("Runner3.cpp",testcase3)
    # c.runprogram()
    # d = generator.file("Runner4.cpp",testcase4)
    # d.runprogram()
    # e = generator.file("Runner5.cpp",testcase5)
    # e.runprogram()
    # key1 = generator.file("keylime1.cpp",keylimetest1)
    # key1.runprogram()
    # key2 = generator.file("keylime2.cpp",keylimetest2)
    # key2.runprogram()