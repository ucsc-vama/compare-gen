#include "../../firrtl-sig/uint.h"
#include <iostream>
#include <assert.h>
#include <stdlib.h>
using namespace std;

int main() {

	UInt<4> a("0x9");
	UInt<4> b("0x9");
	assert(a.cat(b) == UInt<8>("0x99"));

	return 0;
}