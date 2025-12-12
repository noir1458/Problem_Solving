#include<bits/stdc++.h>
#include<iostream>
using namespace std;

int R,C;
int dy[4] = {1,0,-1,0};
int dx[4] = {0,1,0,-1};

int bfs(vector<vector<char>> &board, vector<vector<bool>> &visited){
    deque<tuple<char,int,int,int>> q;
    pair<int,int> tmp_j;

    for (int i=0;i<R;i++){
        for (int j=0;j<C;j++){
            if (board[i][j] == 'F'){
                q.push_back({'F',i,j,0});
            }
            if (board[i][j] == 'J'){
                tmp_j.first = i;
                tmp_j.second = j;
                visited[i][j] = true;
            }
        }
    }
    // J 위치만 나중에 처리해야함
    q.push_back({'J',tmp_j.first,tmp_j.second,0});

    while (!q.empty()){
        auto[c,ny,nx,t] = q.front();
        q.pop_front();

        for(int i=0;i<4;i++){
            int y = ny + dy[i];
            int x = nx + dx[i];
            if (c=='F'){
                // 불이 확산할때
                if (y >= 0 && y < R && x>= 0 && x < C){
                    if (board[y][x] != '#' && board[y][x] != 'F'){
                        // visited 신경쓰지 않고 일단 태워보자
                        board[y][x] = 'F';
                        q.push_back({c,y,x,t+1});
                    }
                }
            } else {
                if (!(y >= 0 && y < R && x>= 0 && x < C)){
                    return t+1;
                } else {
                    if (!visited[y][x] && board[y][x] != '#' && board[y][x] != 'F'){
                        visited[y][x] = true;
                        q.push_back({c,y,x,t+1});
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

    vector<vector<bool>> visited;
    for(int i=0;i<R;i++){
        vector<bool> v(C);
        visited.push_back(v);
    }
    int res = bfs(board, visited);
    if (res==-1){
        cout << "IMPOSSIBLE";
    } else {
        cout << res;
    }
}