#include "./firrtl-sig/uint.h"
#include <iostream>
#include <assert.h>
#include <stdlib.h>
using namespace std;

int main() {

	UInt<32> u3547027185("0xd36b56f1");
	UInt<32> u3081748491("0xb7afc00b");
	UInt<32> u3769359764("0xe0abdd94");
	UInt<32> u2508825829("0x9589a4e5");
	UInt<32> u2206936831("0x838b2eff");
	UInt<32> u3377928164("0xc95717e4");
	UInt<32> u2700165567("0xa0f141bf");
	UInt<32> u3606513150("0xd6f705fe");
	UInt<32> u2698389776("0xa0d62910");
	UInt<32> u2281664212("0x87ff6ed4");
	assert(~u3377928164 == UInt<32>("0x36a8e81b"));
	assert((u3377928164.andr()) == UInt<1>("0x0"));
	assert((u3377928164.orr()) == UInt<1>("0x1"));
	assert((u3377928164.xorr()) == UInt<1>("0x1"));
	assert(~u2508825829 == UInt<32>("0x6a765b1a"));
	assert((u2508825829.andr()) == UInt<1>("0x0"));
	assert((u2508825829.orr()) == UInt<1>("0x1"));
	assert((u2508825829.xorr()) == UInt<1>("0x1"));
	assert(~u2700165567 == UInt<32>("0x5f0ebe40"));
	assert((u2700165567.andr()) == UInt<1>("0x0"));
	assert((u2700165567.orr()) == UInt<1>("0x1"));
	assert((u2700165567.xorr()) == UInt<1>("0x0"));
	assert(~u3081748491 == UInt<32>("0x48503ff4"));
	assert((u3081748491.andr()) == UInt<1>("0x0"));
	assert((u3081748491.orr()) == UInt<1>("0x1"));
	assert((u3081748491.xorr()) == UInt<1>("0x1"));
	assert(~u2698389776 == UInt<32>("0x5f29d6ef"));
	assert((u2698389776.andr()) == UInt<1>("0x0"));
	assert((u2698389776.orr()) == UInt<1>("0x1"));
	assert((u2698389776.xorr()) == UInt<1>("0x1"));
	assert(~u3547027185 == UInt<32>("0x2c94a90e"));
	assert((u3547027185.andr()) == UInt<1>("0x0"));
	assert((u3547027185.orr()) == UInt<1>("0x1"));
	assert((u3547027185.xorr()) == UInt<1>("0x1"));
	assert(~u3769359764 == UInt<32>("0x1f54226b"));
	assert((u3769359764.andr()) == UInt<1>("0x0"));
	assert((u3769359764.orr()) == UInt<1>("0x1"));
	assert((u3769359764.xorr()) == UInt<1>("0x1"));
	assert(~u2281664212 == UInt<32>("0x7800912b"));
	assert((u2281664212.andr()) == UInt<1>("0x0"));
	assert((u2281664212.orr()) == UInt<1>("0x1"));
	assert((u2281664212.xorr()) == UInt<1>("0x1"));
	assert(~u3606513150 == UInt<32>("0x2908fa01"));
	assert((u3606513150.andr()) == UInt<1>("0x0"));
	assert((u3606513150.orr()) == UInt<1>("0x1"));
	assert((u3606513150.xorr()) == UInt<1>("0x1"));
	assert(~u2206936831 == UInt<32>("0x7c74d100"));
	assert((u2206936831.andr()) == UInt<1>("0x0"));
	assert((u2206936831.orr()) == UInt<1>("0x1"));
	assert((u2206936831.xorr()) == UInt<1>("0x1"));

	return 0;
}