#include "../../firrtl-sig/uint.h"
#include <iostream>
#include <assert.h>
#include <stdlib.h>
using namespace std;

int main() {

	UInt<4> a("0xf");
	UInt<4> b("0xf");
	assert((a^b) == UInt<4>("0x0"));

	return 0;
}