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

    ll x,y; cin>>x>>y;

    ll z = (y*100) / x;

    if (z>=99){
        cout << -1 << "\n";
        return 0;
    }

    ll l=0,r=1000000000,res=-1;

    while (l<=r)
    {
        ll m = (l+r) / 2;
        ll next_z = ((y+m)*100 / (x+m));

        if(next_z > z){
            res = m;
            r = m-1;
        } else {
            l = m+1;
        }
    }
    cout << res;

    return 0;
}