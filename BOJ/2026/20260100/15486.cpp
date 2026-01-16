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

    vector<int> T;
    vector<int> P;
    int N; cin>>N;
    rep(i,0,N){
        int a,b; cin>>a>>b;
        T.push_back(a); P.push_back(b);
    }
    
    vector<int> dp(N+1);
    int max_p = 0;
    rep(i,0,N){
        max_p = max(max_p, dp[i]);
        if (i+T[i] < N+1){
            dp[i+T[i]] = max(dp[i+T[i]], max_p + P[i]);
        }
    }
    max_p = max(max_p, dp[N]);

    cout << max_p;

    return 0;
}