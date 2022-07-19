#include "../../firrtl-sig/uint.h"
#include <iostream>
#include <assert.h>
#include <stdlib.h>
using namespace std;

int main() {

	UInt<4> a("0xe");
	UInt<4> b("0xc");
	assert((a^b) == UInt<4>("0x2"));

	return 0;
}