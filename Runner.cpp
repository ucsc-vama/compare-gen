#include "./firrtl-sig/uint.h"
#include<iostream>
#include <assert.h>
#include <stdlib.h>
using namespace std;

int main() {

	UInt<16> ua("0xcafe");
	UInt<16> ub("0xbebe");
	assert(ua+ub == UInt<17>("0x189bc"));
	assert(0 == (ua==ub));
	assert(ua.shr<4>() == UInt<12>("0xcaf"));

	return 0;
}