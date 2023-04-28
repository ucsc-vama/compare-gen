from math import *

def getbitsize(var):
    if var == 0:
        return 1
    return ceil(log2(var+1))

# list_two = ["+", "-", "*", "<", "<=", ">", ">=", "==", "!=", "&", "|", "^", "cat", "/", "%"]
# list_two = ["+", "-", "*", "cat", "==", "!=", "/", "%", "&", "|", "^"]
list_two = ["+", "-", "*", "cat", "/", "%", "&", "|", "^"]
list_bitwise = ["pad", "shl", "shr", "dshl", "dshr"]
headtail = ["tail", "head"]
binbit = ["andr", "orr", "xorr"]
sins = ["~"]
threeparm = ["bits"]

