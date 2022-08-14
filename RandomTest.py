from random import randint

class RandomTest:
    def calc_random(self,op, varsize=0):
        a = randint(0,varsize)#testing only 4 bits
        b = randint(0,varsize)
        self.calc_variables(str(self.ts)+"/random", "test"+str(a)+"_" + ''.join(str(ord(c)) for c in op)+"_" + str(b),op,a,b)