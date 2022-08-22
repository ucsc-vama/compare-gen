import unittest
from hypothesis import example, given, assume, settings, strategies as st
from hypothesis.strategies import text
import config
import test
import subprocess

def encode(input_string):
    count = 1
    prev = ""
    lst = []
    character = ""
    entry = None
    for character in input_string:
        if character != prev:
            if prev:
                entry = (prev, count)
                lst.append(entry)
            count = 1
            prev = character
        else:
            count += 1
    entry = (character, count)
    lst.append(entry)
    return lst


def decode(lst):
    q = ""
    for character, count in lst:
        q += character * count
    return q

@given(a=st.integers(min_value=0, max_value=10000), b=st.integers(min_value=0, max_value=10000))
@settings(max_examples=5)
def hi(a,b):
    print((a,b))

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

if __name__ == "__main__":
    t = test.runtests()
    subprocess.call(["mkdir", "testcases/"+str(t.ts)+"/fuzzy"])
    fuzzysize = int(input("number of fuzzy tests: "))
    op = input("enter operation: ")
    if op in config.list_two:
        FuzzyTest.calc_fuzzy(t, fuzzysize)
        FuzzyTest.test_fuzzy(t)
    else:
        print("invalid operator")
    print("====================")
    t.printresult()