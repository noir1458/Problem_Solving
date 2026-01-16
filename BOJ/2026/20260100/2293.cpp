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

    vector<ll> v;
    ll n,k; cin>>n>>k;
    vector<ll> dp(k+1);
    dp[0]=1;

    rep(i,0,n){
        ll x; cin>>x;
        v.push_back(x);
    }

    for(const auto &e : v){
        rep(i,e,k+1){
            dp[i] = dp[i] + dp[i-e];
        }
    }

    // for(auto e: dp){
    //     cout << e << " ";
    // }
    cout << dp[k];


    return 0;
}