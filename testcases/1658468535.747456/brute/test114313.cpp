#include "../../../firrtl-sig/uint.h"
#include <assert.h>
int main() {

	UInt<4> a("0xb");
	UInt<4> b("0xd");
	assert((a+b) == UInt<5>("0x18"));

	return 0;
}