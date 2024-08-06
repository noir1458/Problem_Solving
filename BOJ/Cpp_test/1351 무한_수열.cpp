#include<iostream>
#include<bits/stdc++.h>
#include<map>

using namespace std;

long long N,P,Q;
map<long long, long long> map1;


long long func2(long long n){
    if (map1.count(n)) return map1[n];
    return map1[n] = func2(n/P) + func2(n/Q);
}

int main(){
    ios::sync_with_stdio(0);
    cin.tie(0),cout.tie(0);

    cin >> N >> P >> Q;
    map1.insert({0,1});

    cout << func2(N);

    return 0;
}