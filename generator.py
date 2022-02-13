import sys
sys.path.insert(1, './firrtl-operations')
from my_uint import *

a = my_uint(2, 0x2)
b = my_uint(4, 0xa)
sum = a.uint_add(b)

def header(f):
    f.write("#include \"./firrtl-sig/uint.h\"\n")
    f.write("#include<iostream>\n")
    f.write("#include <assert.h>\n")
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

    for ia, aval in enumerate(li):
        for ib, bval in enumerate(li):
            if(aval.bitsize == bval.bitsize):
                result = aval.uint_add(bval)
                f.write("\tassert(u"+str(ia)+"+u"+str(ib)+" == UInt<" + str(result.bitsize) + ">(\"" + str(hex(result.value)) + "\"));\n")

    f.write("\n")

    for ia, aval in enumerate(li):
        for ib, bval in enumerate(li):
            if(aval.bitsize == bval.bitsize) and aval.value != bval.value:
                result = aval.uint_sub(bval)
                f.write("\tassert(u"+str(ia)+"-u"+str(ib)+" == UInt<" + str(result.bitsize) + ">(\"" + str(hex(result.value)) + "\"));\n")


    f.write("\treturn 0;\n")
    f.write("}")

if __name__=="__main__":

    f = open("Runner.cpp", "w")

    header(f)
    middle(f)

    f.close()