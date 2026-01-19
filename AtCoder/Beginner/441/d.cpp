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

ll N,M,L,S,T; 

struct Edge {
    ll V,C; 
};


void dfs(vector<vector<Edge>> &g, set<ll> &res, ll v, ll c, ll m){
    if (c > T) return;
    if (m==L){
        if (S<=c) res.insert(v);
        return;
    }

    rep(i,0,g[v].size()){
        dfs(g,res,g[v][i].V,g[v][i].C+c,m+1);
    }
}

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);

    cin>>N>>M>>L>>S>>T;
    vector<vector<Edge>> g (N+1, vector<Edge> (0)); // 목적지,cost

    rep(i,0,M){
        ll U,V,C; cin>>U>>V>>C;
        g[U].push_back({V,C});
    }

    set<ll> res;
    dfs(g,res,1,0,0);
    for(auto e:res){
        cout << e << " ";
    }
    
    return 0;
}