#include "../../../firrtl-sig/uint.h"
#include <assert.h>
int main() {

	UInt<4> a("0xd");
	UInt<4> b("0xc");
	assert(0 == (a<=b));

	return 0;
}