import sys
import os
import subprocess
from random import randint
sys.path.insert(1, './firrtl-operations')
from my_uint import *

class operation:
    ops = {}
    ops["+"] = my_uint.uint_add
    ops["-"] = my_uint.uint_sub
    ops["*"] = my_uint.uint_mul
    ops["/"] = my_uint.uint_div
    ops["%"] = my_uint.uint_rem
    ops["<"] = my_uint.uint_lt
    ops["<="] = my_uint.uint_leq
    ops[">"] = my_uint.uint_gt
    ops[">="] = my_uint.uint_geq
    ops["=="] = my_uint.uint_eq
    ops["!="] = my_uint.uint_neq
    ops["pad"] = my_uint.uint_pad
    ops["shl"] = my_uint.uint_shl
    ops["shr"] = my_uint.uint_shr

    def randcreate(digitlength: int) -> int:
        return randint(2**(digitlength-1), (2**digitlength)-1)

    def declareVariable(f, num: my_uint):
        f.write("\tUInt<" + str(num.bitsize) + "> u" + str(num.value) + "(\"" + str(hex(num.value)) + "\");\n")

    def binary(f, op: str, a: my_uint, b: my_uint):
        func = operation.ops[op]
        result = func(a,b)
        f.write("\tassert(u"+str(a.value)+op+"u"+str(b.value)+ " == UInt<"+str(result.bitsize)+">(\"" + str(hex(result.value)) + "\"));\n")

    def unary(f, op: str, a: my_uint, b: my_uint):
        func = operation.ops[op]
        result = func(a,b)
        f.write("\tassert("+str(result.value) +" == (u"+str(a.value)+op+"u"+str(b.value)+"));\n")

    def bitwise(f, op: str, a: my_uint, n: int):
        func = operation.ops[op]
        result = func(a, n)
        f.write("\tassert(u"+str(a.value)+"."+op+"<"+str(n)+">() == UInt<"+str(result.bitsize)+">(\""+str(hex(result.value))+"\"));\n")

class file:
    def __init__(self, testcase): #initalize file
        f = open("Runner.cpp", "w")
        self.f = f
        self.testcase = testcase

    def new_uint(self, bitsize: int, value: int) -> my_uint:# create my_uint and declare in cpp
        obj = my_uint(bitsize, value)
        operation.declareVariable(self.f, obj)
        return obj

    # def populate_list(self, n, bitsize):
    #     li = []
    #     for i in range(n):
    #         li.append(self.new_uint(bitsize, operation.randcreate(bitsize)))
    #     return li

    def docalculate(self, op: str, a: my_uint, b: my_uint): #call correct operation
        bins = ["+", "-", "*", "/", "%"]
        uns = ["<", "<=", ">", ">=", "==", "!="]
        bits = ["pad", "shl", "shr"]
        if op in bins:
            operation.binary(self.f, op, a, b)
        elif op in uns:
            operation.unary(self.f, op, a, b)
        elif op in bits:
            operation.bitwise(self.f, op, a, b)

    def top(self):#header and main
        self.f.write("#include \"./firrtl-sig/uint.h\"\n")
        self.f.write("#include <iostream>\n")
        self.f.write("#include <assert.h>\n")
        self.f.write("#include <stdlib.h>\n")
        self.f.write("using namespace std;\n\n")
        self.f.write("int main() {\n\n")

    def bottom(self): #return and closing
        self.f.write("\n")
        self.f.write("\treturn 0;\n")
        self.f.write("}")

    def runprogram(self):
        self.top()
        self.testcase(self) # run test
        self.bottom()
        self.f.close()
        subprocess.call(["g++", "Runner.cpp", "-o", "output"]) #test cpp program
        subprocess.call(["./output"])
        subprocess.call(["rm", "output"])
        print("test ended!")

    def testcase1(self): # modify to test for given variable
        a = self.new_uint(16, operation.randcreate(16))
        b = self.new_uint(16, operation.randcreate(16))
        self.docalculate("+", a, b)

    def testcase2(self): #another example
        a = self.new_uint(16, operation.randcreate(16))
        self.docalculate("shr", a, 4)

if __name__=="__main__":
    subprocess.call(["rm", "Runner.cpp"])
    test = file(file.testcase1)
    test.runprogram()
    #test = file(file.testcase2)
    #test.runprogram()
    #subprocess.call(["rm", "Runner.cpp"])

