#include "../../../firrtl-sig/uint.h"
#include <assert.h>
int main() {

	UInt<4> a("0xd");
	UInt<4> b("0x9");
	assert(a.cat(b) == UInt<8>("0xd9"));

	return 0;
}