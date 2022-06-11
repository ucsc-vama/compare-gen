#include "./firrtl-sig/uint.h"
#include <iostream>
#include <assert.h>
#include <stdlib.h>
using namespace std;

int main() {

	UInt<1> u1("0x1");
	UInt<2> u2("0x2");
	UInt<2> u3("0x3");
	UInt<3> u4("0x4");
	UInt<3> u5("0x5");
	UInt<3> u6("0x6");
	UInt<3> u7("0x7");
	UInt<4> u8("0x8");
	UInt<4> u9("0x9");
	UInt<4> u10("0xa");
	UInt<4> u11("0xb");
	UInt<4> u12("0xc");
	UInt<4> u13("0xd");
	UInt<4> u14("0xe");
	UInt<4> u15("0xf");
	UInt<5> u16("0x10");

    /*
    uint add of different bit length cannot be calculated. slight issue on firrtl sig
    */
	// assert((u8+u16) == UInt<6>("0x18"));

    /*
    unable to compare numbers of different bit length
    */
    // cout << (u1>u2) << endl;

}