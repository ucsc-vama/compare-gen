#include "../../firrtl-sig/uint.h"
#include <iostream>
#include <assert.h>
#include <stdlib.h>
using namespace std;

int main() {

	UInt<4> a("0xd");
	UInt<4> b("0x9");
	assert((a-b) == UInt<5>("0x4"));

	return 0;
}