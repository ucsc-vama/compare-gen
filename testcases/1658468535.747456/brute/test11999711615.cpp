#include "../../../firrtl-sig/uint.h"
#include <assert.h>
int main() {

	UInt<4> a("0xb");
	UInt<4> b("0xf");
	assert(a.cat(b) == UInt<8>("0xbf"));

	return 0;
}