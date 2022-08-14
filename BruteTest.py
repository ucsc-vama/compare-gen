from math import *
from test import *

def getbitsize(var):
    if var == 0:
        return 1
    return ceil(log2(var+1))

# list_two = ["+", "-", "*", "<", "<=", ">", ">=", "==", "!=", "&", "|", "^", "cat", "/", "%"]
list_two = ["+", "-", "*", "cat", "/", "%"]
list_bitwise = ["pad", "shl", "shr", "<<", ">>"]
headtail = ["tail", "head"]
binbit = ["andr", "orr", "xorr"]
sins = ["~"]
threeparm = ["bits"]


class BruteTest:
    def testpossible(self, varsize):
        # for op in list_two:
        #     for i in range(0,varsize): #testing only after 8. change after fix
        #         for j in range(0,varsize):
        #             self.calc_variables(str(self.ts)+"/brute","test"+ str(i) + "_" + ''.join(str(ord(c)) for c in op) + "_" + str(j), op, i, j)
        # for op in list_bitwise:
        #     for i in range(0,varsize):
        #         for j in range(5):
        #             self.calc_variables(str(self.ts)+"/brute","test"+ str(i) + ''.join(str(ord(c)) for c in op) + str(j), op, i, j)
        for op in headtail:
            for i in range(0,varsize):
                isize = getbitsize(i)
                for j in range(0,isize):
                    self.calc_variables(str(self.ts)+"/brute","test"+ str(i) + "_" + op + "_" + str(j), op, i, j)
        # for op in binbit:
        #     for i in range(0,varsize):
        #         self.calc_variables(str(self.ts)+"/brute","test"+ op + "_" + str(i), op, i)
        # for op in sins:
        #     for i in range(0, varsize):
        #         self.calc_variables(str(self.ts)+"/brute","test"+ "~_"+str(i), op, i)
        # for op in threeparm:
        #     for i in range(1, varsize):
        #         isize = getbitsize(i)
        #         for h in range(1, isize):
        #             hsize = getbitsize(h)
        #             for l in range(1, hsize):
        #                 self.calc_variables(str(self.ts)+"/brute","test"+ "bits_"+str(i)+"_"+str(h)+"_"+str(l), op, i,h,l)

    def testsquare(self, varsize):
        for op in list_two:
            for i in range(varsize):
                j = 0
                while j < varsize:
                    j = (j << 1) | 1
                    self.calc_variables(str(self.ts)+"/brute","test"+ str(i) + ''.join(str(ord(c)) for c in op) + str(j), op, i, j)