#include "../../../firrtl-sig/uint.h"
#include <assert.h>
int main() {

	UInt<4> a("0xa");
	UInt<4> b("0x8");
	assert((a-b) == UInt<5>("0x2"));

	return 0;
}