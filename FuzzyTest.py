import unittest
from hypothesis import example, given, assume, settings, strategies as st
from hypothesis.strategies import text

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

class FuzzyTest(unittest.TestCase):
    def calc_fuzzy(self, size):

        @given(a=st.integers(min_value=0, max_value=10000), b=st.integers(min_value=0, max_value=10000))
        @settings(max_examples=size)
        def inner(a, b):
            self.fuzzyset.add((a,b))

        inner()

def test_example(size):
    cre = set()

    @given(a=st.integers(min_value=0, max_value=10000), b=st.integers(min_value=0, max_value=10000))
    @settings(max_examples=size)
    def inner(a, b):
        cre.add((a,b))

    inner()

    inner()
    print(cre)

if __name__ == "__main__":
    # unittest.main()
    test_example(5)