import unittest
from hypothesis import example, given, assume, settings, strategies as st
from hypothesis.strategies import text
import config
import test
import subprocess

class FuzzyTest(unittest.TestCase):
    def calc_fuzzy(self, size):
        @given(a=st.integers(min_value=0, max_value=10000), b=st.integers(min_value=0, max_value=10000))
        @settings(max_examples=size)
        def inner(a, b):
            self.fuzzyset.add((a,b))
        inner()
    def test_fuzzy(self):
        for a, b in self.fuzzyset:
            test.runtests.calc_variables(self, str(self.ts)+"/fuzzy","test"+ str(a) +"_"+''.join(str(ord(c)) for c in op)+"_" + str(b), op, a, b)

    def test_square(self, op, size):
        a = 1
        for _ in range(size):
            b = 1
            for _ in range(size):
                self.calc_variables(str(self.ts)+"/fuzzy","test"+ str(a) +"_"+''.join(str(ord(c)) for c in op)+"_"+str(b), op, a, b)
                b <<= 1
            a <<= 1

    def test_max(self, op, size):
        a = 1
        for _ in range(size):
            b = 1
            for _ in range(size):
                self.calc_variables(str(self.ts)+"/fuzzy","test"+ str(a) +"_"+''.join(str(ord(c)) for c in op)+"_"+str(b), op, a, b)
                b = (b << 1) + 1
            a = (a << 1) | 1

if __name__ == "__main__":
    t = test.runtests()
    subprocess.call(["mkdir", "testcases/"+str(t.ts)+"/fuzzy"])
    fuzzysize = int(input("number of fuzzy tests: "))
    op = input("enter operation: ")
    type = input("enter type: ")
    if op in config.list_two or op in config.list_bitwise:
        if type == "square":
            FuzzyTest.test_square(t, op, fuzzysize)
        elif type == "max":
            FuzzyTest.test_max(t, op, fuzzysize)
        else:
            print("invalid type")
    else:
        print("invalid operator")
    print("====================")
    t.printresult()