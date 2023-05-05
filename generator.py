from math import ceil, log2
import sys
import subprocess
import os.path
from random import randint
sys.path.insert(1, str('./firrtl-operations'))
import uint
import sint

def getbitsize(var):
    if var == 0:
        return 1
    return ceil(log2(var+1))
    # return len(bin(var)[2:])

bins = ["+", "-", "*", "/", "%"]
abu = ["^", "|", "&"]
uns = ["<", "<=", ">", ">=", "==", "!="]
bits = ["pad", "shl", "shr", "head", "tail"]
dyn = ["dshl", "dshr"]
sins = ["~"]
binbit = ["andr", "orr", "xorr"]
vlv = ["cat"]
threeparm = ["bits"]

opConvert = {
    "dshl": "<<",
    "dshr": ">>"
}

class u_operation:
    u_ops = {}
    u_ops["+"] = uint.model_uint.uint_add
    u_ops["-"] = uint.model_uint.uint_sub
    u_ops["*"] = uint.model_uint.uint_mul
    u_ops["/"] = uint.model_uint.uint_div
    u_ops["%"] = uint.model_uint.uint_rem
    u_ops["<"] = uint.model_uint.uint_lt
    u_ops["<="] = uint.model_uint.uint_leq
    u_ops[">"] = uint.model_uint.uint_gt
    u_ops[">="] = uint.model_uint.uint_geq
    u_ops["=="] = uint.model_uint.uint_eq
    u_ops["!="] = uint.model_uint.uint_neq
    u_ops["pad"] = uint.model_uint.uint_pad
    u_ops["shl"] = uint.model_uint.uint_shl
    u_ops["shr"] = uint.model_uint.uint_shr
    u_ops["dshl"] = uint.model_uint.uint_dshl
    u_ops["dshr"] = uint.model_uint.uint_dshr
    u_ops["~"] = uint.model_uint.uint_not
    u_ops["&"] = uint.model_uint.uint_and
    u_ops["|"] = uint.model_uint.uint_or
    u_ops["^"] = uint.model_uint.uint_xor
    u_ops["andr"] = uint.model_uint.uint_andr
    u_ops["orr"] = uint.model_uint.uint_orr
    u_ops["xorr"] = uint.model_uint.uint_xorr
    u_ops["cat"] = uint.model_uint.uint_cat
    u_ops["bits"] = uint.model_uint.uint_bits
    u_ops["tail"] = uint.model_uint.uint_tail
    u_ops["head"] = uint.model_uint.uint_head

    def randcreate(digitlength: int) -> int:
        return randint(2**(digitlength-1), (2**digitlength)-1)

    def declareVariable(f, num: uint.model_uint):
        f.write("\tUInt<" + str(num.bitsize) + "> u" + str(num.value) + "(\"" + str(hex(num.value)) + "\");\n")

    def declareOneVariable(f, num: uint.model_uint, name: str):
        f.write("\tUInt<" + str(num.bitsize) + "> " + name + "(\"" + str(hex(num.value)) + "\");\n")

    #	assert(u0+u0 == UInt<1>("0x0"));
    def binary(file, func, op: str, a, b):
        # func = operation.u_ops[op]
        uint_a = uint.model_uint(a)
        uint_b = uint.model_uint(b)
        result = func(uint_a, uint_b)
        if result != None: #only bc divsion by zero is impossible
            file.f.write("\tassert((a"+op+"b"+ ") == UInt<"+str(result.bitsize)+">(\"" + str(hex(result.value)) + "\"));\n")

    #	assert(0 == (u59221<u58024));
    def unary(file, func, op: str, a: int, b: int):
        # func = operation.u_ops[op]
        uint_a = uint.model_uint(a)
        uint_b = uint.model_uint(b)
        result = func(uint_a, uint_b)
        file.f.write("\tassert("+str(result.value) +" == (a"+op+"b"+"));\n")

    #	assert(u59221.pad<3>() == UInt<16>("0xe755"));
    def bitwise(file, func, op: str, a: int, n):
        # func = operation.u_ops[op]
        uint_a = uint.model_uint(a)
        result = func(uint_a, n)
        file.f.write("\tassert(a"+"."+op+"<"+str(n)+">() == UInt<"+str(result.bitsize)+">(\""+str(hex(result.value))+"\"));\n")

    #   assert((u15 >> UInt<3>("0x4")) == UInt<4>("0x0"));
    def dynamic(file, func, op: str, a: int, b):
        # func = operation.u_ops[op]
        uint_a = uint.model_uint(a)
        b_size = getbitsize(b)
        uint_b = uint.model_uint(b, b_size)
        result = func(uint_a, uint_b)
        file.f.write("\tassert((a"+" "+op+" UInt<"+str(b_size)+">(\""+str(hex(uint_b.value))+"\")) == UInt<"+str(result.bitsize)+">(\""+str(hex(result.value))+"\"));\n")

    #   assert(~u0 == UInt<1>("0x0"));
    def singular(file, func, op: str, a: int):
        # func = operation.u_ops[op]
        uint_a = uint.model_uint(a)
        result = func(uint_a)
        file.f.write("\tassert("+op+"a"+" == UInt<"+str(result.bitsize)+">(\""+str(hex(result.value))+"\"));\n")

    #   assert(u15%u15 == UInt<4>("0x0"));
    def comp(file, func, op: str, a: int, b: int):
        # func = operation.u_ops[op]
        uint_a = uint.model_uint(a)
        uint_b = uint.model_uint(b)
        result = func(uint_a, uint_b)
        file.f.write("\tassert((a"+op+"b"+ ") == UInt<"+str(result.bitsize)+">(\"" + str(hex(result.value)) + "\"));\n")

    #   assert((u4059599200.andr()) == UInt<1>("0x0"));
    def binarybitwise(file, func, op: str, a: int):
        # func = operation.u_ops[op]
        uint_a = uint.model_uint(a)
        result = func(uint_a)
        file.f.write("\tassert((a"+"."+op+"()) == UInt<"+str(result.bitsize)+">(\""+str(hex(result.value))+"\"));\n")

    #   assert((u4.cat(u5)) == UInt<1>("0x1"));
    def vlv(file, func, op: str, a: int, b: int):
        # func = operation.u_ops[op]
        uint_a = uint.model_uint(a)
        uint_b = uint.model_uint(b)
        result = func(uint_a, uint_b)
        file.f.write("\tassert(a"+"."+op+"(b"+") == UInt<"+str(result.bitsize)+">(\""+str(hex(result.value))+"\"));\n")

    #   assert((u4.bits<0,1>) == UInt<1>("0x1"));
    def threeparm(file, func, op: str, a: int, b: int, c: int):
        # func = operation.u_ops[op]
        uint_a = uint.model_uint(a)
        result = func(uint_a, b, c)
        file.f.write("\tassert((a"+"."+op+"<"+str(b)+","+str(c)+">()) == UInt<"+str(result.bitsize)+">(\""+str(hex(result.value))+"\"));\n")

class s_operation:
    s_ops = {}
    s_ops["+"] = sint.model_sint.sint_add
    s_ops["-"] = sint.model_sint.sint_sub
    s_ops["*"] = sint.model_sint.sint_mul
    s_ops["/"] = sint.model_sint.sint_div
    s_ops["%"] = sint.model_sint.sint_mod
    s_ops["<"] = sint.model_sint.sint_lt
    s_ops["<="] = sint.model_sint.sint_leq
    s_ops[">"] = sint.model_sint.sint_gt
    s_ops[">="] = sint.model_sint.sint_geq
    s_ops["=="] = sint.model_sint.sint_eq
    s_ops["!="] = sint.model_sint.sint_neq
    s_ops["pad"] = sint.model_sint.sint_pad
    s_ops["shl"] = sint.model_sint.sint_shl
    s_ops["shr"] = sint.model_sint.sint_shr
    s_ops["dshl"] = sint.model_sint.sint_dshl
    s_ops["dshr"] = sint.model_sint.sint_dshr
    s_ops["~"] = sint.model_sint.sint_not
    s_ops["&"] = sint.model_sint.sint_and
    s_ops["|"] = sint.model_sint.sint_or
    s_ops["^"] = sint.model_sint.sint_xor
    s_ops["andr"] = sint.model_sint.sint_andr
    s_ops["orr"] = sint.model_sint.sint_orr
    s_ops["xorr"] = sint.model_sint.sint_xorr
    s_ops["cat"] = sint.model_sint.sint_cat
    s_ops["bits"] = sint.model_sint.sint_bits
    s_ops["tail"] = sint.model_sint.sint_tail
    s_ops["head"] = sint.model_sint.sint_head

    def randcreate(digitlength: int) -> int:
        return randint(2**(digitlength-1), (2**digitlength)-1)

    def declareVariable(f, num: sint.model_sint):
        f.write("\tSInt<" + str(num.bitsize) + "> u" + str(num.value) + "(\"" + str(hex(num.value)) + "\");\n")

    def declareOneVariable(f, num: sint.model_sint, name: str):
        f.write("\tSInt<" + str(num.bitsize) + "> " + name + "(\"" + str(hex(num.realval)) + "\");\n")

    #	assert(u0+u0 == SInt<1>("0x0"));
    def binary(file, func, op: str, a, b):
        sint_a = sint.model_sint(a)
        sint_b = sint.model_sint(b)
        result = func(sint_a, sint_b)
        if result != None: #only bc divsion by zero is impossible
            file.f.write("\tassert(a"+op+"b"+ " == SInt<"+str(result.bitsize)+">(\"" + str(hex(result.realval)) + "\"));\n")

    def abu(file, func, op: str, a, b):
        sint_a = sint.model_sint(a)
        sint_b = sint.model_sint(b)
        result = func(sint_a, sint_b)
        if result != None: #only bc divsion by zero is impossible
            file.f.write("\tassert((a"+op+"b)"+ " == UInt<"+str(result.bitsize)+">(\"" + str(hex(result.realval)) + "\"));\n")

    #   assert(0 == (false<(a<b))));
    def unary(file, func, op: str, a: int, b: int):
        sint_a = sint.model_sint(a)
        sint_b = sint.model_sint(b)
        result = func(sint_a, sint_b)
        file.f.write("\tassert("+str(result.value) +" == (a"+op+"b"+"));\n")

    #	assert(u59221.pad<3>() == UInt<16>("0xe755"));
    def bitwise(file, func, op: str, a: int, n):
        sint_a = sint.model_sint(a)
        result = func(sint_a, n)
        if result.type == "uint":
            file.f.write("\tassert(a"+"."+op+"<"+str(n)+">() == UInt<"+str(result.bitsize)+">(\""+str(hex(result.value))+"\"));\n")
        else:
            file.f.write("\tassert(a"+"."+op+"<"+str(n)+">() == SInt<"+str(result.bitsize)+">(\""+str(hex(result.realval))+"\"));\n")

        #   assert((s15 >> UInt<3>("0x4")) == UInt<4>("0x0"));
    def dynamic(file, func, op: str, a: int, b):
        sint_a = sint.model_sint(a)
        b_size = getbitsize(b)
        uint_b = uint.model_uint(b, b_size)
        result = func(sint_a, uint_b)
        file.f.write("\tassert((a"+" "+op+" UInt<"+str(b_size)+">(\""+str(hex(uint_b.value))+"\")) == SInt<"+str(result.bitsize)+">(\""+str(hex(result.realval))+"\"));\n")

    #   assert((u4.cat(u5)) == UInt<1>("0x1"));
    def vlv(file, func, op: str, a: int, b: int):
        # func = operation.u_ops[op]
        sint_a = sint.model_sint(a)
        sint_b = sint.model_sint(b)
        result = func(sint_a, sint_b)
        file.f.write("\tassert(a"+"."+op+"(b) == SInt<"+str(result.bitsize)+">(\""+str(hex(result.realval))+"\"));\n")

class file:
    def __init__(self, folder, name): #initalize file
        self.name = "testcases/"+folder+"/"+name
        f = open(self.name+".cpp", "w")
        self.f = f
        self.testcase = None
        self.completed = 0

    def settestcase(self, testcase):
        self.testcase = testcase

    def new_uint(self, bitsize: int, value: int) -> uint.model_uint:# create uint.model_uint and declare in cpp
        obj = uint.model_uint(value, bitsize)
        u_operation.declareVariable(self.f, obj)
        return obj

    def new_one_uint(self, bitsize: int, value: int, name) -> uint.model_uint:# create uint.model_uint and declare in cpp
        obj = uint.model_uint(value, bitsize)
        u_operation.declareOneVariable(self.f, obj, name)
        return obj
    
    def new_one_sint(self, bitsize: int, value: int, name) -> sint.model_sint:# create uint.model_uint and declare in cpp
        obj = sint.model_sint(value, bitsize)
        s_operation.declareOneVariable(self.f, obj, name)
        return obj

    def docalculate(self, op: str, a, b = 0, c = 0): #call correct operation
        func = u_operation.u_ops[op]

        if op in bins:
            u_operation.binary(self, func, op, a, b)
        elif op in abu:
            u_operation.binary(self, func, op, a, b)
        elif op in uns:
            u_operation.unary(self, func, op, a, b)
        elif op in bits:
            u_operation.bitwise(self, func, op, a, b)
        elif op in dyn:
            u_operation.dynamic(self, func, opConvert[op], a, b)
        elif op in sins:
            u_operation.singular(self, func, op, a)
        elif op in binbit:
            u_operation.binarybitwise(self, func, op, a)
        elif op in vlv:
            u_operation.vlv(self, func, op, a, b)
        elif op in threeparm:
            u_operation.threeparm(self, func, op, a, b, c)

    def s_docalculate(self, op: str, a, b = 0, c = 0): #call correct operation
        func = s_operation.s_ops[op]

        if op in bins:
            s_operation.binary(self, func, op, a, b)
        elif op in abu:
            s_operation.abu(self, func, op, a, b)
        elif op in uns:
            s_operation.unary(self, func, op, a, b)
        elif op in bits:
            s_operation.bitwise(self, func, op, a, b)
        elif op in dyn:
            s_operation.dynamic(self, func, opConvert[op], a, b)
        # elif op in sins:
        #     u_operation.singular(self, func, op, a)
        elif op in binbit:#now working on
            u_operation.binarybitwise(self, func, op, a)
        elif op in vlv:
            s_operation.vlv(self, func, op, a, b)
        # elif op in threeparm:
            # u_operation.threeparm(self, func, op, a, b, c)

    def top(self, type):#header and main
        if os.getenv("GITHUB_ACTIONS"):
            if type == "uint":
                self.f.write("#include \"../../../../firrtl-sig/uint.h\"\n")
            else:
                self.f.write("#include \"../../../../firrtl-sig/sint.h\"\n")
        else:
            if type == "uint":
                self.f.write("#include \"../../../firrtl-sig/uint.h\"\n")
            else:
                self.f.write("#include \"../../../firrtl-sig/sint.h\"\n")
        self.f.write("#include <assert.h>\n")
        self.f.write("int main() {\n\n")

    def bottom(self): #return and closing
        self.f.write("\n")
        self.f.write("\treturn 0;\n")
        self.f.write("}")

    def runmanual(self, type, op, a, b = 0, c = 0):
        self.top(type)
        if type == "uint":
            self.new_one_uint(getbitsize(a),a, "a")
            if op not in bits and op not in binbit and op not in sins and op not in threeparm and op not in dyn: #no need to declare b
                self.new_one_uint(getbitsize(b),b, "b")
            self.docalculate(op, a, b, c)
        else:#sint
            self.new_one_sint(getbitsize(a),a, "a")
            if op not in bits and op not in binbit and op not in sins and op not in threeparm and op not in dyn: #no need to declare b
                self.new_one_sint(getbitsize(b),b, "b")
            self.s_docalculate(op, a, b, c)
        self.bottom()
        self.f.close()
        subprocess.call(["g++", self.name+".cpp", "-o", self.name]) #test cpp program
        if os.path.exists(self.name):
            subprocess.call(["./"+self.name])
            subprocess.call(["rm", self.name])
            self.completed = 1
    
    def getcompletedcount(self):
        return self.completed
