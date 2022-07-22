#include "../../../firrtl-sig/uint.h"
#include <assert.h>
int main() {

	UInt<4> a("0xf");
	UInt<4> b("0xf");
	assert((a*b) == UInt<8>("0xe1"));

	return 0;
}