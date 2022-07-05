#include "./firrtl-sig/uint.h"
#include <iostream>
#include <assert.h>
#include <stdlib.h>
using namespace std;

int main() {

	UInt<32> u3993604093("0xee098ffd");
	UInt<32> u4189142192("0xf9b13cb0");
	UInt<32> u3172390119("0xbd16d4e7");
	UInt<32> u3901049547("0xe8854acb");
	UInt<32> u3014077832("0xb3a72d88");
	UInt<32> u3941325007("0xeaebd8cf");
	UInt<32> u2570651659("0x9939080b");
	UInt<32> u2769724894("0xa516a5de");
	UInt<32> u3142812429("0xbb53830d");
	UInt<32> u3280079235("0xc3820983");
	assert(~u3280079235 == UInt<32>("0x3c7df67c"));
	assert((u3280079235.andr()) == UInt<1>("0x0"));
	assert((u3280079235.orr()) == UInt<1>("0x1"));
	assert((u3280079235.xorr()) == UInt<1>("0x1"));
	assert(~u3172390119 == UInt<32>("0x42e92b18"));
	assert((u3172390119.andr()) == UInt<1>("0x0"));
	assert((u3172390119.orr()) == UInt<1>("0x1"));
	assert((u3172390119.xorr()) == UInt<1>("0x1"));
	assert(~u3014077832 == UInt<32>("0x4c58d277"));
	assert((u3014077832.andr()) == UInt<1>("0x0"));
	assert((u3014077832.orr()) == UInt<1>("0x1"));
	assert((u3014077832.xorr()) == UInt<1>("0x0"));
	assert(~u3901049547 == UInt<32>("0x177ab534"));
	assert((u3901049547.andr()) == UInt<1>("0x0"));
	assert((u3901049547.orr()) == UInt<1>("0x1"));
	assert((u3901049547.xorr()) == UInt<1>("0x1"));
	assert(~u2570651659 == UInt<32>("0x66c6f7f4"));
	assert((u2570651659.andr()) == UInt<1>("0x0"));
	assert((u2570651659.orr()) == UInt<1>("0x1"));
	assert((u2570651659.xorr()) == UInt<1>("0x0"));
	assert(~u3142812429 == UInt<32>("0x44ac7cf2"));
	assert((u3142812429.andr()) == UInt<1>("0x0"));
	assert((u3142812429.orr()) == UInt<1>("0x1"));
	assert((u3142812429.xorr()) == UInt<1>("0x0"));
	assert(~u3941325007 == UInt<32>("0x15142730"));
	assert((u3941325007.andr()) == UInt<1>("0x0"));
	assert((u3941325007.orr()) == UInt<1>("0x1"));
	assert((u3941325007.xorr()) == UInt<1>("0x1"));
	assert(~u4189142192 == UInt<32>("0x64ec34f"));
	assert((u4189142192.andr()) == UInt<1>("0x0"));
	assert((u4189142192.orr()) == UInt<1>("0x1"));
	assert((u4189142192.xorr()) == UInt<1>("0x1"));
	assert(~u3993604093 == UInt<32>("0x11f67002"));
	assert((u3993604093.andr()) == UInt<1>("0x0"));
	assert((u3993604093.orr()) == UInt<1>("0x1"));
	assert((u3993604093.xorr()) == UInt<1>("0x0"));
	assert(~u2769724894 == UInt<32>("0x5ae95a21"));
	assert((u2769724894.andr()) == UInt<1>("0x0"));
	assert((u2769724894.orr()) == UInt<1>("0x1"));
	assert((u2769724894.xorr()) == UInt<1>("0x1"));

	return 0;
}