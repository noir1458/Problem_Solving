#include<iostream>
#include<bits/stdc++.h>

using namespace std;

int func3(){
    int a = 10;
    int mod = 1000000007;
    for (int i=0; i<10; i++){
        a = 10 * a % mod;
        cout << a << endl;
    }
    return a;
}

int main(){
    cin.tie(0); cout.tie(0);
    ios::sync_with_stdio(0);

    cout << func3() << endl;

    return 0;
}