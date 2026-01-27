#include <bits/stdc++.h>
using namespace std;

vector<vector<int>> g;
int n,m,w;

bool floyd_warshal(){
    for(int k=0;k<=n;k++){
        for(int a=0;a<=n;a++){
            for(int b=0;b<=n;b++){
                g[a][b] = min(g[a][b], g[a][k]+g[k][b]);
            }
        }
    }
    for(int i=0;i<=n;i++){
        if (g[i][i]<0) return true;
    }
    return false;
}

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);

    int TC;cin>>TC;
    while (TC--)
    {
        cin>>n>>m>>w;
        g.clear();
        g.assign(n+1,vector<int> (n+1,1e9));
        int s,e,t;
        for(int i=0;i<m;i++){
            cin>>s>>e>>t;
            g[s][e] = min(g[s][e],t);
            g[e][s] = min(g[e][s],t);
        }
        for(int i=0;i<w;i++){
            cin>>s>>e>>t;
            g[s][e] = min(g[s][e],-t);
        }
        if(floyd_warshal()) cout << "YES\n";
        else cout << "NO\n";
    }
    return 0;
}