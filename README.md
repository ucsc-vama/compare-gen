Compare gen
=================
This repo is designed to combine the functionality of [firrtl-operations](https://github.com/ucsc-vama/firrtl-operations/tree/main) and [firrtl-sig](https://github.com/ucsc-vama/firrtl-sig) to test the accuracy of each operation. Python program will generate a test case in C++ code. Compiling and running the c++ code will yield the accuracy test of U-int and S-int operations in firrtl-sig.


File structure:
```
├── Firrtl-sig
│	├── README.md
│	└── ...
└── Compare-gen
	├── README.md
	└── ...
```
Must have firrtl-sig cloned in the same level as compare-gen

run bruteforce test:
```
    $ python3 BruteTest.py -t sint -m 3 &> outfile.txt
```

NOTES: