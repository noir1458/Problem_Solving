#include <bits/stdc++.h>
using namespace std;

int N,M;

struct Edge {
    int V,C;
    bool operator<(const Edge&other) const{ 
        // pq안에서 < 사용해 정렬, max heap이 기본
        return C>other.C; // 내 cost 가 크면 참이 되도록
    }
};

vector<vector<Edge>> g;
vector<int> dist;

void djkstra(int start, int end){
    priority_queue<Edge, vector<Edge>> pq;
    pq.push({start,0});

    while(!pq.empty()){
        // pop
        Edge curr = pq.top(); pq.pop();
        // check
        if (dist[curr.V]<curr.C) continue; 
        // Relaxation
        for(const auto& e : g[curr.V]){
            if (dist[e.V] > curr.C + e.C){
                dist[e.V] = curr.C + e.C;
                pq.push({e.V, dist[e.V]});
            }
        }
    }
}

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);

    cin>>N>>M;
    g.resize(N+1, vector<Edge> (0)); // 0번 버림
    dist.assign(N+1,1e9);

    for(int i=0;i<M;i++){
        int a,b,c; cin>>a>>b>>c;
        g[a].push_back({b,c});
    }

    int a,b; cin>>a>>b;
    dist[a]=0;
    djkstra(a,b);

    cout << dist[b];

    return 0;
}