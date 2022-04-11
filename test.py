import subprocess
import generator

def populate_list(self, n, bitsize):
    li = []
    for i in range(n):
        li.append(generator.file.new_uint(self, bitsize, generator.operation.randcreate(bitsize)))
    return li

def loop_calc(self, li):
    for i in li:
        for j in li:
            generator.file.docalculate(self,"+", i, j)

def testcase3(self):
    li = populate_list(self, 3, 16)
    loop_calc(self, li)

    li = populate_list(self, 3, 64)
    loop_calc(self, li)

if __name__=="__main__":
    subprocess.call(["rm", "Runner.cpp"])
    a = generator.file(testcase3)
    a.runprogram()