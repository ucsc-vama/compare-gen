#include "../../../firrtl-sig/uint.h"
#include <assert.h>
int main() {

	UInt<4> a("0xc");
	UInt<4> b("0xa");
	assert((a*b) == UInt<8>("0x78"));

	return 0;
}