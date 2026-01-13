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

    int N;cin>>N;
    cin.ignore();

    while (N--)
    {   
        string s;
        getline(cin,s,'\n');
        if (!s.empty() && s.back()=='\r'){
            s.pop_back();
        }

        bool ok = true;
        rep(i,0,(int)s.size()/2){
            if(tolower(s[i])!=tolower(s[s.size()-1-i])){
                ok = false;
                break;
            }
        }
        cout << (ok ? "Yes\n" : "No\n");
    }
    return 0;
}