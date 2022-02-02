#include "./firrtl-sig/uint.h"

#include<iostream>
using namespace std;

int main() {


   UInt<16>  a16u(0xcafe);
   UInt<16>  b16u(0xbebe);
   if(a16u + b16u == UInt<17>(0x189bc))
      cout << "equal" << endl;

   cout << "Hello World. This is C++ program" << endl;
   return 0;
}