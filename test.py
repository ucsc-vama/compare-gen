#import subprocess
import generator
from my_uint import *

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
            generator.file.new_uint(self, len(bin(i)[2:]), i)
            li.add(i)
    return li

def calc_two(self, li):
    for i in li:
        for j in li:
            generator.file.docalculate(self,"+", i, j)
            generator.file.docalculate(self,"-", i, j)
            generator.file.docalculate(self,"*", i, j)
            generator.file.docalculate(self,"<", i, j)
            generator.file.docalculate(self,"<=", i, j)
            generator.file.docalculate(self,">", i, j)
            generator.file.docalculate(self,">=", i, j)
            generator.file.docalculate(self,"==", i, j)
            generator.file.docalculate(self,"!=", i, j)
            generator.file.docalculate(self,"&", i, j)
            generator.file.docalculate(self,"|", i, j)
            generator.file.docalculate(self,"^", i, j)
            generator.file.docalculate(self,"cat", i, j)
            generator.file.docalculate(self,"/", i, j)
            generator.file.docalculate(self,"%", i, j)
            # if j.bitsize < 64 and j.value > 0:
            #     generator.file.docalculate(self,"/", i, j)
            #     generator.file.docalculate(self,"%", i, j)

def calc_bitwise(self, li):
    for i in li:
        for j in range(10):
            generator.file.docalculate(self,"pad", i, j)
            generator.file.docalculate(self,"shl", i, j)
            generator.file.docalculate(self,"shr", i, j)
            generator.file.docalculate(self,"<<", i, j)
            generator.file.docalculate(self,">>", i, j)

def calc_sin(self, li):
    for i in li:
        generator.file.docalculate(self,"~", i)
        generator.file.docalculate(self,"andr", i)
        generator.file.docalculate(self,"orr", i)
        generator.file.docalculate(self,"xorr", i)

def calc_lohi(self, li):
    for i in li:
        for j in range(len(bin(i)[2:])):
            for k in range(j):
                generator.file.docalculate(self,"bits", i, j, k)

def testcase1(self): # not used
    li = create_vars(self, 10)

def testcase2(self): # + - * < <= > >= == != & | ^ cat / %
    li = create_vars(self, 16)
    calc_two(self, li)

def testcase3(self): # pad shl shr << >>
    li = create_randvars(self, 10, 32)
    calc_bitwise(self, li)

def testcase4(self): # ~ andr orr
    li = create_randvars(self, 10, 32)
    calc_sin(self, li)

def testcase5(self): # bits
    li = create_vars(self, 16)
    calc_lohi(self, li)

if __name__=="__main__":
    #subprocess.call(["rm", "Runner.cpp"])
    # a = generator.file("Runner1.cpp",testcase1)
    # a.runprogram()
    b = generator.file("Runner2.cpp",testcase2)
    b.runprogram()
    c = generator.file("Runner3.cpp",testcase3)
    c.runprogram()
    d = generator.file("Runner4.cpp",testcase4)
    d.runprogram()
    e = generator.file("Runner5.cpp",testcase5)
    e.runprogram()