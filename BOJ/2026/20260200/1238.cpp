#include <bits/stdc++.h>
using namespace std;

struct Edge{
    int v,cost;

    bool operator<(const Edge&other)const{
        return cost > other.cost;
    }
};

int N,M,X;
vector<vector<Edge>> g1;
vector<vector<Edge>> g2;
vector<int> dist1;
vector<int> dist2;

void dijkstra(int start, vector<vector<Edge>> &g, vector<int> &dist){
    priority_queue<Edge> pq;
    dist[start] = 0;
    pq.push({start,0});

    while (!pq.empty()){
        //pop
        Edge curr = pq.top();pq.pop();
        //check
        if(dist[curr.v] < curr.cost) continue;
        //relaxation
        for(const auto &next:g[curr.v]){
            if(dist[next.v] > curr.cost + next.cost){
                dist[next.v] = curr.cost + next.cost;
                pq.push({next.v,dist[next.v]});
            }
        }
    }    
}

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);

    cin>>N>>M>>X;
    g1.resize(N+1, vector<Edge> (0));
    g2.resize(N+1, vector<Edge> (0));
    dist1.resize(N+1,1e9);
    dist2.resize(N+1,1e9);

    for(int i=0;i<M;i++){
        int a,b,c;cin>>a>>b>>c;
        g1[a].push_back({b,c});
        g2[b].push_back({a,c});
    }
    
    dijkstra(X,g1,dist1);
    dijkstra(X,g2,dist2);
    int mx = 0;
    for(int i=1;i<N+1;i++){
        mx = max(mx,dist1[i]+dist2[i]);
    }
    cout << mx;

    return 0;
}