#include <bits/stdc++.h>
using namespace std;

using ll = long long;
using pii = pair<int, int>;
using pll = pair<ll, ll>;

const int INF = 1e9;
const ll LINF = 1e18;
const int MOD = 998244353; // or 1e9 + 7

#define rep(i, a, b) for (int i = (a); i < (b); ++i)
#define all(x) (x).begin(), (x).end()

int dy[4] = {1,0,-1,0};
int dx[4] = {0,1,0,-1};
int M,N,K;

void print_v(vector<vector<int>> &board){
    for(auto e:board){
        for(auto e2:e){
            cout << e2 << " ";
        }
        cout << "\n";
    }
    cout << "\n";
}

int bfs(vector<vector<int>> &board, vector<vector<int>> &visited, int start_y, int start_x){
    visited[start_y][start_x] = 1;
    deque<pair<int,int>> q;
    q.push_back({start_y,start_x});
    int c=1;
    while (!q.empty()){
        auto [y,x] = q.front(); q.pop_front();
        rep(i,0,4){
            int ny = y+dy[i];
            int nx = x+dx[i];
            if (0<=ny && ny < M && 0<=nx && nx < N){
                if (visited[ny][nx]==0 && board[ny][nx]==0){
                    q.push_back({ny,nx});
                    c++;
                    visited[ny][nx] = 1;
                }
            }
        }
    }
    return c;
}

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);

    cin>>M>>N>>K;
    vector<vector<int>> board(M,vector<int> (N));

    rep(i,0,K){
        // 왼쪽 아래, 오른쪽 위
        int x1,y1,x2,y2; cin>>x1>>y1>>x2>>y2;
        rep(j,y1,y2){ // y2-1, x2-1 까지만 칠해야함
            rep(k,x1,x2){
                board[j][k] = 1;
            }
        }
    }

    // 0 인 영역을 bfs로 카운트
    vector<vector<int>> visited(M,vector<int> (N));
    vector<int> area;
    rep(i,0,M){
        rep(j,0,N){
            if (board[i][j]==0 && visited[i][j]==0){
                int r = bfs(board,visited,i,j);
                area.push_back(r);
            }
        }
    }

    sort(all(area));
    cout << area.size() << "\n";
    for(const auto &e:area) cout << e << " ";

    return 0;
}