#include "./firrtl-sig/uint.h"
#include <iostream>
#include <assert.h>
#include <stdlib.h>
using namespace std;

int main() {

	UInt<80> u0("0x3da3e90d8f93ab12d239");
	UInt<80> u1("0x234901234823ad3e9283");

	cout << (u0 - u1) << endl;

	return 0;
}