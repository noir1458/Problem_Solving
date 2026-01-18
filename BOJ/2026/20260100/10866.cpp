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

    int N; cin>>N;
    deque<int> q;
    rep(i,0,N){
        string s;int x; cin >>s;
        if (s=="push_back" || s=="push_front"){
            cin >> x;
        }

        if (s=="push_back"){
            q.push_back(x);
        } else if (s=="push_front"){
            q.push_front(x);
        } else if (s=="front"){
            if (q.empty()) cout << -1 << "\n";
            else cout << q.front() << "\n";
        } else if (s=="back"){
            if (q.empty()) cout << -1 << "\n";
            else cout << q.back() << "\n";
        } else if (s=="pop_back"){
            if (q.empty()) cout << -1 << "\n";
            else {
            cout << q.back() << "\n";
            q.pop_back();
            }
        } else if (s=="pop_front"){
            if (q.empty()) cout << -1 << "\n";
            else {
            cout << q.front() << "\n";
            q.pop_front();
            }
        } else if (s=="size"){
            cout << q.size() << "\n";
        } else if (s=="empty"){
            cout << q.empty() << "\n";
        }
    }

    return 0;
}