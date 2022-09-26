import unittest
from hypothesis import example, given, assume, settings, strategies as st
from hypothesis.strategies import text
import config
import test
import subprocess
import getopt, sys

class FuzzyTest(unittest.TestCase):
    def calc_fuzzy(self, size):
        @given(a=st.integers(min_value=0, max_value=10000), b=st.integers(min_value=0, max_value=10000))
        @settings(max_examples=size)
        def inner(a, b):
            self.fuzzyset.add((a,b))
        inner()
    def test_fuzzy(self):
        for a, b in self.fuzzyset:
            test.runtests.calc_variables(self, str(self.ts)+"/fuzzy", op, a, b)

    def test_square(self, op, size):
        a = 1
        for _ in range(size):
            b = 1
            for _ in range(size):
                self.calc_variables(str(self.ts)+"/fuzzy", op, a, b)
                b <<= 1
            a <<= 1

    def test_max(self, op, size):
        a = 1
        for _ in range(size):
            b = 1
            for _ in range(size):
                self.calc_variables(str(self.ts)+"/fuzzy", op, a, b)
                b = (b << 1) + 1
            a = (a << 1) | 1

if __name__ == "__main__":
    t = test.runtests()
    subprocess.call(["mkdir", "testcases/"+str(t.ts)+"/fuzzy"])

    arglist = sys.argv[1:]
    options = "f:o:h"
    fuzzysize = 0
    op = "+"
    type = "square"
    long_options = ["fuzzysize=", "help"]
    maxbit = 1
    try:
        arguments, values = getopt.getopt(arglist, options, long_options)
        for currentArgument, currentValue in arguments:
            if currentArgument in ("-f", "--fuzzysize"):
                fuzzysize = int(currentValue)
            elif currentArgument in ("-o", "--operator"):
                op = currentValue
            elif currentArgument in ("-h", "--help"):
                print("usage: FuzzyTest.py -s <max value>")
                sys.exit()
    except getopt.error as err:
        print (str(err))

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