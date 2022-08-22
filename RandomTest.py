from random import randint
import test
import subprocess

class RandomTest:

    def __init__(self):
        self.values = set()

    def findrandoms(self, varsize=0):
        self.values.add((randint(0,varsize), randint(0,varsize)))

    def calc_random(self,op, values):
        self.calc_variables(str(self.ts)+"/random", "test"+str(values[0])+"_" + ''.join(str(ord(c)) for c in op)+"_" + str(values[1]),op,values[0],values[1])

if __name__=="__main__":
    t = test.runtests()
    subprocess.call(["mkdir", "testcases/"+str(t.ts)+"/random"])
    randomsize = int(input("number of random tests: ")) or 0
    if randomsize > 0:
        op = input("operation: ")
        maxsize = int(input("max bitlength: "))
        varsize = (1<<maxsize) - 1
        R = RandomTest()
        while len(R.values) < randomsize:
            R.findrandoms(varsize)
        R.values = list(R.values)
        for i in range(randomsize):
            RandomTest.calc_random(t,op, R.values[i])
    print("====================")
    t.printresult()