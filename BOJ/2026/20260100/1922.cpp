#include <bits/stdc++.h>
using namespace std;

int n,m;
struct Edge{
    int c,u,v;
    bool operator<(const Edge &other) const{
        return c<other.c;
    }
};
vector<Edge> v;
vector<int> parent;
vector<int> rnk;

int find(int a){
    if (parent[a]==a) return a;
    return parent[a] = find(parent[a]);
}

bool _union(int a, int b){
    a = find(a);
    b = find(b);
    if (a==b) return false;

    if (rnk[a]<rnk[b]) parent[a] = b;
    else if (rnk[a]>rnk[b]) parent[b] = a;
    else {
        parent[b] = a;
        rnk[a]++;
    }
    return true;
}

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);

    cin>>n>>m;
    for(int i=0;i<m;i++){
        int u,v1,c; cin>>u>>v1>>c;
        v.push_back({c,u,v1});
    }

    sort(v.begin(),v.end());
    for(int i=0;i<n+1;i++){ // 0번 버림
        parent.push_back(i);
    }
    rnk.resize(n+1,0);

    int connected = 0;
    int cost = 0;
    for(int i=0;i<size(v);i++){
        Edge X = v[i];
        if (_union(X.u,X.v)){
            cost += X.c;
            connected ++;
        }
        if (connected==n-1) break;
    }
    cout << cost; 
    return 0;
}