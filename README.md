Compare gen
=================
This repo is designed to combine the functionality of [firrtl-operations](https://github.com/ucsc-vama/firrtl-operations/tree/main) and [firrtl-sig](https://github.com/ucsc-vama/firrtl-sig) to test the accuracy of each operation. Python program will generate a test case in C++ code. Compiling and running the c++ code will yield the accuracy test of U-int and S-int operations in firrtl-sig.

run test script:

    $ python test.py

NOTES:

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

* bit extraction operation dont work when lower and higher is equal