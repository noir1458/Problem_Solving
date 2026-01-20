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

int N=0,M=0; 

void dfs(vector<int> &v,vector<int> &res, int i){
    res.push_back(v[i]);
    if (size(res)==M){
        for(const auto&e :res){
            cout << e << " ";
        }
        cout << "\n";
        res.pop_back();
        return;
    }
    for(int j=i;j<size(v);j++){
        dfs(v,res,j);
    }
    res.pop_back();
}

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);

    cin>>N>>M;
    set<int> s;
    rep(i,0,N){
        int x; cin >> x;
        s.insert(x);
    } 

    vector<int> v(all(s));
    sort(all(v));

    vector<int> res;
    for(int i=0;i<size(v);i++){
        dfs(v,res,i);
    }

    return 0;
}