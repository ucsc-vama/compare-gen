#import subprocess
import generator
from my_uint import *

def getbitsize(var):
    return len(bin(var)[2:])

list_two = ["+", "-", "*", "<", "<=", ">", ">=", "==", "!=", "&", "|", "^", "cat", "/", "%"]
list_bitwise = ["pad", "shl", "shr", "<<", ">>", "tail", "head"]

def create_randvars(self, n, bitsize):
    li = set()
    for i in range(n):
        var = generator.operation.randcreate(bitsize)
        generator.file.new_uint(self, bitsize, var)
        li.add(var)
    return li

def create_vars(self, n):
    li = set()
    for i in range(n):
        if i >= 8:
            generator.file.new_uint(self, getbitsize(i), i)
            li.add(i)
    return li

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
    manual = generator.file(filename)
    manual.runmanual(op,a,b)

###################################################### test cases

def testcase1(self): # not used
    li = create_vars(self, 10)

def testcase2(self): # + - * < <= > >= == != & | ^ cat / %
    li = create_vars(self, 16)
    calc_two(self, li)

def testcase3(self): # pad shl shr << >> head tail
    li = create_randvars(self, 10, 32)
    calc_bitwise(self, li)

def testcase4(self): # ~ andr orr
    li = create_randvars(self, 10, 32)
    calc_sin(self, li)

def testcase5(self): # bits
    li = create_vars(self, 16)
    calc_lohi(self, li)

def keylimetest1(self): #test first 1000 numbers
    li = create_vars(self, 1000)
    calc_two(self, li)

def keylimetest2(self): #test 1000 variables of bitsize 32
    li = create_randvars(self, 1000, 32)
    calc_two(self, li)

########################################################

def testcasemanual():
    calc_manual("test1.cpp", "+", 13, 15)
    calc_manual("test2.cpp", "+", 14, 11)
    calc_manual("test3.cpp", "+", 9, 12)

def testcasebrute(self, maxsize=0):
    # testcase2(self)
    create_vars(self, (1<<maxsize)-1)

#########################################################

def testbrute(maxsize=0):
    brute = generator.file("Brute1.cpp")
    brute.settestcase(testcasebrute)
    brute.runprogram(maxsize)

if __name__=="__main__":
    testcasemanual()
    testbrute(8)
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