#include "../../../firrtl-sig/uint.h"
#include <assert.h>
int main() {

	UInt<4> a("0xc");
	UInt<4> b("0xb");
	assert((a^b) == UInt<4>("0x7"));

	return 0;
}