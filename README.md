Compare gen
=================
This repo is designed to combine the functionality of [firrtl-operations](https://github.com/ucsc-vama/firrtl-operations/tree/main) and [firrtl-sig](https://github.com/ucsc-vama/firrtl-sig) to test the accuracy of each operation. Python program will generate a test case in C++ code. Compiling and running the c++ code will yield the accuracy test of U-int and S-int operations in firrtl-sig.

run test script:

    $ python test.py

NOTES:

* uint "add" and comparisons of different bit length cannot be calculated.
* uint "tail" should operate on n less than on equal to the bit width of e. however only works on less than.
* similarly, uint "head" does not work on n equal to 0.
* different bitlength operation doesnt work for "^", "|", "&", "<", ">", ">=", "<=", "=="
>>>
    UInt<2> a("0x2");
	UInt<1> b("0x1");
	assert((a|b) == UInt<2>("0x3"));
>>>
>>>
	UInt<2> a("0x2");
	UInt<1> b("0x1");
	assert((a&b) == UInt<2>("0x0"));
>>>