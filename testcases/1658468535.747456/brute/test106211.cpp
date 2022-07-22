#include "../../../firrtl-sig/uint.h"
#include <assert.h>
int main() {

	UInt<4> a("0xa");
	UInt<4> b("0xb");
	assert(0 == (a>b));

	return 0;
}