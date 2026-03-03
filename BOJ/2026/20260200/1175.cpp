#include <bits/stdc++.h>
using namespace std;

int dy[4] = {1,0,-1,0};
int dx[4] = {0,1,0,-1};

struct Pos
{
    int y,x;
};

struct Pos_
{
    int y,x,dir,p;
};

int N,M;
vector<vector<char>> board;
vector<Pos> gift;
int visited[50][50][5][4]; // y,x,dir,배달여부...

bool pos_valid(Pos now){
    return ((0<=now.y && now.y<N) && (0<=now.x && now.x<M));
}

int bfs(Pos start){
    deque<Pos_> q;
    q.push_back({start.y,start.x,4,0}); // 이전방향 없으므로 4로 처리. 초기배열도 크기 5로 늘린다
    visited[start.y][start.x][4][0] = 0;

    while (!q.empty())
    {
        Pos_ now = q.front();q.pop_front();
        for(int i=0;i<4;i++){
            if (i==now.dir) continue;

            int ny = now.y + dy[i];
            int nx = now.x + dx[i];
            if(pos_valid({ny,nx}) && (board[ny][nx] != '#') && (visited[ny][nx][i][now.p]==-1)){
                if (board[ny][nx]== 'C'){
                    // C만남
                    int next_p = now.p;
                    for(int id=0;id<2;id++){
                        if(ny==gift[id].y && nx==gift[id].x)
                            next_p = next_p | (1<<id);
                    }
                    visited[ny][nx][i][next_p] = visited[now.y][now.x][now.dir][now.p] +1;
                    
                    if (next_p==3){
                        return visited[ny][nx][i][next_p];
                    }
                    q.push_back({ny,nx,i,next_p});
                } else {
                    // C 안만남
                    visited[ny][nx][i][now.p] = visited[now.y][now.x][now.dir][now.p] + 1;
                    q.push_back({ny,nx,i,now.p});
                }
            }
        }
    }
    return -1;
}

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);

    cin>>N>>M;
    board.assign(N,vector<char> (M,' '));
    for(int i=0; i<50; ++i)
        for(int j=0; j<50; ++j)
            for(int d=0; d<5; ++d)
                for(int b=0; b<4; ++b)
                    visited[i][j][d][b] = -1;
    Pos start = {};

    for(int i=0;i<N;i++){
        string s;cin>>s;
        for(int j=0;j<M;j++){
            board[i][j] = s[j];
            if(s[j]=='S'){
                start = {i,j};
            }
            if(s[j] == 'C'){
                gift.push_back({i,j});
            }
        }
    }
    cout << bfs(start);
    return 0;
}