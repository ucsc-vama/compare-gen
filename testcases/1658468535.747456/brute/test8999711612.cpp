#include "../../../firrtl-sig/uint.h"
#include <assert.h>
int main() {

	UInt<4> a("0x8");
	UInt<4> b("0xc");
	assert(a.cat(b) == UInt<8>("0x8c"));

	return 0;
}