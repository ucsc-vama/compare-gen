#include "../../firrtl-sig/uint.h"
#include <iostream>
#include <assert.h>
#include <stdlib.h>
using namespace std;

int main() {

	UInt<4> a("0xc");
	UInt<4> b("0xc");
	assert(a.cat(b) == UInt<8>("0xcc"));

	return 0;
}