#include <bits/stdc++.h>
using namespace std;

int board[9][9];
vector<pair<int,int>> v; // y,x

bool check_y(int y, int x, int v){
    for(int i=0;i<9;i++){
        if(board[y][i]==v){
                return false;
        }
    }
    return true;
}

bool check_x(int y, int x, int v){
    for(int i=0;i<9;i++){
        if(board[i][x]==v){
                return false;
        }
    }
    return true;
}

bool check_9(int y, int x, int v){
    int y_start = (y/3)*3;
    int x_start = (x/3)*3; 
    for(int i=y_start;i<y_start+3;i++){
        for(int j=x_start;j<x_start+3;j++){
                if(board[i][j]==v){
                    return false;
                }
            }
        }
    return true;
}

bool value_valid(int y, int x, int v){
    return (check_y(y,x,v) && check_x(y,x,v) && check_9(y,x,v));
}

void print_board(){
    for(const auto&e:board){
            for(const auto&e2:e){
                cout << e2 << " ";
            }
        cout << "\n";
    }
}

bool dfs(int idx){
    if(idx == size(v)){
    return true;
    }

    for(int i=1;i<10;i++){
        int ny=v[idx].first;
        int nx=v[idx].second;
        if(value_valid(ny,nx,i)){
            board[ny][nx]=i;
            if(dfs(idx+1)) return true;
        }
        board[ny][nx]=0;
    }
    return false;
}

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);

    for(int i=0;i<9;i++){
        for(int j=0;j<9;j++){
            int x;cin>>x;
            board[i][j]=x;
            if(x==0){
                v.push_back({i,j});
            }
        }
    }

    dfs(0);

    print_board();

    return 0;
}