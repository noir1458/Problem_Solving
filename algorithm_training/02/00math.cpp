#include<iostream>
#include<bits/stdc++.h>

using namespace std;

int main(){
    long long x = 123456789123456789LL;

    // 아래 코드는 버그가 있다
    int a = 123456789;
    long long b = a*a;
    cout << b << "\n"; //-1757895751

    // g++ 컴파일러가 지원하는 자료형
    __int128_t c;

}