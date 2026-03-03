#include <bits/stdc++.h>
using namespace std;

using ll = long long;

int K;
vector<int> v;
vector<vector<ll>> dp;
vector<ll> s;

void solve(){
    cin >>K;
    v.assign(K+1,0);
    dp.assign(K+1, vector<int> (K+1,-1));
    s.assign(K+1,0);

    for(int i=1;i<K+1;i++){
        cin>>v[i];
    }

    for(int i=1;i<K+1;i++){
        s[i] = s[i-1] + v[i];
    }

    for(int len=2;len<=K;len++){
        for(int i=1;i<=K-len+1)
    }


    cout << dp[0][K-1] << "\n";

}

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);

    int T; cin>>T;
    for(int i=0;i<T;i++){
        solve();
    }

    return 0;
}