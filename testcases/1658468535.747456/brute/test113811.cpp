#include "../../../firrtl-sig/uint.h"
#include <assert.h>
int main() {

	UInt<4> a("0xb");
	UInt<4> b("0xb");
	assert((a&b) == UInt<4>("0xb"));

	return 0;
}