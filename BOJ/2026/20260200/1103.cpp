#include <bits/stdc++.h>
using namespace std;

int N,M;
vector<vector<char>> g;
vector<vector<int> visited;

struct Pos{
    int y,x;
};

bool Pos_valid(Pos p){
    return ((0<=p.y && p.y<N) && (0<=p.x && p.x<M));
}

int dy[4] = {1,0,-1,0};
int dx[4] = {0,1,0,-1};

int dfs(Pos now){
    if (g[now.y][now.x] == 'H') return 0;

    for(int i=0;i<4;i++){
        int mv = g[now.y][now.x] - '0';
        int ny = now.y + dy[i] * mv;
        int nx = now.x + dx[i] * mv;
        if(!Pos_valid({ny,nx})) continue;
        dfs({ny,nx});
    }
}

// int bfs(Pos start){
//     deque<Pos> q;
//     q.push_back(start);
//     visited[start.y][start.x] = 0;

//     while (!q.empty())
//     {
//         Pos now = q.front(); q.pop_front();
//         for(int i=0;i<4;i++){
//             int mv = 0;
//             if(board[now.y][now.x] == 'H'){
//                 continue;
//             } else {
//                 mv = board[now.y][now.x] - '0';
//             }
//             int ny = now.y + dy[i]*mv;
//             int nx = not.x + dx[i]*mv;

//             if(Pos_valid({ny,nx}) && (visited[ny][nx] == -1)){
//                 q.push_back({ny,nx});
//                 visited[ny][nx] = visited[now.y][now.x]+1;
//             }
//         }
//     }

    return
}


int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);

    cin>>N>>M;
    g.assign(N,vector<int> (M,0));
    visited.assign(N,vector<int> (M,-1));

    for(int i=0;i<N;i++){
        string s; cin>>s;
        for(int j=0;j<M;j++){
            g[i][j] = s[j];
        }
    }


    int res = bfs({0,0});

    return 0;
}