#include <bits/stdc++.h>
using namespace std;

int V,E;

struct Edge
{
    int vertex,weight;
    bool operator<(const Edge& other) const{
        return weight > other.weight;
    }
};

vector<vector<Edge>> g;
vector<int> dist;
vector<int> parent;

void djikstra(int start){
    priority_queue<Edge> pq;
    dist[start]=0;
    pq.push({start,0});

    while (!pq.empty())
    {
        //pop
        Edge curr = pq.top(); pq.pop();
        // check
        if (dist[curr.vertex] < curr.weight){
            continue;
        }
        // relaxation
        for(const auto& next:g[curr.vertex]){
            if (next.weight + curr.weight < dist[next.vertex]){
                dist[next.vertex] = next.weight + curr.weight;
                parent[next.vertex] = curr.vertex;
                pq.push({next.vertex,dist[next.vertex]}); 
            }
        }
    }
}

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);

    cin>>V>>E;
    g.assign(V+1,vector<Edge> {});
    dist.assign(V+1,1e9);
    parent.assign(V+1,-1);

    int start; cin>>start;
    for(int i=0;i<E;i++){
        int u,v,w; cin>>u>>v>>w;
        g[u].push_back({v,w});
    }

    djikstra(start);

    for(int i=1;i<V+1;i++){
        if (dist[i]==1e9){
            cout << "INF\n";
        } else {
            cout << dist[i] << "\n";
        }
    }

    return 0;
}