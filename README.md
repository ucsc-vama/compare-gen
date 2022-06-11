Compare gen
=================
This repo is designed to combine the functionality of [firrtl-operations](https://github.com/ucsc-vama/firrtl-operations/tree/main) and [firrtl-sig](https://github.com/ucsc-vama/firrtl-sig) to test the accuracy of each operation. Python program will generate a test case in C++ code. Compiling and running the c++ code will yield the accuracy test of U-int and S-int operations in firrtl-sig.

run test script:

    $ python test.py

NOTES:

* doing "add" with numbers less than 3 bit generate boolean issues
>>>
	UInt<2> u3("0x3");
	UInt<3> u4("0x4");
	cout << (u3+u4) << endl;
>>>
* shift right results in error if n is greater than bitlength. "If n is greater than or
equal to the bit-width of e, the resulting value will be zero for unsigned types and the sign
bit for signed types. n must be non-negative."
* dynamic shift by bits of length greater than 4
>>>
    cout << (u8 << UInt<5>("0x1f")) << endl;
>>>
* uints of different bit length cannot be calculated. slight issue on firrtl sig (fixed?)
* test creates random values and will therefore have slight chance of error when two equal numbers were generated by accident