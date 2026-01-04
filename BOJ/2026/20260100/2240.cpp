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

    int T,W; cin>>T>>W;
    vector<int> v(T+1);
    rep(i,1,T+1){
        cin>>v[i];
    }

    vector<vector<int>> dp(T+1,vector<int> (W+1));
    rep(i,1,T+1){
        rep(j,0,W+1){
            int pos = (j%2 == 0) ? 1:2;
            if (j>0){
                dp[i][j] = max(dp[i-1][j],dp[i-1][j-1]) + (pos==v[i]?1:0);
            } else {
                dp[i][j] = dp[i-1][j] + (pos==v[i]?1:0);
            }
        }
    }
    cout << *max_element(dp[T].begin(),dp[T].end());
    return 0;
}