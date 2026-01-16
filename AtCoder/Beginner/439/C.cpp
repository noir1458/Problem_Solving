#include<bits/stdc++.h>
#include<iostream>
using namespace std;
typedef long long ll;

int main(){
    ios::sync_with_stdio(0);
    cin.tie(0);cout.tie(0);

    ll n; cin>>n;
    // n 이하의 숫자중 좋은 숫자 판별.

    vector<int> c(n+1,0); // 더한것, 나온횟수
    for(ll x=1;x*x < n; x++){
        for(ll y=x+1; x*x+y*y <= n ;y++){
            c[x*x+y*y]++;
        }
    }

    vector<ll> res;
    for(ll i=0;i<c.size();i++){
        if (c[i]==1){
            res.push_back(i);
        }
    }

    cout << res.size() << "\n";
    for(auto e:res){
        cout << e << " ";
    }
}