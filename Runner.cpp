#include "./firrtl-sig/uint.h"
#include <iostream>
#include <assert.h>
#include <stdlib.h>
using namespace std;

int main() {

	UInt<16> u59046("0xe6a6");
	assert(u59046.shr<4>() == UInt<12>("0xe6a"));

	return 0;
}