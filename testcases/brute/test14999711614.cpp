#include "../../firrtl-sig/uint.h"
#include <iostream>
#include <assert.h>
#include <stdlib.h>
using namespace std;

int main() {

	UInt<4> a("0xe");
	UInt<4> b("0xe");
	assert(a.cat(b) == UInt<8>("0xee"));

	return 0;
}