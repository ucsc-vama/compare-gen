import subprocess
import generator

def testcase3(self):
    li = []
    li.append(generator.file.new_uint(self, 16, generator.operation.randcreate(16)))
    li.append(generator.file.new_uint(self, 16, generator.operation.randcreate(16)))
    li.append(generator.file.new_uint(self, 16, generator.operation.randcreate(16)))
    li.append(generator.file.new_uint(self, 16, generator.operation.randcreate(16)))
    li.append(generator.file.new_uint(self, 16, generator.operation.randcreate(16)))
    li.append(generator.file.new_uint(self, 16, generator.operation.randcreate(16)))
    for i in range(0, 6):
        for j in range(0, 6):
            generator.file.docalculate(self,"+", li[i], li[j])
    for i in range(0, 6):
        for j in range(0, 6):
            generator.file.docalculate(self,"-", li[i], li[j])
    for i in range(0, 6):
        for j in range(0, 6):
            generator.file.docalculate(self,"*", li[i], li[j])
    for i in range(0, 6):
        for j in range(0, 6):
            generator.file.docalculate(self,"/", li[i], li[j])
    for i in range(0, 6):
        for j in range(0, 6):
            generator.file.docalculate(self,"%", li[i], li[j])


if __name__=="__main__":
    subprocess.call(["rm", "Runner.cpp"])
    a = generator.file(testcase3)
    a.runprogram()