#include <bits/stdc++.h>
using namespace std;

using ll = long long;
using pii = pair<int, int>;
using pll = pair<ll, ll>;

const int INF = 1e9;
const ll LINF = 1e18;
const int MOD = 10007; // or 1e9 + 7

#define rep(i, a, b) for (int i = (a); i < (b); ++i)
#define all(x) (x).begin(), (x).end()


int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);

    ll n; cin>>n;

    vector<ll> dp;
    dp.push_back(0); // 0 pass
    dp.push_back(1); // 1
    dp.push_back(3); // 2
    
    // 끝에 오는 타일을 생각
    // 새로 하나 1개 - 1
    // 가로 2개, 2*2 1개 - 2

    rep(i,3,n+1){
        ll t = dp[i-1] + 2*dp[i-2];
        dp.push_back(t%MOD);
    }
    cout << dp[n];
    return 0;
}