#include "../../firrtl-sig/uint.h"
#include <iostream>
#include <assert.h>
#include <stdlib.h>
using namespace std;

int main() {

	UInt<4> a("0xb");
	UInt<4> b("0xb");
	assert(0 == (a!=b));

	return 0;
}