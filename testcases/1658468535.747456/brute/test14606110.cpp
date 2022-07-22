#include "../../../firrtl-sig/uint.h"
#include <assert.h>
int main() {

	UInt<4> a("0xe");
	UInt<4> b("0xa");
	assert(0 == (a<=b));

	return 0;
}