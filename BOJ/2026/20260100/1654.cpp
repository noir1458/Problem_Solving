#include <bits/stdc++.h>
using namespace std;

using ll = long long;
using pii = pair<int, int>;
using pll = pair<ll, ll>;

const int INF = 1e9;
const ll LINF = 1e18;
const int MOD = 998244353; // or 1e9 + 7

#define rep(i, a, b) for (int i = (a); i < (b); ++i)
#define all(x) (x).begin(), (x).end()

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);

    ll K,N; cin>>K>>N;
    vector<ll> v(K);
    rep(i,0,K){
        cin>>v[i];
    }

    ll l=1,r=*max_element(all(v)),m=0;
    ll res=0;
    while (l<=r){
        m = (l+r)/2;
        ll c= 0;

        rep(i,0,K){
            c += v[i]/m;
        }

        if (c >= N){
            l = m+1;
            res = m;
            
        } else {
            r = m-1;
        }
    }
    cout << res;
    return 0;
}