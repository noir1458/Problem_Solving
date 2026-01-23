#include <bits/stdc++.h>
using namespace std;

int n,m;
struct Edge{
    int u,v,c;
    bool operator<(const Edge &other) const{
        return c<other.c;
    }
};
vector<Edge> g;
vector<int> parent;
vector<int> rnk;

int _find(int a){
    if(parent[a]==a) return a;
    return parent[a] = _find(parent[a]);
}

bool _union(int a, int b){
    a = _find(a);
    b = _find(b);
    if (a==b) return false;

    if (rnk[a] > rnk[b]){
        int tmp=a;a=b;b=tmp;
    }
    parent[a] = b;
    if (rnk[a]==rnk[b]){
        rnk[b]++;
    }
    return true;
}

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);

    cin>>n>>m;
    for(int i=0;i<m;i++){
        int a,b,c;cin>>a>>b>>c;
        g.push_back({a,b,c});
    }
    rnk.resize(n+1,0);
    for(int i=0;i<n+1;i++){
        parent.push_back(i);
    }

    sort(g.begin(),g.end());

    int connected = 0;
    int cost = 0;
    int mx = 0;
    for(int i=0;i<size(g);i++){
        int a = g[i].u;
        int b = g[i].v;
        int c = g[i].c;
        if (_union(a,b)){
            connected++;
            cost += c;
            mx = max(mx,c);
        }
        if (connected==n-1) break;
    }
    cout << cost-mx;

    return 0;
}