Compare gen
=================
This repo is designed to combine the functionality of [firrtl-operations](https://github.com/ucsc-vama/firrtl-operations/tree/main) and [firrtl-sig](https://github.com/ucsc-vama/firrtl-sig) to test the accuracy of each operation. Python program will generate a test case in C++ code. Compiling and running the c++ code will yield the accuracy test of U-int and S-int operations in firrtl-sig.

First run generator:

    $ python generator.py

Notes:
* firrtl sig outputs signed bit 1 when subtracting 64bit or 128bit
```
	UInt<64> u5("0xa3901ba6fe91832a");
	cout << u5-u5 << endl;
	//output: 0x10000000000000000<U65>
```