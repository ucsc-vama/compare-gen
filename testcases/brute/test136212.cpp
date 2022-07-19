#include "../../firrtl-sig/uint.h"
#include <iostream>
#include <assert.h>
#include <stdlib.h>
using namespace std;

int main() {

	UInt<4> a("0xd");
	UInt<4> b("0xc");
	assert(1 == (a>b));

	return 0;
}