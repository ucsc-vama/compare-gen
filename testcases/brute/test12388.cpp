#include "../../firrtl-sig/uint.h"
#include <iostream>
#include <assert.h>
#include <stdlib.h>
using namespace std;

int main() {

	UInt<4> a("0xc");
	UInt<4> b("0x8");
	assert((a&b) == UInt<4>("0x8"));

	return 0;
}