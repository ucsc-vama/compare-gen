#include "../../../firrtl-sig/uint.h"
#include <assert.h>
int main() {

	UInt<4> a("0xc");
	UInt<4> b("0x9");
	assert(a.cat(b) == UInt<8>("0xc9"));

	return 0;
}