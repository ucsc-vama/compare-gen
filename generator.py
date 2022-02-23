import sys
sys.path.insert(1, './firrtl-operations')
from my_uint import *

a = my_uint(2, 0x2)
b = my_uint(4, 0xa)
sum = a.uint_add(b)

class operation:
    def binary(op, func, f, a, b):
        result = func(a,b)
        f.write("\tassert(u"+str(0)+op+"u"+str(1)+" == UInt<"+str(result.bitsize)+">(\"" + str(hex(result.value)) + "\"));\n")

def header(f):
    f.write("#include \"./firrtl-sig/uint.h\"\n")
    f.write("#include<iostream>\n")
    f.write("#include <assert.h>\n")
    f.write("#include <stdlib.h>\n")
    f.write("using namespace std;\n")

def middle(f):

    a = my_uint(16, 0xcafe)
    b = my_uint(16, 0xbebe)
    c = my_uint(64, 0xe2bd5b4ff8b30fc8)
    d = my_uint(64, 0x2fc353e33c6938a7)

    li = []
    li.append(a)
    li.append(b)
    li.append(c)
    li.append(d)

    f.write("int main() {\n")
    
    for count, num in enumerate(li):
        f.write("\tUInt<" + str(num.bitsize) + "> u" + str(count) + "(\"" + str(hex(num.value)) + "\");\n")
    f.write("\n")

    ops = {}
    ops["+"] = my_uint.uint_add
    ops["-"] = operation.binary
    ops["*"] = operation.binary

    operation.binary("+",ops["+"],f,a,b)

    f.write("\n")
    f.write("\treturn 0;\n")
    f.write("}")

if __name__=="__main__":

    f = open("Runner.cpp", "w")

    header(f)
    middle(f)

    f.close()