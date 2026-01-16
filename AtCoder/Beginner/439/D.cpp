#include<bits/stdc++.h>
#include<iostream>
using namespace std;
typedef long long ll;

int main(){
    ios::sync_with_stdio(0);
    cin.tie(0);cout.tie(0);

    ll N; cin >> N;
    vector<ll> v(N);
    for(int i=0;i<N;i++){
        cin >> v[i];
    }

    map<ll, vector<ll>> pos;
    for(int i=0;i<N;i++){
        pos[v[i]].push_back(i+1);
    }

    //
}