#include "../../firrtl-sig/uint.h"
#include <iostream>
#include <assert.h>
#include <stdlib.h>
using namespace std;

int main() {

	UInt<4> a("0xd");
	UInt<4> b("0xe");
	assert((a*b) == UInt<8>("0xb6"));

	return 0;
}