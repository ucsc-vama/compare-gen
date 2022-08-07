#include "../../../firrtl-sig/uint.h"
#include <assert.h>
int main() {

	UInt<2> a("0x3");
	assert((a.bits<0,0>()) == UInt<0>("0x0"));

	return 0;
}