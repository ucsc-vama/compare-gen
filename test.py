import subprocess
import generator
from model_uint import *
from BruteTest import *
from RandomTest import *
from FuzzyTest import *
import config
from datetime import datetime
from math import * 

class runtests:

    def __init__(self):
        self.ts = datetime.timestamp(datetime.now())
        subprocess.call(["mkdir", "testcases/"+str(self.ts)])
        self.completed = 0
        self.count = 0

    def printresult(self):
        print("tests completed:", self.completed)
        print("tests count:", self.count)

    def calc_variables(self, folder, op, a, b=0, c=0):
        if op == "%" and b == 0: #division by zero
            return
        manual = generator.file(folder,"test"+''.join(str(ord(ch)) for ch in op)+"_" + str(a) +"_"+ str(b)+"_"+str(c))
        manual.runmanual(op,a,b,c)
        self.completed += manual.getcompletedcount()
        self.count += 1

    def createfolder(self):#not used
        subprocess.call(["mkdir", "testcases/"+str(self.ts)+"/brute"])
        subprocess.call(["mkdir", "testcases/"+str(self.ts)+"/manual"])
        subprocess.call(["mkdir", "testcases/"+str(self.ts)+"/random"])
        subprocess.call(["mkdir", "testcases/"+str(self.ts)+"/fuzzy"])

    def calc_manual(self, filename, op, a, b=0, c=0):
        self.calc_variables(str(self.ts)+"/manual", op, a, b, c)