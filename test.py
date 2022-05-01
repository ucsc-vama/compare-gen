import subprocess
import generator
from my_uint import *

def populate_list(self, li, n, bitsize):
    for i in range(n):
        li.append(generator.file.new_uint(self, bitsize, generator.operation.randcreate(bitsize)))
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
            generator.file.docalculate(self,"pad", i, j)
            generator.file.docalculate(self,"shl", i, j)
            generator.file.docalculate(self,"shr", i, j)
            if j.bitsize < 64 and j.value > 0:
                generator.file.docalculate(self,"/", i, j)
                generator.file.docalculate(self,"%", i, j)
            
def calc_dyn(self, li):
    b = my_uint(4, 0x4)
    for i in li:
        generator.file.docalculate(self,"<<", i, b)
        generator.file.docalculate(self,">>", i, b)
        generator.file.docalculate(self,"~", i)

def testcase3(self):
    #simple random cases

    li = []
    li = populate_list(self, li, 3, 16)
    calc_all(self, li)

    li = []
    li = populate_list(self, li, 3, 32)
    calc_all(self, li)

    li = []
    li = populate_list(self, li, 3, 127)
    calc_all(self, li)

    li = []
    li = populate_list(self, li, 3, 200)
    calc_all(self, li)

    #small values
    li = []
    li.append(generator.file.new_uint(self, 1, 0x0))
    li.append(generator.file.new_uint(self, 1, 0x1))

    li = []
    li.append(generator.file.new_uint(self, 2, 0x2))
    li.append(generator.file.new_uint(self, 2, 0x3))

    li = []
    li.append(generator.file.new_uint(self, 3, 0x4))
    li.append(generator.file.new_uint(self, 3, 0x5))
    li.append(generator.file.new_uint(self, 3, 0x6))
    li.append(generator.file.new_uint(self, 3, 0x7))

    li = []
    li.append(generator.file.new_uint(self, 4, 0x8))
    li.append(generator.file.new_uint(self, 4, 0x9))
    li.append(generator.file.new_uint(self, 4, 0xA))
    li.append(generator.file.new_uint(self, 4, 0xB))
    li.append(generator.file.new_uint(self, 4, 0xC))
    li.append(generator.file.new_uint(self, 4, 0xD))
    li.append(generator.file.new_uint(self, 4, 0xE))
    li.append(generator.file.new_uint(self, 4, 0xF))
    
    
    calc_all(self, li)
    calc_dyn(self, li)
    

if __name__=="__main__":
    subprocess.call(["rm", "Runner.cpp"])
    a = generator.file(testcase3)
    a.runprogram()