#include "../../../firrtl-sig/uint.h"
#include <assert.h>
int main() {

	UInt<4> a("0xb");
	UInt<4> b("0x9");
	assert((a*b) == UInt<8>("0x63"));

	return 0;
}