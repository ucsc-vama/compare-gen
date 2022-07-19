#include "../../firrtl-sig/uint.h"
#include <iostream>
#include <assert.h>
#include <stdlib.h>
using namespace std;

int main() {

	UInt<4> a("0xf");
	UInt<4> b("0x8");
	assert(a.cat(b) == UInt<8>("0xf8"));

	return 0;
}