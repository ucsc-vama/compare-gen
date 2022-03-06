import sys
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

def top(f):
    f.write("#include \"./firrtl-sig/uint.h\"\n")
    f.write("#include<iostream>\n")
    f.write("#include <assert.h>\n")
    f.write("#include <stdlib.h>\n")
    f.write("using namespace std;\n\n")
    f.write("int main() {\n\n")

def testcase(f):
    top(f)
    a = ("a", my_uint(16, 0xcafe))
    b = ("b", my_uint(16, 0xbebe))
    operation.declareVariable(f, a)
    operation.declareVariable(f, b)
    operation.binary(f,"+",a,b)
    operation.binary(f,"-",a,b)
    operation.binary(f,"*",a,b)
    operation.binary(f,"/",a,b)
    operation.binary(f,"%",a,b)
    operation.unary(f,"<",a,b)
    operation.unary(f,"<=",a,b)
    operation.unary(f,">",a,b)
    operation.unary(f,">=",a,b)
    operation.unary(f,"==",a,b)
    operation.unary(f,"!=",a,b)
    bottom(f)
    
def bottom(f):
    f.write("\n")
    f.write("\treturn 0;\n")
    f.write("}")

if __name__=="__main__":

    f = open("Runner1.cpp", "w")
    testcase(f)

    f = open("Runner2.cpp", "w")
    testcase(f)

    f.close()