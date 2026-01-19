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

    ll N,K,X; cin>>N>>K>>X;
    vector<ll> v(N);
    rep(i,0,N){
        cin>>v[i];
    }

    sort(v.rbegin(),v.rend());

    ll w = N-K;
    ll c = 0;
    rep(i,w,N){
        c += v[i];
        w ++;
        if (c>=X) break;
    }
    if (c < X) cout << -1;
    else cout << w;
    return 0;
}