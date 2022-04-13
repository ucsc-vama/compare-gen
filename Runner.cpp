#include "./firrtl-sig/uint.h"
#include <iostream>
#include <assert.h>
#include <stdlib.h>
using namespace std;

int main() {

	UInt<1> u0("0x0");
	UInt<2> u1("0x2");

	cout << u0 + u1 << endl;

	return 0;
}