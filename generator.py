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

    def randcreate(digitlength):
        return randint(2**(digitlength-1), (2**digitlength)-1)

    def declareVariable(f, num):
        f.write("\tUInt<" + str(num[1].bitsize) + "> u" + num[0] + "(\"" + str(hex(num[1].value)) + "\");\n")

    def genvariables(f):
        bitsize = 16
        li = []
        li.append(("a", my_uint(bitsize, operation.randcreate(bitsize))))
        li.append(("b", my_uint(bitsize, operation.randcreate(bitsize))))
        li.append(("c", my_uint(bitsize, operation.randcreate(bitsize))))
        li.append(("d", my_uint(bitsize, operation.randcreate(bitsize))))
        for n in li:
            operation.declareVariable(f, n)
        return li

    def binary(f, op, a, b):
        func = operation.ops[op]
        result = func(a[1],b[1])
        f.write("\tassert(u"+a[0]+op+"u"+b[0]+" == UInt<"+str(result.bitsize)+">(\"" + str(hex(result.value)) + "\"));\n")

    def unary(f, op, a, b):
        func = operation.ops[op]
        result = func(a[1],b[1])
        f.write("\tassert("+str(result.value) +" == (u"+a[0]+op+"u"+b[0]+"));\n")

    def bitwise(f, op, a, n):
        func = operation.ops[op]
        result = func(a[1], n)
        f.write("\tassert(u"+a[0]+"."+op+"<"+str(n)+">() == UInt<"+str(result.bitsize)+">(\""+str(hex(result.value))+"\"));\n")

def top(f):
    f.write("#include \"./firrtl-sig/uint.h\"\n")
    f.write("#include<iostream>\n")
    f.write("#include <assert.h>\n")
    f.write("#include <stdlib.h>\n")
    f.write("using namespace std;\n\n")
    f.write("int main() {\n\n")

def testcase1(f, vars):
    operation.binary(f, "+", vars[0], vars[1])

def testcase2(f, vars):
    operation.bitwise(f,"shr",vars[0],4)
    
def bottom(f):
    f.write("\n")
    f.write("\treturn 0;\n")
    f.write("}")

def runprogram(test):
    f = open("Runner.cpp", "w")
    top(f)
    test(f, operation.genvariables(f))
    bottom(f)
    f.close()

    subprocess.call("make")
    subprocess.call("./Runner")
    subprocess.call(["make", "clean"])

if __name__=="__main__":

    subprocess.call(["rm", "Runner.cpp"])
    subprocess.call(["make", "clean"])
    runprogram(testcase1)
    runprogram(testcase2)
    #subprocess.call(["rm", "Runner.cpp"])

