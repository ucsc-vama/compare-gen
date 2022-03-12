import sys
import os
import subprocess
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

    def declareVariable(f, num):
        f.write("\tUInt<" + str(num[1].bitsize) + "> u" + num[0] + "(\"" + str(hex(num[1].value)) + "\");\n")

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

def testcase1(f):
    top(f)
    a = ("a", my_uint(16, 0xcafe))
    b = ("b", my_uint(16, 0xbebe))
    operation.declareVariable(f, a)
    operation.declareVariable(f, b)
    operation.bitwise(f,"shr",a,4)
    bottom(f)

def testcase2(f):
    top(f)
    a = ("a", my_uint(16, 0xcafe))
    b = ("b", my_uint(16, 0xbebe))
    operation.declareVariable(f, a)
    operation.declareVariable(f, b)
    operation.binary(f, "+", a, b)
    operation.unary(f, "==", a, b)
    operation.bitwise(f,"shr",a,4)
    bottom(f)
    
def bottom(f):
    f.write("\n")
    f.write("\treturn 0;\n")
    f.write("}")

def runprogram(test):
    f = open("Runner.cpp", "w")
    test(f)
    f.close()

    subprocess.call("make")
    subprocess.call("./Runner")
    subprocess.call(["make", "clean"])
    #subprocess.call(["rm", "Runner.cpp"])

if __name__=="__main__":

    subprocess.call(["make", "clean"])
    runprogram(testcase1)
    runprogram(testcase2)

