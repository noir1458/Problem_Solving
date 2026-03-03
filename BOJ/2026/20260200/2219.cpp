#include <bits/stdc++.h>
using namespace std;

vector<vector<int>> dist;
int N,M;

void fw(){
    for(int k=1;k<N+1;k++){
        for(int a=1;a<N+1;a++){
            for(int b=1;b<N+1;b++){
                dist[a][b] = min(dist[a][b], dist[a][k]+dist[k][b]);
            }
        }
    }
}

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);

    cin>>N>>M;
    dist.assign(N+1,vector<int>(N+1,1e9));
    for(int i=0;i<M;i++){
        int a,b,c;cin>>a>>b>>c;
        dist[a][b] = c;
        dist[b][a] = c;
    }

    for(int i=0;i<N+1;i++){
        dist[i][i] = 0;
    }

    fw();

    int idx=-1;
    int min_v = 1e9;
    for(int i=1;i<N+1;i++){
        int s = accumulate(dist[i].begin()+1,dist[i].end(),0LL);
        if(min_v > s){
            idx = i;
            min_v = s;
        }
    }

    cout << idx;
    return 0;
}