import unittest
from hypothesis import example, given, assume, strategies as st
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
    @given(a=st.integers(min_value=0, max_value=10000), b=st.integers(min_value=0, max_value=10000))
    def calc_fuzzy(self,a, b):
        self.fuzzylist.append((a,b))

@given(min=st.integers(min_value=1, max_value=10),max=st.integers(min_value=1, max_value=10))
# @example(n=1)
def test_example(hi,min, max):
    print(hi)
    print(min, max)
    # assert expected(n)  == real(n)

if __name__ == "__main__":
    # unittest.main()
    test_example("hekki")