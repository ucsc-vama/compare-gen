#include "./firrtl-sig/uint.h"
#include <iostream>
#include <assert.h>
#include <stdlib.h>
using namespace std;

int main() {

	UInt<4> u8("0x8");
	UInt<4> u9("0x9");
	UInt<4> u10("0xa");
	UInt<4> u11("0xb");
	UInt<4> u12("0xc");
	UInt<4> u13("0xd");
	UInt<4> u14("0xe");
	UInt<4> u15("0xf");
	assert((u8.bits<1,0>()) == UInt<2>("0x0"));
	assert((u8.bits<2,0>()) == UInt<3>("0x0"));
	assert((u8.bits<2,1>()) == UInt<2>("0x0"));
	assert((u8.bits<3,0>()) == UInt<4>("0x8"));
	assert((u8.bits<3,1>()) == UInt<3>("0x4"));
	assert((u8.bits<3,2>()) == UInt<2>("0x2"));
	assert((u9.bits<1,0>()) == UInt<2>("0x1"));
	assert((u9.bits<2,0>()) == UInt<3>("0x1"));
	assert((u9.bits<2,1>()) == UInt<2>("0x0"));
	assert((u9.bits<3,0>()) == UInt<4>("0x9"));
	assert((u9.bits<3,1>()) == UInt<3>("0x4"));
	assert((u9.bits<3,2>()) == UInt<2>("0x2"));
	assert((u10.bits<1,0>()) == UInt<2>("0x2"));
	assert((u10.bits<2,0>()) == UInt<3>("0x2"));
	assert((u10.bits<2,1>()) == UInt<2>("0x1"));
	assert((u10.bits<3,0>()) == UInt<4>("0xa"));
	assert((u10.bits<3,1>()) == UInt<3>("0x5"));
	assert((u10.bits<3,2>()) == UInt<2>("0x2"));
	assert((u11.bits<1,0>()) == UInt<2>("0x3"));
	assert((u11.bits<2,0>()) == UInt<3>("0x3"));
	assert((u11.bits<2,1>()) == UInt<2>("0x1"));
	assert((u11.bits<3,0>()) == UInt<4>("0xb"));
	assert((u11.bits<3,1>()) == UInt<3>("0x5"));
	assert((u11.bits<3,2>()) == UInt<2>("0x2"));
	assert((u12.bits<1,0>()) == UInt<2>("0x0"));
	assert((u12.bits<2,0>()) == UInt<3>("0x4"));
	assert((u12.bits<2,1>()) == UInt<2>("0x2"));
	assert((u12.bits<3,0>()) == UInt<4>("0xc"));
	assert((u12.bits<3,1>()) == UInt<3>("0x6"));
	assert((u12.bits<3,2>()) == UInt<2>("0x3"));
	assert((u13.bits<1,0>()) == UInt<2>("0x1"));
	assert((u13.bits<2,0>()) == UInt<3>("0x5"));
	assert((u13.bits<2,1>()) == UInt<2>("0x2"));
	assert((u13.bits<3,0>()) == UInt<4>("0xd"));
	assert((u13.bits<3,1>()) == UInt<3>("0x6"));
	assert((u13.bits<3,2>()) == UInt<2>("0x3"));
	assert((u14.bits<1,0>()) == UInt<2>("0x2"));
	assert((u14.bits<2,0>()) == UInt<3>("0x6"));
	assert((u14.bits<2,1>()) == UInt<2>("0x3"));
	assert((u14.bits<3,0>()) == UInt<4>("0xe"));
	assert((u14.bits<3,1>()) == UInt<3>("0x7"));
	assert((u14.bits<3,2>()) == UInt<2>("0x3"));
	assert((u15.bits<1,0>()) == UInt<2>("0x3"));
	assert((u15.bits<2,0>()) == UInt<3>("0x7"));
	assert((u15.bits<2,1>()) == UInt<2>("0x3"));
	assert((u15.bits<3,0>()) == UInt<4>("0xf"));
	assert((u15.bits<3,1>()) == UInt<3>("0x7"));
	assert((u15.bits<3,2>()) == UInt<2>("0x3"));

	return 0;
}