#include <bits/stdc++.h>
using namespace std;

int n,m;
struct Edge{
    int vertex,cost;
    bool operator<(const Edge &other) const{
        return cost > other.cost;
    }
};

vector<vector<Edge>> g;
vector<int> dist;
vector<int> parent;

void dijkstra(int start, int end){
    priority_queue<Edge, vector<Edge>> pq;
    pq.push({start,0});

    while (!pq.empty()){
        // pop
        Edge curr = pq.top(); pq.pop();
        // check
        if (curr.cost > dist[curr.vertex]) continue;
        // relaxation
        for(const auto &next:g[curr.vertex]){
            if(dist[next.vertex] > curr.cost + next.cost){
                dist[next.vertex] = curr.cost + next.cost;
                parent[next.vertex] = curr.vertex;
                pq.push({next.vertex,dist[next.vertex]});
            }
        }
    }
}

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);

    cin >> n >> m;

    g.resize(n+1,vector<Edge> (0));
    dist.resize(n+1,1e9);
    parent.resize(n+1, -1);

    for(int i=0;i<m;i++){
        int a,b,c; cin>>a>>b>>c;
        g[a].push_back({b,c});
    }

    int start,end; cin>>start>>end;
    dist[start] = 0;
    dijkstra(start,end);

    cout << dist[end] << "\n";

    vector<int> res;
    for(int i=end;i!=-1;i=parent[i]){
        res.push_back(i);
    }
    reverse(res.begin(),res.end());
    cout << size(res) << "\n";
    for(const auto &e:res){
        cout << e << " ";
    }

    return 0;
}