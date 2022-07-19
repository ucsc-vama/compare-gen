#include "../../firrtl-sig/uint.h"
#include <iostream>
#include <assert.h>
#include <stdlib.h>
using namespace std;

int main() {

	UInt<4> a("0xb");
	UInt<4> b("0xd");
	assert((a^b) == UInt<4>("0x6"));

	return 0;
}