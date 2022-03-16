#include "./firrtl-sig/uint.h"
#include<iostream>
#include <assert.h>
#include <stdlib.h>
using namespace std;

int main() {

	UInt<16> ua("0xe1ef");
	UInt<16> ub("0xbc51");
	UInt<16> uc("0x9da8");
	UInt<16> ud("0x9395");
	assert(ua.shr<4>() == UInt<12>("0xe1e"));

	return 0;
}