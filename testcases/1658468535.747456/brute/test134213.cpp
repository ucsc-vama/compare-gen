#include "../../../firrtl-sig/uint.h"
#include <assert.h>
int main() {

	UInt<4> a("0xd");
	UInt<4> b("0xd");
	assert((a*b) == UInt<8>("0xa9"));

	return 0;
}