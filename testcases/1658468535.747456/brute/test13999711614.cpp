#include "../../../firrtl-sig/uint.h"
#include <assert.h>
int main() {

	UInt<4> a("0xd");
	UInt<4> b("0xe");
	assert(a.cat(b) == UInt<8>("0xde"));

	return 0;
}