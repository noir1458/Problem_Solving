#include <bits/stdc++.h>
using namespace std;

int N;
vector<vector<int>> g;
vector<bool> visited;
vector<int> apple;

int dfs(int start){
    int c=apple[start];
    deque<int> q;
    q.push_back(start);
    visited[start] = true;

    while (!q.empty()){
        int now = q.front();q.pop_front();
        for(const auto&e:g[now]){
            if(visited[e]==false){
                q.push_back(e);
                visited[e]=true;
                c+=apple[e];
            }
        }
    }
    return c;
}

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);

    cin>>N;
    g.assign(N+1,vector<int> (0)); // 0번버림
    apple.assign(N+1,0);
    for(int i=1;i<N+1;i++){
        cin >> apple[i];
    }
    for(int i=0;i<N-1;i++){
        int a,b;cin>>a>>b;
        g[a].push_back(b);
        g[b].push_back(a);
    }

    int res= 0;
    int idx = -1;
    for(int i=1;i<N+1;i++){
        visited.assign(N+1,false);
        int tmp = dfs(i);
        if (res < tmp){
            res = tmp;
            idx = i;
        }
    }
    cout << res << " " << idx; 
    return 0;
}