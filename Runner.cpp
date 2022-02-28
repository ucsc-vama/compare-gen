#include "./firrtl-sig/uint.h"
#include<iostream>
#include <assert.h>
#include <stdlib.h>
using namespace std;

int main() {
	UInt<16> u0("0xcafe");
	UInt<16> u1("0xbebe");
	UInt<64> u2("0xe2bd5b4ff8b30fc8");
	UInt<64> u3("0x2fc353e33c6938a7");

	assert(u0+u1 == UInt<17>("0x189bc"));
	assert(u0-u1 == UInt<17>("0xc40"));
	assert(u0*u1 == UInt<32>("0x973f2c84"));
	assert(u0/u1 == UInt<16>("0x1"));
	assert(u0%u1 == UInt<16>("0xc40"));

	assert(0==(u2<u3));
	assert(0==(u2<=u3));
	assert(1==(u2>u3));
	assert(1==(u2>=u3));
	assert(0==(u2==u3));
	assert(1==(u2!=u3));

	return 0;
}