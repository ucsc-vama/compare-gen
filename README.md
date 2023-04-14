Compare gen
=================
This repo is designed to combine the functionality of [firrtl-operations](https://github.com/ucsc-vama/firrtl-operations/tree/main) and [firrtl-sig](https://github.com/ucsc-vama/firrtl-sig) to test the accuracy of each operation. Python program will generate a test case in C++ code. Compiling and running the c++ code will yield the accuracy test of U-int and S-int operations in firrtl-sig.

run bruteforce test:
```
    $ python3 BruteTest.py -t sint -s 3 &> outfile.txt
```

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

* lt/gt incorrrect result?
```
	SInt<4> a("0x9");
	SInt<4> b("0x1");
	cout << (a<b) << endl;
	// should be true
	// but prints false
```

* comparison issue
```
  SInt<2> a(0x3);
  cout << (a >> UInt<2>("0x2"))  << endl;
  cout << SInt<2>(0x3) << endl;
	cout << ((a >> UInt<2>("0x2")) == SInt<2>(0x3)) << endl;
```

* head operation cannot run when n=0
