#include "../../../firrtl-sig/uint.h"
#include <assert.h>
int main() {

	UInt<4> a("0xf");
	UInt<4> b("0xc");
	assert((a*b) == UInt<8>("0xb4"));

	return 0;
}