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

    int x1,y1,x2,y2,x3,y3;
    cin >> x1 >> y1 >> x2 >> y2 >> x3 >> y3;

    int v1_x = (x2-x1);
    int v1_y = (y2-y1);
    int v2_x = (x3-x1);
    int v2_y = (y3-y1);

    int z = v1_x * v2_y - v1_y * v2_x;
    cout << (z>0)-(z<0);

    return 0;
}