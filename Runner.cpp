#include "./firrtl-sig/uint.h"
#include <iostream>
#include <assert.h>
#include <stdlib.h>
using namespace std;

int main() {

	UInt<16> u54583("0xd537");
	UInt<16> u41385("0xa1a9");
	UInt<16> u48670("0xbe1e");
	UInt<16> u60778("0xed6a");
	UInt<16> u53702("0xd1c6");
	UInt<16> u45791("0xb2df");
	assert(u54583+u54583 == UInt<17>("0x1aa6e"));
	assert(u54583+u41385 == UInt<17>("0x176e0"));
	assert(u54583+u48670 == UInt<17>("0x19355"));
	assert(u54583+u60778 == UInt<17>("0x1c2a1"));
	assert(u54583+u53702 == UInt<17>("0x1a6fd"));
	assert(u54583+u45791 == UInt<17>("0x18816"));
	assert(u41385+u54583 == UInt<17>("0x176e0"));
	assert(u41385+u41385 == UInt<17>("0x14352"));
	assert(u41385+u48670 == UInt<17>("0x15fc7"));
	assert(u41385+u60778 == UInt<17>("0x18f13"));
	assert(u41385+u53702 == UInt<17>("0x1736f"));
	assert(u41385+u45791 == UInt<17>("0x15488"));
	assert(u48670+u54583 == UInt<17>("0x19355"));
	assert(u48670+u41385 == UInt<17>("0x15fc7"));
	assert(u48670+u48670 == UInt<17>("0x17c3c"));
	assert(u48670+u60778 == UInt<17>("0x1ab88"));
	assert(u48670+u53702 == UInt<17>("0x18fe4"));
	assert(u48670+u45791 == UInt<17>("0x170fd"));
	assert(u60778+u54583 == UInt<17>("0x1c2a1"));
	assert(u60778+u41385 == UInt<17>("0x18f13"));
	assert(u60778+u48670 == UInt<17>("0x1ab88"));
	assert(u60778+u60778 == UInt<17>("0x1dad4"));
	assert(u60778+u53702 == UInt<17>("0x1bf30"));
	assert(u60778+u45791 == UInt<17>("0x1a049"));
	assert(u53702+u54583 == UInt<17>("0x1a6fd"));
	assert(u53702+u41385 == UInt<17>("0x1736f"));
	assert(u53702+u48670 == UInt<17>("0x18fe4"));
	assert(u53702+u60778 == UInt<17>("0x1bf30"));
	assert(u53702+u53702 == UInt<17>("0x1a38c"));
	assert(u53702+u45791 == UInt<17>("0x184a5"));
	assert(u45791+u54583 == UInt<17>("0x18816"));
	assert(u45791+u41385 == UInt<17>("0x15488"));
	assert(u45791+u48670 == UInt<17>("0x170fd"));
	assert(u45791+u60778 == UInt<17>("0x1a049"));
	assert(u45791+u53702 == UInt<17>("0x184a5"));
	assert(u45791+u45791 == UInt<17>("0x165be"));
	assert(u54583-u54583 == UInt<17>("0x0"));
	assert(u54583-u41385 == UInt<17>("0x338e"));
	assert(u54583-u48670 == UInt<17>("0x1719"));
	assert(u54583-u60778 == UInt<17>("0x1e7cd"));
	assert(u54583-u53702 == UInt<17>("0x371"));
	assert(u54583-u45791 == UInt<17>("0x2258"));
	assert(u41385-u54583 == UInt<17>("0x1cc72"));
	assert(u41385-u41385 == UInt<17>("0x0"));
	assert(u41385-u48670 == UInt<17>("0x1e38b"));
	assert(u41385-u60778 == UInt<17>("0x1b43f"));
	assert(u41385-u53702 == UInt<17>("0x1cfe3"));
	assert(u41385-u45791 == UInt<17>("0x1eeca"));
	assert(u48670-u54583 == UInt<17>("0x1e8e7"));
	assert(u48670-u41385 == UInt<17>("0x1c75"));
	assert(u48670-u48670 == UInt<17>("0x0"));
	assert(u48670-u60778 == UInt<17>("0x1d0b4"));
	assert(u48670-u53702 == UInt<17>("0x1ec58"));
	assert(u48670-u45791 == UInt<17>("0xb3f"));
	assert(u60778-u54583 == UInt<17>("0x1833"));
	assert(u60778-u41385 == UInt<17>("0x4bc1"));
	assert(u60778-u48670 == UInt<17>("0x2f4c"));
	assert(u60778-u60778 == UInt<17>("0x0"));
	assert(u60778-u53702 == UInt<17>("0x1ba4"));
	assert(u60778-u45791 == UInt<17>("0x3a8b"));
	assert(u53702-u54583 == UInt<17>("0x1fc8f"));
	assert(u53702-u41385 == UInt<17>("0x301d"));
	assert(u53702-u48670 == UInt<17>("0x13a8"));
	assert(u53702-u60778 == UInt<17>("0x1e45c"));
	assert(u53702-u53702 == UInt<17>("0x0"));
	assert(u53702-u45791 == UInt<17>("0x1ee7"));
	assert(u45791-u54583 == UInt<17>("0x1dda8"));
	assert(u45791-u41385 == UInt<17>("0x1136"));
	assert(u45791-u48670 == UInt<17>("0x1f4c1"));
	assert(u45791-u60778 == UInt<17>("0x1c575"));
	assert(u45791-u53702 == UInt<17>("0x1e119"));
	assert(u45791-u45791 == UInt<17>("0x0"));
	assert(u54583*u54583 == UInt<32>("0xb19491d1"));
	assert(u54583*u41385 == UInt<32>("0x86a4584f"));
	assert(u54583*u48670 == UInt<32>("0x9e57ce72"));
	assert(u54583*u60778 == UInt<32>("0xc5bc33c6"));
	assert(u54583*u53702 == UInt<32>("0xaeb6cf8a"));
	assert(u54583*u45791 == UInt<32>("0x94f9f8e9"));
	assert(u41385*u54583 == UInt<32>("0x86a4584f"));
	assert(u41385*u41385 == UInt<32>("0x66160191"));
	assert(u41385*u48670 == UInt<32>("0x780e5fce"));
	assert(u41385*u60778 == UInt<32>("0x95ec64fa"));
	assert(u41385*u53702 == UInt<32>("0x847801b6"));
	assert(u41385*u45791 == UInt<32>("0x70f45437"));
	assert(u48670*u54583 == UInt<32>("0x9e57ce72"));
	assert(u48670*u41385 == UInt<32>("0x780e5fce"));
	assert(u48670*u48670 == UInt<32>("0x8d308b84"));
	assert(u48670*u60778 == UInt<32>("0xb0507e6c"));
	assert(u48670*u53702 == UInt<32>("0x9bc98934"));
	assert(u48670*u45791 == UInt<32>("0x84d67822"));
	assert(u60778*u54583 == UInt<32>("0xc5bc33c6"));
	assert(u60778*u41385 == UInt<32>("0x95ec64fa"));
	assert(u60778*u48670 == UInt<32>("0xb0507e6c"));
	assert(u60778*u60778 == UInt<32>("0xdc2d6fe4"));
	assert(u60778*u53702 == UInt<32>("0xc28b29fc"));
	assert(u60778*u45791 == UInt<32>("0xa5e28356"));
	assert(u53702*u54583 == UInt<32>("0xaeb6cf8a"));
	assert(u53702*u41385 == UInt<32>("0x847801b6"));
	assert(u53702*u48670 == UInt<32>("0x9bc98934"));
	assert(u53702*u60778 == UInt<32>("0xc28b29fc"));
	assert(u53702*u53702 == UInt<32>("0xabe4e524"));
	assert(u53702*u45791 == UInt<32>("0x9292677a"));
	assert(u45791*u54583 == UInt<32>("0x94f9f8e9"));
	assert(u45791*u41385 == UInt<32>("0x70f45437"));
	assert(u45791*u48670 == UInt<32>("0x84d67822"));
	assert(u45791*u60778 == UInt<32>("0xa5e28356"));
	assert(u45791*u53702 == UInt<32>("0x9292677a"));
	assert(u45791*u45791 == UInt<32>("0x7cfade41"));
	assert(u54583/u54583 == UInt<16>("0x1"));
	assert(u54583/u41385 == UInt<16>("0x1"));
	assert(u54583/u48670 == UInt<16>("0x1"));
	assert(u54583/u60778 == UInt<16>("0x0"));
	assert(u54583/u53702 == UInt<16>("0x1"));
	assert(u54583/u45791 == UInt<16>("0x1"));
	assert(u41385/u54583 == UInt<16>("0x0"));
	assert(u41385/u41385 == UInt<16>("0x1"));
	assert(u41385/u48670 == UInt<16>("0x0"));
	assert(u41385/u60778 == UInt<16>("0x0"));
	assert(u41385/u53702 == UInt<16>("0x0"));
	assert(u41385/u45791 == UInt<16>("0x0"));
	assert(u48670/u54583 == UInt<16>("0x0"));
	assert(u48670/u41385 == UInt<16>("0x1"));
	assert(u48670/u48670 == UInt<16>("0x1"));
	assert(u48670/u60778 == UInt<16>("0x0"));
	assert(u48670/u53702 == UInt<16>("0x0"));
	assert(u48670/u45791 == UInt<16>("0x1"));
	assert(u60778/u54583 == UInt<16>("0x1"));
	assert(u60778/u41385 == UInt<16>("0x1"));
	assert(u60778/u48670 == UInt<16>("0x1"));
	assert(u60778/u60778 == UInt<16>("0x1"));
	assert(u60778/u53702 == UInt<16>("0x1"));
	assert(u60778/u45791 == UInt<16>("0x1"));
	assert(u53702/u54583 == UInt<16>("0x0"));
	assert(u53702/u41385 == UInt<16>("0x1"));
	assert(u53702/u48670 == UInt<16>("0x1"));
	assert(u53702/u60778 == UInt<16>("0x0"));
	assert(u53702/u53702 == UInt<16>("0x1"));
	assert(u53702/u45791 == UInt<16>("0x1"));
	assert(u45791/u54583 == UInt<16>("0x0"));
	assert(u45791/u41385 == UInt<16>("0x1"));
	assert(u45791/u48670 == UInt<16>("0x0"));
	assert(u45791/u60778 == UInt<16>("0x0"));
	assert(u45791/u53702 == UInt<16>("0x0"));
	assert(u45791/u45791 == UInt<16>("0x1"));
	assert(u54583%u54583 == UInt<16>("0x0"));
	assert(u54583%u41385 == UInt<16>("0x338e"));
	assert(u54583%u48670 == UInt<16>("0x1719"));
	assert(u54583%u60778 == UInt<16>("0xd537"));
	assert(u54583%u53702 == UInt<16>("0x371"));
	assert(u54583%u45791 == UInt<16>("0x2258"));
	assert(u41385%u54583 == UInt<16>("0xa1a9"));
	assert(u41385%u41385 == UInt<16>("0x0"));
	assert(u41385%u48670 == UInt<16>("0xa1a9"));
	assert(u41385%u60778 == UInt<16>("0xa1a9"));
	assert(u41385%u53702 == UInt<16>("0xa1a9"));
	assert(u41385%u45791 == UInt<16>("0xa1a9"));
	assert(u48670%u54583 == UInt<16>("0xbe1e"));
	assert(u48670%u41385 == UInt<16>("0x1c75"));
	assert(u48670%u48670 == UInt<16>("0x0"));
	assert(u48670%u60778 == UInt<16>("0xbe1e"));
	assert(u48670%u53702 == UInt<16>("0xbe1e"));
	assert(u48670%u45791 == UInt<16>("0xb3f"));
	assert(u60778%u54583 == UInt<16>("0x1833"));
	assert(u60778%u41385 == UInt<16>("0x4bc1"));
	assert(u60778%u48670 == UInt<16>("0x2f4c"));
	assert(u60778%u60778 == UInt<16>("0x0"));
	assert(u60778%u53702 == UInt<16>("0x1ba4"));
	assert(u60778%u45791 == UInt<16>("0x3a8b"));
	assert(u53702%u54583 == UInt<16>("0xd1c6"));
	assert(u53702%u41385 == UInt<16>("0x301d"));
	assert(u53702%u48670 == UInt<16>("0x13a8"));
	assert(u53702%u60778 == UInt<16>("0xd1c6"));
	assert(u53702%u53702 == UInt<16>("0x0"));
	assert(u53702%u45791 == UInt<16>("0x1ee7"));
	assert(u45791%u54583 == UInt<16>("0xb2df"));
	assert(u45791%u41385 == UInt<16>("0x1136"));
	assert(u45791%u48670 == UInt<16>("0xb2df"));
	assert(u45791%u60778 == UInt<16>("0xb2df"));
	assert(u45791%u53702 == UInt<16>("0xb2df"));
	assert(u45791%u45791 == UInt<16>("0x0"));

	return 0;
}