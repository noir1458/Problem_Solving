#include<iostream>
#include<bits/stdc++.h>
using namespace std;
int main(){
    cin.tie(0);cout.tie(0);
    ios::sync_with_stdio(0);

    long long s,e;
    cin >> s >> e;
    if(s>e){
        long long tmp = s;
        s = e;
        e = tmp;
    }
    if (s==e){
        cout << 0 << "\n";
        cout << "";
        return 0;
    }
    cout << (e-s-1) << "\n";
    for(long long i=s+1;i<e;i++){
        cout << i << " ";
    }
    return 0;
}