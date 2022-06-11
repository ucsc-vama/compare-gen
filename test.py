import subprocess
import generator
from my_uint import *

### complete test 
def calc_complete(self, li):
    for i in li:
        for j in li:
            generator.file.docalculate(self,"*", i, j)

def populate_list(self, n, bitsize):
    li = []
    for i in range(n):
        li.append(generator.file.new_uint(self, bitsize, generator.operation.randcreate(bitsize)))
    return li

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

def calc_all(self, li):
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
            # generator.file.docalculate(self,"pad", i, j)
            # generator.file.docalculate(self,"shl", i, j)
            # generator.file.docalculate(self,"shr", i, j)
            # generator.file.docalculate(self,"&", i, j)
            # generator.file.docalculate(self,"|", i, j)
            # generator.file.docalculate(self,"^", i, j)
            # generator.file.docalculate(self,"andr", i, j)
            # generator.file.docalculate(self,"orr", i, j)
            # generator.file.docalculate(self,"xorr", i, j)
            # generator.file.docalculate(self,"cat", i, j)
            # if j.bitsize < 64 and j.value > 0:
            #     generator.file.docalculate(self,"/", i, j)
            #     generator.file.docalculate(self,"%", i, j)
            
def calc_add(self, li):
    for i in li:
        for j in li:
            generator.file.docalculate(self,"+", i, j)

def calc_bitwise(self, li):
    for i in li:
        for j in range(100):
            generator.file.docalculate(self,"pad", i, j)
            generator.file.docalculate(self,"shl", i, j)
            generator.file.docalculate(self,"shr", i, j)


def calc_dyn(self, li):
    b = my_uint(3, 0x4)
    #b = my_uint(5, 0x1f)
    for i in li:
        generator.file.docalculate(self,"<<", i)
        generator.file.docalculate(self,">>", i)
        generator.file.docalculate(self,"~", i)

def calc_lohi(self, li):
    for i in li:
        generator.file.docalculate(self,"bits", i)

def testcase3(self):
    ##complete test (working)
    li = create_vars(self, 16)
    # calc_complete(self, li)
    calc_all(self, li)
    # calc_dyn(self, li)
    # calc_lohi(self, li)

def testcase1(self):
    li = create_randvars(self, 10, 32)
    calc_add(self, li)

def testcase2(self):
    li = create_randvars(self, 10, 32)
    calc_bitwise(self, li)

if __name__=="__main__":
    #subprocess.call(["rm", "Runner.cpp"])
    a = generator.file("Runner1.cpp",testcase1)
    a.runprogram()
    b = generator.file("Runner2.cpp",testcase3)
    b.runprogram()
    c = generator.file("Runner3.cpp",testcase2)
    c.runprogram()