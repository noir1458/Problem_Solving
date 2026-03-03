#include <bits/stdc++.h>
using namespace std;

int N;
vector<vector<int>> g;
vector<bool> visited;

int bfs(int start){
    visited.assign(N,false);
    deque<pair<int,int>> q; // 좌표, 이동횟수
    q.push_back({start,0});
    visited[start] = true;
    int c = 0;

    while (!q.empty())
    {
        auto [now, move_cnt] = q.front(); q.pop_front();

        if(move_cnt==1) c++;

        if (move_cnt==2){
            c++;
            continue;
        }

        for(int i=0;i<N;i++){
            if (g[now][i] == 1 && !visited[i]){
                visited[i] = true;
                int mv = move_cnt +1;
                q.push_back({i,mv});
            }
        }
    }
    return c;
}

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);

    // 2친구가 많은 사람..?

    // 인접 배열의 형태로 주어짐
    // bfs로 2번만 움직여서 개수세기?
    cin>>N;
    g.assign(N,vector<int> (N));
    for(int i=0;i<N;i++){
        string s; cin>>s;
        for(int j=0;j<N;j++){
            if (s[j]=='Y'){
                g[i][j] = 1;
            } else {
                g[i][j] = 0;
            }
            
        }
    }

    int res = 0;
    for(int i=0;i<N;i++){
        //cout << bfs(i);
        res = max(res, bfs(i));
    }
    
    cout << res;

    return 0;
}