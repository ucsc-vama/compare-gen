#include "../../../firrtl-sig/uint.h"
#include <assert.h>
int main() {

	UInt<4> a("0x9");
	UInt<4> b("0xa");
	assert((a^b) == UInt<4>("0x3"));

	return 0;
}