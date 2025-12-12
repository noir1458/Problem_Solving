#include<bits/stdc++.h>
#include<iostream>
using namespace std;

int R,C;
int INF = 987654321;
int dy[4] = {1,0,-1,0};
int dx[4] = {0,1,0,-1};

void bfs_f(vector<vector<char>> &board, vector<vector<int>> &visited_f){
    deque <tuple<int,int,int>> q;

    for (int i=0;i<R;i++){
        for (int j=0;j<C;j++){
            if (board[i][j] == 'F'){
                q.push_back({i,j,0});
                visited_f[i][j] = 0;
            }
        }
    }

    while(!q.empty()){
        auto[ny,nx,t] = q.front(); q.pop_front();

        for(int i=0;i<4;i++){
            int y=ny+dy[i];
            int x=nx+dx[i];
            if(y >= 0 && y < R && x>= 0 && x < C){
                if (board[y][x] != '#') {
                    if (visited_f[y][x] == INF){
                        visited_f[y][x] = t+1; 
                        q.push_back({y,x,t+1});
                    }
                }
            }
        }
    }
}

int bfs(vector<vector<char>> &board, vector<vector<int>> &visited_f, vector<vector<int>> &visited_j){
    deque<tuple<int,int,int>> q;

    for (int i=0;i<R;i++){
        for (int j=0;j<C;j++){
            if (board[i][j] == 'J'){
                q.push_back({i,j,0});
                visited_j[i][j] = true;
            }
        }
    }

    while (!q.empty()){
        auto[ny,nx,t] = q.front();
        q.pop_front();

        for(int i=0;i<4;i++){
            int y = ny + dy[i];
            int x = nx + dx[i];
            if (!(y >= 0 && y < R && x>= 0 && x < C)){
                return t+1;
            } else {
                if (!visited_j[y][x] && board[y][x] != '#' && board[y][x] != 'F'){
                    if (t+1 < visited_f[y][x]){
                    visited_j[y][x] = true;
                    q.push_back({y,x,t+1});
                    }
                }
            }
        }
    }
    return -1;
}

int main(){
    ios::sync_with_stdio(0);
    cin.tie(0); cout.tie(0);
    
    cin >> R >> C;
    vector<vector<char>> board;
    for(int i=0;i<R;i++){
        vector<char> v;
        for(int j=0;j<C;j++){
            char x;
            cin >> x;
            v.push_back(x);
        }
        board.push_back(v);
    }

    vector<vector<int>> visited_f(R,vector<int>(C,INF));
    vector<vector<int>> visited_j(R,vector<int>(C,0));

    bfs_f(board,visited_f);
    int res = bfs(board, visited_f, visited_j);
    if (res==-1){
        cout << "IMPOSSIBLE";
    } else {
        cout << res;
    }
}