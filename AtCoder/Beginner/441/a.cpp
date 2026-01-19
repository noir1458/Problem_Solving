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

    int p,q,x,y; cin>>p>>q>>x>>y;
    if (p<=x && x < p+100 && q <=y && y < q+100){
        cout << "Yes";
    } else {
        cout << "No";
    }

    return 0;
}