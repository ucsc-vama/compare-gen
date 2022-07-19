#include "../../firrtl-sig/uint.h"
#include <iostream>
#include <assert.h>
#include <stdlib.h>
using namespace std;

int main() {

	UInt<4> a("0x8");
	UInt<4> b("0x9");
	assert((a*b) == UInt<8>("0x48"));

	return 0;
}