#include <iostream>
#include <bits/stdc++.h>

using namespace std;

int dy[4] = {1,0,-1,0};
int dx[4] = {0,1,0,-1};

int dfs(int a, int b,int c, vector<vector<pair<int,int>>> &g, vector<bool> &visited){
    if(a==b){
        return c;
    }
    for(int i=0;i<g[a].size();i++){
        int next = g[a][i].first;
        int weight = g[a][i].second;
        if(visited[next] == false){
            visited[next] = true;
            int result = dfs(next,b, c+weight,g,visited);
            if(result != -1) return result;
            visited[next] = false;
        }
    }
    return -1;
}

int main() {
	cin.tie(0); cout.tie(0);
	ios::sync_with_stdio(0);

    vector<vector<pair<int,int>>> g;
    int N,M;
    cin >> N >> M; // n개 노드, m개 쌍

    for(int i=0;i<N+1;i++){ // 0번 버리고 n+1개 넣기
        vector<pair<int,int>> t;
        g.push_back(t);
    }

    for(int i=0;i<N-1;i++){
        int a,b,w;
        cin >> a >> b >> w;
        g[a].push_back({b,w});
        g[b].push_back({a,w});
    }
    for(int i=0;i<M;i++){
        vector<bool> visited;
        visited.resize(N+1,false);
        int a,b;
        cin>>a>>b;
        visited[a] = true;
        cout << dfs(a,b,0,g,visited)<<"\n";
    }

	return 0;
}