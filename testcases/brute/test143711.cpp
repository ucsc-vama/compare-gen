#include "../../firrtl-sig/uint.h"
#include <iostream>
#include <assert.h>
#include <stdlib.h>
using namespace std;

int main() {

	UInt<4> a("0xe");
	UInt<4> b("0xb");
	assert((a%b) == UInt<4>("0x3"));

	return 0;
}