from math import *
import test
import config
import subprocess
import threading

class BruteTest:

    def testpossible(self, varsize):
        for op in config.list_two:
            for i in range(0,varsize): #testing only after 8. change after fix
                for j in range(0,varsize):
                    self.calc_variables(str(self.ts)+"/brute","test"+ str(i) + "_" + ''.join(str(ord(c)) for c in op) + "_" + str(j), op, i, j)
        for op in config.list_bitwise:
            for i in range(0,varsize):
                for j in range(5):
                    self.calc_variables(str(self.ts)+"/brute","test"+ str(i) + ''.join(str(ord(c)) for c in op) + str(j), op, i, j)
        for op in config.headtail:
            for i in range(0,varsize):
                isize = config.getbitsize(i)
                for j in range(0,isize):
                    self.calc_variables(str(self.ts)+"/brute","test"+ str(i) + "_" + op + "_" + str(j), op, i, j)
        for op in config.binbit:
            for i in range(0,varsize):
                self.calc_variables(str(self.ts)+"/brute","test"+ op + "_" + str(i), op, i)
        for op in config.sins:
            for i in range(0, varsize):
                self.calc_variables(str(self.ts)+"/brute","test"+ "~_"+str(i), op, i)

    def testthreeparm(self, varsize):
        for op in config.threeparm:
            for i in range(1, varsize):
                isize = config.getbitsize(i)
                for h in range(1, isize):
                    hsize = config.getbitsize(h)
                    for l in range(1, hsize):
                        self.calc_variables(str(self.ts)+"/brute","test"+ "bits_"+str(i)+"_"+str(h)+"_"+str(l), op, i,h,l)

    def testsquare(self, varsize):
        for op in config.list_two:
            for i in range(varsize):
                j = 0
                while j < varsize:
                    j = (j << 1) | 1
                    self.calc_variables(str(self.ts)+"/brute","test"+ str(i) + ''.join(str(ord(c)) for c in op) + str(j), op, i, j)

def print_cube(num):
    # function to print cube of given num
    print("Cube: {}" .format(num * num * num))

def print_square(num):
    # function to print square of given num
    print("Square: {}" .format(num * num))

if __name__=="__main__":
    t = test.runtests()
    subprocess.call(["mkdir", "testcases/"+str(t.ts)+"/brute"])
    upperlimit = int(input("max bitlength: "))
    t1 = threading.Thread(target=BruteTest.testpossible, args=(t, upperlimit,))
    t2 = threading.Thread(target=BruteTest.testthreeparm, args=(t, upperlimit,))
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    # BruteTest.testpossible(t,upperlimit)
    print("====================")
    t.printresult()