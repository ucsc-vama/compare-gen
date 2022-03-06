#include "./firrtl-sig/uint.h"
#include<iostream>
#include <assert.h>
#include <stdlib.h>
using namespace std;

int main() {

	UInt<16> ua("0xcafe");
	UInt<16> ub("0xbebe");
	assert(ua+ub == UInt<17>("0x189bc"));
	assert(ua-ub == UInt<17>("0xc40"));
	assert(ua*ub == UInt<32>("0x973f2c84"));
	assert(ua/ub == UInt<16>("0x1"));
	assert(ua%ub == UInt<16>("0xc40"));
	assert(0 == (ua<ub));
	assert(0 == (ua<=ub));
	assert(1 == (ua>ub));
	assert(1 == (ua>=ub));
	assert(0 == (ua==ub));
	assert(1 == (ua!=ub));

	assert(ua.pad<4>() == UInt<16>("0xcafe"));
	assert(ua.shl<4>() == UInt<20>("0xcafe0"));
	assert(ua.shr<4>() == UInt<12>("0xcaf"));

	return 0;
}