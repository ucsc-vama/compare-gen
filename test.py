import subprocess
import generator

def populate_list(self, li, n, bitsize):
    for i in range(n):
        li.append(generator.file.new_uint(self, bitsize, generator.operation.randcreate(bitsize)))
    return li

def calc_all(self, li):
    for i in li:
        for j in li:
            generator.file.docalculate(self,"+", i, j)
            generator.file.docalculate(self,"-", i, j)
            generator.file.docalculate(self,"*", i, j)
            if j.bitsize < 64 and j.value > 0:
                generator.file.docalculate(self,"/", i, j)
                generator.file.docalculate(self,"%", i, j)

def calc_all_64(self, li):
    for i in li:
        for j in li:
            generator.file.docalculate(self,"+", i, j)
            generator.file.docalculate(self,"-", i, j)
            generator.file.docalculate(self,"*", i, j)
            
def testcase3(self):
    #simple random cases
    # li = []
    # li = populate_list(self, li, 3, 16)
    # calc_all(self, li)

    # li = []
    # li = populate_list(self, li, 3, 127)
    # calc_all(self, li)

    #custom cases
    li = []
    li.append(generator.file.new_uint(self, 1, 0x0))
    #li.append(generator.file.new_uint(self, 1, 0x1))
    li.append(generator.file.new_uint(self, 2, 0x2))
    #li.append(generator.file.new_uint(self, 2, 0x3))
    #li.append(generator.file.new_uint(self, 5, 0x11))
    calc_all(self, li)

    

if __name__=="__main__":
    subprocess.call(["rm", "Runner.cpp"])
    a = generator.file(testcase3)
    a.runprogram()