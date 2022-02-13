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

	assert(u0+u0 == UInt<17>("0x195fc"));
	assert(u0+u1 == UInt<17>("0x189bc"));
	assert(u1+u0 == UInt<17>("0x189bc"));
	assert(u1+u1 == UInt<17>("0x17d7c"));
	assert(u2+u2 == UInt<65>("0x1c57ab69ff1661f90"));
	assert(u2+u3 == UInt<65>("0x11280af33351c486f"));
	assert(u3+u2 == UInt<65>("0x11280af33351c486f"));
	assert(u3+u3 == UInt<65>("0x5f86a7c678d2714e"));

	assert(u0-u1 == UInt<17>("0xc40"));
	assert(u1-u0 == UInt<17>("0x1f3c0"));
	assert(u2-u3 == UInt<65>("0xb2fa076cbc49d721"));
	assert(u3-u2 == UInt<65>("0x14d05f89343b628df"));

	assert(u0*u1 == UInt<32>("0x973f2c84"));
	assert(u1*u0 == UInt<32>("0x973f2c84"));
	assert(u2*u3 == UInt<128>("0x2a4dc44ce497c914d9d3df0ec14b0b78"));
	assert(u3*u2 == UInt<128>("0x2a4dc44ce497c914d9d3df0ec14b0b78"));

	assert(u0/u1 == UInt<16>("0x1"));
	assert(u1/u0 == UInt<16>("0x0"));
	assert(u2/u3 == UInt<64>("0x4"));
	assert(u3/u2 == UInt<64>("0x0"));

	assert(u0%u1 == UInt<16>("0xc40"));
	assert(u1%u0 == UInt<16>("0xbebe"));
	assert(u2%u3 == UInt<64>("0x23b00bc3070e2d2c"));
	assert(u3%u2 == UInt<64>("0x2fc353e33c6938a7"));

	bool result;
	result = u0<u1;
	assert(0==result);
	result = u1<u0;
	assert(1==result);
	result = u2<u3;
	assert(0==result);
	result = u3<u2;
	assert(1==result);

	result = u0<=u1;
	assert(0==result);
	result = u1<=u0;
	assert(1==result);
	result = u2<=u3;
	assert(0==result);
	result = u3<=u2;
	assert(1==result);

	result = u0>u1;
	assert(1==result);
	result = u1>u0;
	assert(0==result);
	result = u2>u3;
	assert(1==result);
	result = u3>u2;
	assert(0==result);

	result = u0>=u1;
	assert(1==result);
	result = u1>=u0;
	assert(0==result);
	result = u2>=u3;
	assert(1==result);
	result = u3>=u2;
	assert(0==result);

	return 0;
}