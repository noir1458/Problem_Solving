#include <bits/stdc++.h>
using namespace std;

int H,W;
vector<vector<char>> board;
vector<vector<int>> visited;

int dy[4] = {1,0,-1,0};
int dx[4] = {0,1,0,-1};

bool Pos_valid(int y, int x){
    return (0<=y && y<H) && (0<=x && x<W);
}

bool touch_border(int y,int x){
    return (y==0 || y==H-1 || x==0 || x==W-1);
}

bool bfs(int i, int j){
    bool is_touch = false;
    if(touch_border(i,j)) is_touch=true;

    visited[i][j] =1;
    deque<pair<int,int>> q;
    q.push_back({i,j});

    while (!q.empty())
    {
        auto [now_y,now_x] = q.front();q.pop_front();
        for(int i=0;i<4;i++){
            int ny = now_y + dy[i];
            int nx = now_x + dx[i];
            if(Pos_valid(ny,nx)){
                if (!visited[ny][nx] && board[ny][nx]=='.'){
                    visited[ny][nx] = 1;
                    q.push_back({ny,nx});
                    if(touch_border(ny,nx)){
                        is_touch = true;
                    }
                }
            }
        }
    }
    return (is_touch)?false:true;
}

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);

    cin>>H>>W;
    board.assign(H,vector<char> (W));
    visited.assign(H, vector<int> (W));

    for(int i=0;i<H;i++){
        string s;cin>>s;
        for(int j=0;j<W;j++){
            board[i][j] = s[j];
        }
    }

    int c=0;
    for(int i=0;i<H;i++){
        for(int j=0;j<W;j++){
            if(board[i][j]=='.' && !visited[i][j] && bfs(i,j)){
                c++;
            }
        }
    }
    cout << c;

    return 0;
}