#include "./firrtl-sig/uint.h"
#include <iostream>
#include <assert.h>
#include <stdlib.h>
using namespace std;

int main() {

	UInt<16> u53127("0xcf87");
	UInt<16> u55840("0xda20");
	assert(u53127+u55840 == UInt<17>("0x1a9a7"));

	return 0;
}