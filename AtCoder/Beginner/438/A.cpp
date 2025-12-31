#include<bits/stdc++.h>
#include<iostream>
using namespace std;

int main(){
    ios::sync_with_stdio(0);
    cin.tie(0);cout.tie(0);

    int D,F; cin >> D >> F;
    int tmp=F;
    while (tmp <= D)
    {
        tmp += 7;
    }
    cout << tmp - D;
}