#include "./firrtl-sig/uint.h"
#include<iostream>
#include <assert.h>
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

	UInt<64> u5("0xa3901ba6fe91832a");
	cout << u5-u5 << endl;
	//output: 0x10000000000000000<U65>

	return 0;
}