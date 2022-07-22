#include "../../../firrtl-sig/uint.h"
#include <assert.h>
int main() {

	UInt<4> a("0xf");
	UInt<4> b("0xb");
	assert((a/b) == UInt<4>("0x1"));

	return 0;
}