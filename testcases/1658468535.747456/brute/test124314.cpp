#include "../../../firrtl-sig/uint.h"
#include <assert.h>
int main() {

	UInt<4> a("0xc");
	UInt<4> b("0xe");
	assert((a+b) == UInt<5>("0x1a"));

	return 0;
}