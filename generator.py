import sys
sys.path.insert(1, './firrtl-operations')
from my_uint import *

a = my_uint(2, 0x2)
b = my_uint(4, 0xa)
sum = a.uint_add(b)

def gen():
    print("test", sum.value)

if __name__=="__main__":
    gen()