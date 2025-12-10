#include<bits/stdc++.h>
#include<iostream>
using namespace std;

int n,m;
int dy[4] = {1,0,-1,0};
int dx[4] = {0,1,0,-1};

int bfs(vector<vector<int>> &board, vector<vector<bool>> &visited, int y,int x){
    deque<pair<int,int>> q;
    q.push_back({y,x});
    visited[y][x]=true;
    int t=1;

    while (!q.empty()){
        auto [Y,X] = q.front(); q.pop_front();
        for(int i=0;i<4;i++){
            int ny = Y + dy[i];
            int nx = X + dx[i];
            if (ny < 0 || ny >= n || nx < 0 || nx >= m) continue;
            if (visited[ny][nx] || board[ny][nx] != 1) continue;
            visited[ny][nx] = true;
            t++;
            q.push_back({ny,nx});
        }
    }
    return t;
}

int main(){
    ios::sync_with_stdio(0);
    cin.tie(0);cout.tie(0);

    cin>>n>>m;
    vector<vector<int>> board;
    for(int i=0;i<n;i++){
        vector<int> row;
        int x;
        for(int j=0;j<m;j++){
            cin >> x;
            row.push_back(x);
        }
        board.push_back(row);
    }

    vector<vector<bool>> visited;
    for(int i=0;i<n;i++){
        vector<bool> row(m);
        visited.push_back(row);
    }

    int c=0;
    int p=0;
    for(int i=0;i<n;i++){
        for(int j=0;j<m;j++){
            if(!visited[i][j] && board[i][j]==1){
                p++;
                int a = bfs(board,visited,i,j);
                if (a>c) c=a;
            }
        }
    }
    cout << p << "\n" << c;
}