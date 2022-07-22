#include "../../../firrtl-sig/uint.h"
#include <assert.h>
int main() {

	UInt<4> a("0xd");
	UInt<4> b("0xf");
	assert((a*b) == UInt<8>("0xc3"));

	return 0;
}