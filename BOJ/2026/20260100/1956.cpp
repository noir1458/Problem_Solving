#include <bits/stdc++.h>
using namespace std;

vector<vector<int>> g; 
int v,e;

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);

    cin>>v>>e;
    g.assign(v+1,vector<int>(v+1,1e9)); // 0번 버림
    for(int i=0;i<e;i++){
        int a,b,c;cin>>a>>b>>c;
        g[a][b] = c;
    }

    // 원래 대각선은 0으로 초기화 시켰으나, 지금은 전부 inf로
    for(int k=0;k<v+1;k++){
        for(int a=0;a<v+1;a++){
            for(int b=0;b<v+1;b++){
                g[a][b] = min(g[a][b], g[a][k]+g[k][b]);
            }
        }
    }
    
    int min_res = 1e9;
    for(int i=0;i<v+1;i++){
        min_res = min(min_res,g[i][i]);
    }
    if (min_res!=1e9) cout << min_res;
    else cout << "-1";

    return 0;
}