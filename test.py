import subprocess
import generator
import subprocess
import os.path
import sys
sys.path.insert(1, '/firrtl-operations/')
import uint
from BruteTest import *
from RandomTest import *
import config
from datetime import datetime
from math import * 

class runtests:

    def __init__(self):
        self.ts = datetime.timestamp(datetime.now())
        subprocess.call(["mkdir", "-p", "testcases/"+str(self.ts)+"/"])
        self.completed = 0
        self.count = 0
        self.clear = False
        self.type = "uint"
        print("testcases/"+str(self.ts)+"/")

    def printresult(self):
        print("tests completed:", self.completed)
        print("tests count:", self.count)

    def calc_variables(self, op, a, b=0, c=0):
        if (op == "%" or op == "/") and b == 0: #division by zero
            return
        manual = generator.file(str(self.ts),"test"+str(self.type)+''.join(str(ord(ch)) for ch in op)+"_" + str(a) +"_"+ str(b)+"_"+str(c))
        manual.runmanual(self.type,op,a,b,c)
        if self.clear and os.path.exists(manual.name+".cpp"):
            subprocess.call(["rm", manual.name+".cpp"])
        self.completed += manual.getcompletedcount()
        self.count += 1

    def createfolder(self):#not used
        subprocess.call(["mkdir", "testcases/"+str(self.ts)+"/brute"])
        subprocess.call(["mkdir", "testcases/"+str(self.ts)+"/manual"])
        subprocess.call(["mkdir", "testcases/"+str(self.ts)+"/random"])
        subprocess.call(["mkdir", "testcases/"+str(self.ts)+"/fuzzy"])

    def calc_manual(self, op, a, b=0, c=0):
        self.calc_variables(str(self.ts), op, a, b, c)