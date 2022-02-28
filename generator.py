import sys
sys.path.insert(1, './firrtl-operations')
from my_uint import *

class operation:
    def declareVariable(f, name, num):
        f.write("\tUInt<" + str(num.bitsize) + "> u" + name + "(\"" + str(hex(num.value)) + "\");\n")

    def binary(f, op, ops, li, a, b):
        func = ops[op]
        result = func(a,b)
        f.write("\tassert(u"+str(li.index(a))+op+"u"+str(li.index(b))+" == UInt<"+str(result.bitsize)+">(\"" + str(hex(result.value)) + "\"));\n")

    def unary(f, op, ops, li, a, b):
        func = ops[op]
        result = func(a,b)
        f.write("\tassert("+str(result.value) +"==(u"+str(li.index(a))+op+"u"+str(li.index(b))+"));\n")

def header(f):
    f.write("#include \"./firrtl-sig/uint.h\"\n")
    f.write("#include<iostream>\n")
    f.write("#include <assert.h>\n")
    f.write("#include <stdlib.h>\n")
    f.write("using namespace std;\n\n")

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
    
    #print test variables
    for count, num in enumerate(li):
        operation.declareVariable(f, str(count), num)
    f.write("\n")

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

    operation.binary(f,"+",ops,li,a,b)
    operation.binary(f,"-",ops,li,a,b)
    operation.binary(f,"*",ops,li,a,b)
    operation.binary(f,"/",ops,li,a,b)
    operation.binary(f,"%",ops,li,a,b)

    f.write("\n")
    operation.unary(f,"<",ops,li,c,d)
    operation.unary(f,"<=",ops,li,c,d)
    operation.unary(f,">",ops,li,c,d)
    operation.unary(f,">=",ops,li,c,d)
    operation.unary(f,"==",ops,li,c,d)
    operation.unary(f,"!=",ops,li,c,d)
    
    f.write("\n")
    f.write("\treturn 0;\n")
    f.write("}")

if __name__=="__main__":

    f = open("Runner.cpp", "w")

    header(f)
    middle(f)

    f.close()