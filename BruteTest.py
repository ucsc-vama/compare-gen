from math import *
from test import *
import settings

class BruteTest:

    def testpossible(self, varsize):
        for op in settings.list_two:
            for i in range(0,varsize): #testing only after 8. change after fix
                for j in range(0,varsize):
                    self.calc_variables(str(self.ts)+"/brute","test"+ str(i) + "_" + ''.join(str(ord(c)) for c in op) + "_" + str(j), op, i, j)
        for op in settings.list_bitwise:
            for i in range(0,varsize):
                for j in range(5):
                    self.calc_variables(str(self.ts)+"/brute","test"+ str(i) + ''.join(str(ord(c)) for c in op) + str(j), op, i, j)
        for op in settings.headtail:
            for i in range(0,varsize):
                isize = settings.getbitsize(i)
                for j in range(0,isize):
                    self.calc_variables(str(self.ts)+"/brute","test"+ str(i) + "_" + op + "_" + str(j), op, i, j)
        for op in settings.binbit:
            for i in range(0,varsize):
                self.calc_variables(str(self.ts)+"/brute","test"+ op + "_" + str(i), op, i)
        for op in settings.sins:
            for i in range(0, varsize):
                self.calc_variables(str(self.ts)+"/brute","test"+ "~_"+str(i), op, i)
        for op in settings.threeparm:
            for i in range(1, varsize):
                isize = settings.getbitsize(i)
                for h in range(1, isize):
                    hsize = settings.getbitsize(h)
                    for l in range(1, hsize):
                        self.calc_variables(str(self.ts)+"/brute","test"+ "bits_"+str(i)+"_"+str(h)+"_"+str(l), op, i,h,l)

    def testsquare(self, varsize):
        for op in settings.list_two:
            for i in range(varsize):
                j = 0
                while j < varsize:
                    j = (j << 1) | 1
                    self.calc_variables(str(self.ts)+"/brute","test"+ str(i) + ''.join(str(ord(c)) for c in op) + str(j), op, i, j)