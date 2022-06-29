#include "./firrtl-sig/uint.h"
#include <iostream>
#include <assert.h>
#include <stdlib.h>
using namespace std;

int main() {

	UInt<32> u3606533266("0xd6f75492");
	UInt<32> u3979405317("0xed30e805");
	UInt<32> u3288418872("0xc4014a38");
	UInt<32> u2533430598("0x97011546");
	UInt<32> u3204968087("0xbf07ee97");
	UInt<32> u2721034488("0xa22fb0f8");
	UInt<32> u2747321151("0xa3c0cb3f");
	UInt<32> u2392293589("0x8e9780d5");
	UInt<32> u4223621359("0xfbbf58ef");
	UInt<32> u2520603637("0x963d5bf5");
	assert(~u2721034488 == UInt<32>("0x5dd04f07"));
	assert((u2721034488.andr()) == UInt<1>("0x0"));
	assert((u2721034488.orr()) == UInt<1>("0x1"));
	assert((u2721034488.xorr()) == UInt<1>("0x0"));
	assert(~u3979405317 == UInt<32>("0x12cf17fa"));
	assert((u3979405317.andr()) == UInt<1>("0x0"));
	assert((u3979405317.orr()) == UInt<1>("0x1"));
	assert((u3979405317.xorr()) == UInt<1>("0x0"));
	assert(~u2533430598 == UInt<32>("0x68feeab9"));
	assert((u2533430598.andr()) == UInt<1>("0x0"));
	assert((u2533430598.orr()) == UInt<1>("0x1"));
	assert((u2533430598.xorr()) == UInt<1>("0x0"));
	assert(~u4223621359 == UInt<32>("0x440a710"));
	assert((u4223621359.andr()) == UInt<1>("0x0"));
	assert((u4223621359.orr()) == UInt<1>("0x1"));
	assert((u4223621359.xorr()) == UInt<1>("0x0"));
	assert(~u3606533266 == UInt<32>("0x2908ab6d"));
	assert((u3606533266.andr()) == UInt<1>("0x0"));
	assert((u3606533266.orr()) == UInt<1>("0x1"));
	assert((u3606533266.xorr()) == UInt<1>("0x0"));
	assert(~u2392293589 == UInt<32>("0x71687f2a"));
	assert((u2392293589.andr()) == UInt<1>("0x0"));
	assert((u2392293589.orr()) == UInt<1>("0x1"));
	assert((u2392293589.xorr()) == UInt<1>("0x1"));
	assert(~u2520603637 == UInt<32>("0x69c2a40a"));
	assert((u2520603637.andr()) == UInt<1>("0x0"));
	assert((u2520603637.orr()) == UInt<1>("0x1"));
	assert((u2520603637.xorr()) == UInt<1>("0x0"));
	assert(~u3204968087 == UInt<32>("0x40f81168"));
	assert((u3204968087.andr()) == UInt<1>("0x0"));
	assert((u3204968087.orr()) == UInt<1>("0x1"));
	assert((u3204968087.xorr()) == UInt<1>("0x1"));
	assert(~u3288418872 == UInt<32>("0x3bfeb5c7"));
	assert((u3288418872.andr()) == UInt<1>("0x0"));
	assert((u3288418872.orr()) == UInt<1>("0x1"));
	assert((u3288418872.xorr()) == UInt<1>("0x0"));
	assert(~u2747321151 == UInt<32>("0x5c3f34c0"));
	assert((u2747321151.andr()) == UInt<1>("0x0"));
	assert((u2747321151.orr()) == UInt<1>("0x1"));
	assert((u2747321151.xorr()) == UInt<1>("0x1"));

	return 0;
}