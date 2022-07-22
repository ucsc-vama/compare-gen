#include "../../../firrtl-sig/uint.h"
#include <assert.h>
int main() {

	UInt<4> a("0x8");
	UInt<4> b("0xb");
	assert((a*b) == UInt<8>("0x58"));

	return 0;
}