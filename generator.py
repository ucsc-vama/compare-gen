import sys
import subprocess
import os.path
from random import randint
sys.path.insert(1, str('./firrtl-operations'))
from model_uint import *

def getbitsize(var):
    if var == 0:
        return 1
    return ceil(log2(var+1))
    # return len(bin(var)[2:])

bins = ["+", "-", "*", "/", "%", "&", "|", "^"]
uns = ["<", "<=", ">", ">=", "==", "!="]
bits = ["pad", "shl", "shr", "head", "tail"]
dyn = ["<<", ">>"]
sins = ["~"]
binbit = ["andr", "orr", "xorr"]
vlv = ["cat"]
threeparm = ["bits"]

class operation:
    ops = {}
    ops["+"] = model_uint.uint_add
    ops["-"] = model_uint.uint_sub
    ops["*"] = model_uint.uint_mul
    ops["/"] = model_uint.uint_div
    ops["%"] = model_uint.uint_rem
    ops["<"] = model_uint.uint_lt
    ops["<="] = model_uint.uint_leq
    ops[">"] = model_uint.uint_gt
    ops[">="] = model_uint.uint_geq
    ops["=="] = model_uint.uint_eq
    ops["!="] = model_uint.uint_neq
    ops["pad"] = model_uint.uint_pad
    ops["shl"] = model_uint.uint_shl
    ops["shr"] = model_uint.uint_shr
    ops["<<"] = model_uint.uint_dshl
    ops[">>"] = model_uint.uint_dshr
    ops["~"] = model_uint.uint_not
    ops["&"] = model_uint.uint_and
    ops["|"] = model_uint.uint_or
    ops["^"] = model_uint.uint_xor
    ops["andr"] = model_uint.uint_andr
    ops["orr"] = model_uint.uint_orr
    ops["xorr"] = model_uint.uint_xorr
    ops["cat"] = model_uint.uint_cat
    ops["bits"] = model_uint.uint_bits
    ops["tail"] = model_uint.uint_tail
    ops["head"] = model_uint.uint_head

    def randcreate(digitlength: int) -> int:
        return randint(2**(digitlength-1), (2**digitlength)-1)

    def declareVariable(f, num: model_uint):
        f.write("\tUInt<" + str(num.bitsize) + "> u" + str(num.value) + "(\"" + str(hex(num.value)) + "\");\n")

    def declareOneVariable(f, num: model_uint, name: str):
        f.write("\tUInt<" + str(num.bitsize) + "> " + name + "(\"" + str(hex(num.value)) + "\");\n")

    #	assert(u0+u0 == UInt<1>("0x0"));
    def binary(file, op: str, a, b):
        func = operation.ops[op]
        uint_a = model_uint(a)
        uint_b = model_uint(b)
        result = func(uint_a, uint_b)
        if result != None: #only bc divsion by zero is impossible
            file.f.write("\tassert((a"+op+"b"+ ") == UInt<"+str(result.bitsize)+">(\"" + str(hex(result.value)) + "\"));\n")

    #	assert(0 == (u59221<u58024));
    def unary(file, op: str, a: int, b: int):
        func = operation.ops[op]
        uint_a = model_uint(a)
        uint_b = model_uint(b)
        result = func(uint_a, uint_b)
        file.f.write("\tassert("+str(result.value) +" == (a"+op+"b"+"));\n")

    #	assert(u59221.pad<3>() == UInt<16>("0xe755"));
    def bitwise(file, op: str, a: int, n):
        func = operation.ops[op]
        uint_a = model_uint(a)
        result = func(uint_a, n)
        file.f.write("\tassert(a"+"."+op+"<"+str(n)+">() == UInt<"+str(result.bitsize)+">(\""+str(hex(result.value))+"\"));\n")

    #   assert((u15 >> UInt<3>("0x4")) == UInt<4>("0x0"));
    def dynamic(file, op: str, a: int, b):
        func = operation.ops[op]
        uint_a = model_uint(a)
        b_size = getbitsize(b)
        uint_b = model_uint(b, b_size)
        result = func(uint_a, uint_b)
        file.f.write("\tassert((a"+" "+op+" UInt<"+str(b_size)+">(\""+str(hex(uint_b.value))+"\")) == UInt<"+str(result.bitsize)+">(\""+str(hex(result.value))+"\"));\n")

    #   assert(~u0 == UInt<1>("0x0"));
    def singular(file, op: str, a: int):
        func = operation.ops[op]
        uint_a = model_uint(a)
        result = func(uint_a)
        file.f.write("\tassert("+op+"a"+" == UInt<"+str(result.bitsize)+">(\""+str(hex(result.value))+"\"));\n")

    #   assert(u15%u15 == UInt<4>("0x0"));
    def comp(file, op: str, a: int, b: int):
        func = operation.ops[op]
        uint_a = model_uint(a)
        uint_b = model_uint(b)
        result = func(uint_a, uint_b)
        file.f.write("\tassert((a"+op+"b"+ ") == UInt<"+str(result.bitsize)+">(\"" + str(hex(result.value)) + "\"));\n")

    #   assert((u4059599200.andr()) == UInt<1>("0x0"));
    def binarybitwise(file, op: str, a: int):
        func = operation.ops[op]
        uint_a = model_uint(a)
        result = func(uint_a)
        file.f.write("\tassert((a"+"."+op+"()) == UInt<"+str(result.bitsize)+">(\""+str(hex(result.value))+"\"));\n")

    #   assert((u4.cat(u5)) == UInt<1>("0x1"));
    def vlv(file, op: str, a: int, b: int):
        func = operation.ops[op]
        uint_a = model_uint(a)
        uint_b = model_uint(b)
        result = func(uint_a, uint_b)
        file.f.write("\tassert(a"+"."+op+"(b"+") == UInt<"+str(result.bitsize)+">(\""+str(hex(result.value))+"\"));\n")

    #   assert((u4.bits<0,1>) == UInt<1>("0x1"));
    def threeparm(file, op: str, a: int, b: int, c: int):
        func = operation.ops[op]
        uint_a = model_uint(a)
        result = func(uint_a, b, c)
        file.f.write("\tassert((a"+"."+op+"<"+str(b)+","+str(c)+">()) == UInt<"+str(result.bitsize)+">(\""+str(hex(result.value))+"\"));\n")

class file:
    
    def __init__(self, folder, name): #initalize file
        self.name = "testcases/"+folder+"/"+name
        f = open(self.name+".cpp", "w")
        self.f = f
        self.testcase = None
        self.completed = 0

    def settestcase(self, testcase):
        self.testcase = testcase

    def new_uint(self, bitsize: int, value: int) -> model_uint:# create model_uint and declare in cpp
        obj = model_uint(value, bitsize)
        operation.declareVariable(self.f, obj)
        # self.li.add(value)
        return obj

    def new_one_uint(self, bitsize: int, value: int, name) -> model_uint:# create model_uint and declare in cpp
        obj = model_uint(value, bitsize)
        operation.declareOneVariable(self.f, obj, name)
        return obj

    def docalculate(self, op: str, a, b = 0, c = 0): #call correct operation
        if op in bins:
            operation.binary(self, op, a, b)
        elif op in uns:
            operation.unary(self, op, a, b)
        elif op in bits:
            operation.bitwise(self, op, a, b)
        elif op in dyn:
            operation.dynamic(self, op, a, b)
        elif op in sins:
            operation.singular(self, op, a)
        elif op in binbit:
            operation.binarybitwise(self, op, a)
        elif op in vlv:
            operation.vlv(self, op, a, b)
        elif op in threeparm:
            operation.threeparm(self, op, a, b, c)

    def top(self):#header and main
        self.f.write("#include \"../../../firrtl-sig/uint.h\"\n")
        self.f.write("#include <assert.h>\n")
        self.f.write("int main() {\n\n")

    def bottom(self): #return and closing
        self.f.write("\n")
        self.f.write("\treturn 0;\n")
        self.f.write("}")

    # def runprogram(self,maxsize = 0):
    #     self.top()
    #     self.testcase(self, maxsize) # run test
    #     self.bottom()
    #     self.f.close()
    #     subprocess.call(["g++", self.name, "-o", "output"]) #test cpp program
    #     subprocess.call(["./output"])
    #     subprocess.call(["rm", "output"])
    #     print(self.name, ": test ended!")

    def runmanual(self, op, a, b = 0, c = 0):
        # print(self.name, ": test started!")
        self.top()
        self.new_one_uint(getbitsize(a),a, "a")
        if op not in bits and op not in binbit and op not in sins and op not in threeparm and op not in dyn: #no need to declare b
            self.new_one_uint(getbitsize(b),b, "b")
        self.docalculate(op, a, b, c)
        self.bottom()
        self.f.close()
        subprocess.call(["g++", self.name+".cpp", "-o", self.name]) #test cpp program
        if os.path.exists(self.name):
            subprocess.call(["./"+self.name])
            subprocess.call(["rm", self.name])
            self.completed = 1
    
    def getcompletedcount(self):
        return self.completed

# if __name__=="__main__":
    # subprocess.call(["rm", "Runner.cpp"])
    # test = file("Runner1.cpp", file.testcase1)
    # test.runprogram()
    #test = file(file.testcase2)
    #test.runprogram()
    #subprocess.call(["rm", "Runner.cpp"])

