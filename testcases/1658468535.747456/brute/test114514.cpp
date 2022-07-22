#include "../../../firrtl-sig/uint.h"
#include <assert.h>
int main() {

	UInt<4> a("0xb");
	UInt<4> b("0xe");
	assert((a-b) == UInt<5>("0x1d"));

	return 0;
}