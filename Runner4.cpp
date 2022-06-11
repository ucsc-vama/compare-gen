#include "./firrtl-sig/uint.h"
#include <iostream>
#include <assert.h>
#include <stdlib.h>
using namespace std;

int main() {

	UInt<32> u4103589442("0xf497ce42");
	UInt<32> u2386756833("0x8e4304e1");
	UInt<32> u3814238324("0xe358a874");
	UInt<32> u3129991641("0xba8fe1d9");
	UInt<32> u2762064974("0xa4a1c44e");
	UInt<32> u2810989472("0xa78c4ba0");
	UInt<32> u3110131838("0xb960d87e");
	UInt<32> u3670823460("0xdacc5224");
	UInt<32> u3745721174("0xdf432b56");
	UInt<32> u3973165845("0xecd1b315");
	assert(~u2810989472 == UInt<32>("0x5873b45f"));
	assert((u2810989472.andr()) == UInt<1>("0x0"));
	assert((u2810989472.orr()) == UInt<1>("0x1"));
	assert((u2810989472.xorr()) == UInt<1>("0x0"));
	assert(~u2386756833 == UInt<32>("0x71bcfb1e"));
	assert((u2386756833.andr()) == UInt<1>("0x0"));
	assert((u2386756833.orr()) == UInt<1>("0x1"));
	assert((u2386756833.xorr()) == UInt<1>("0x0"));
	assert(~u4103589442 == UInt<32>("0xb6831bd"));
	assert((u4103589442.andr()) == UInt<1>("0x0"));
	assert((u4103589442.orr()) == UInt<1>("0x1"));
	assert((u4103589442.xorr()) == UInt<1>("0x1"));
	assert(~u3670823460 == UInt<32>("0x2533addb"));
	assert((u3670823460.andr()) == UInt<1>("0x0"));
	assert((u3670823460.orr()) == UInt<1>("0x1"));
	assert((u3670823460.xorr()) == UInt<1>("0x0"));
	assert(~u2762064974 == UInt<32>("0x5b5e3bb1"));
	assert((u2762064974.andr()) == UInt<1>("0x0"));
	assert((u2762064974.orr()) == UInt<1>("0x1"));
	assert((u2762064974.xorr()) == UInt<1>("0x1"));
	assert(~u3814238324 == UInt<32>("0x1ca7578b"));
	assert((u3814238324.andr()) == UInt<1>("0x0"));
	assert((u3814238324.orr()) == UInt<1>("0x1"));
	assert((u3814238324.xorr()) == UInt<1>("0x1"));
	assert(~u3973165845 == UInt<32>("0x132e4cea"));
	assert((u3973165845.andr()) == UInt<1>("0x0"));
	assert((u3973165845.orr()) == UInt<1>("0x1"));
	assert((u3973165845.xorr()) == UInt<1>("0x1"));
	assert(~u3745721174 == UInt<32>("0x20bcd4a9"));
	assert((u3745721174.andr()) == UInt<1>("0x0"));
	assert((u3745721174.orr()) == UInt<1>("0x1"));
	assert((u3745721174.xorr()) == UInt<1>("0x0"));
	assert(~u3129991641 == UInt<32>("0x45701e26"));
	assert((u3129991641.andr()) == UInt<1>("0x0"));
	assert((u3129991641.orr()) == UInt<1>("0x1"));
	assert((u3129991641.xorr()) == UInt<1>("0x1"));
	assert(~u3110131838 == UInt<32>("0x469f2781"));
	assert((u3110131838.andr()) == UInt<1>("0x0"));
	assert((u3110131838.orr()) == UInt<1>("0x1"));
	assert((u3110131838.xorr()) == UInt<1>("0x1"));

	return 0;
}