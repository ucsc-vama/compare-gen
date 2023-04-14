#include "./firrtl-sig/uint.h"
#include "./firrtl-sig/sint.h"
#include <iostream>
#include <assert.h>
#include <stdlib.h>
using namespace std;

int main() {

    SInt<1> s0("0x0");
	SInt<1> s1(0x1);
    SInt<4> s2(0x2);
	SInt<4> s3(0x3);
    SInt<4> s4(0x4);
	SInt<4> s5(0x5);
    SInt<4> s6(0x6);
    SInt<4> s7(0x7);
	SInt<4> s8(0x8);
    SInt<4> s9(0x9);
	SInt<4> sa(0xa);
    SInt<16> s6dba(0x6dba);
    SInt<16> sccb2(0xccb2);

    UInt<4> u4(0x4);

    SInt<64> a64s("0x71088d1c4a5c4a02");
    SInt<64> b64s("0xdefaa415d9062302");

    SInt<80> a80s("0x381c1fe6bca6875922fe");
    SInt<80> b80s("0xefbe8ae0d38ab7f36dda");

    SInt<158> s158("0x381c1fe6bca6875922fe381c1fe6bca6875922fe");


    UInt<80> b80u("0xefbe8ae0d38ab7f36dda");
    // cout << UInt<16>(~s6dba) << endl;
    // cout << UInt<16>(~sccb2) << endl;
    // cout << ~s158 << endl;
    // cout << ~s9 << endl;
    
    //and, or, xor
    // cout << (s6dba ^ sccb2) << endl;
    // cout << (a80s ^ b80s) << endl;

    //andr, orr, xorr
    // cout << (s9.xorr()) << endl;
    // cout << (s6dba.xorr()) << endl;
    // cout << (sccb2.xorr()) << endl;
    // cout << (a64s.xorr()) << endl;
    // cout << (b64s.xorr()) << endl;
    // cout << (a80s.xorr()) << endl;
    // cout << (s158.xorr()) << endl;

    //cat
    // cout << (s6dba.cat(sccb2)) << endl;
    // cout << (s9.cat(s3)) << endl;
    // cout << (s158.cat(a80s)) << endl;
    
    //bits
    // cout << (s6dba.bits<15,3>()) << endl;
    // cout << (a64s.bits<32,13>()) << endl;
    // cout << (b80s.bits<72,59>()) << endl;
    // cout << (s158.bits<102,72>()) << endl;

    //head, tail
    //ERROR. cannot do tail operation with bitwidth equal to n
    // Issue where result is 0.
    // cout << (s3.tail<3>()) << endl;
    // cout << (s6dba.tail<3>()) << endl;
    // cout << (b80s.tail<79>()) << endl; 
    // cout << (s158.tail<63>()) << endl;

    // cout << (b80s.tail<80>()) << endl;
    // cout << (b80s.head<0>()) << endl;
    // cout << (b80u.tail<80>()) << endl;

    // SInt<2> a(0x3);
    // cout << (a >> UInt<2>("0x2"))  << endl;
    // cout << SInt<2>(0x3) << endl;
	// cout << ((a >> UInt<2>("0x2")) == SInt<2>(0x3)) << endl;

    SInt<3> a("0x6");
    // cout << (a >> UInt<1>("0x0")) << endl;
    // cout << (a >> UInt<1>("0x1")) << endl;
    // cout << (a >> UInt<2>("0x2")) << endl;
    // cout << "here" << (a >> UInt<2>("0x3")) << endl;
    // cout << (a >> UInt<3>("0x4")) << endl;
    // cout << (a >> UInt<3>("0x5")) << endl;

    cout << a.tail<0>() << endl;

    return 0;
}