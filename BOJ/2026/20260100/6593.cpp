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

int dx[6] = {1,0,-1,0,0,0};
int dy[6] = {0,1,0,-1,0,0};
int dz[6] = {0,0,0,0,1,-1};

int L,R,C;

struct Pos {
    int l,r,c;
};

int bfs(vector<vector<vector<char>>> &v, vector<vector<vector<int>>> &visited, Pos& start){
    visited[start.l][start.r][start.c] = 0;
    deque<Pos> q;
    q.push_back(start);
    while (!q.empty()){
        Pos Now = q.front(); q.pop_front();
        rep(i,0,6){
            int nl=Now.l+dz[i];
            int nr=Now.r+dy[i];
            int nc=Now.c+dx[i];
            if(0<=nl && nl < L && 0<=nr && nr < R && 0<=nc && nc <C){
                if(v[nl][nr][nc] != '#'){
                    if (v[nl][nr][nc] == 'E'){
                        return visited[Now.l][Now.r][Now.c] + 1;
                    }
                    if(visited[nl][nr][nc]==-1){ // if not visited
                        visited[nl][nr][nc]=visited[Now.l][Now.r][Now.c] + 1;
                        q.push_back({nl,nr,nc});
                    }
                }
            }
        }
    }
    return -1;
}

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);

    while (true)
    {
        cin>>L>>R>>C;
        if (!L && !R && !C) break;

        vector<vector<vector<char>>> v (L, vector<vector<char>>(R,vector<char>(C,-1)));
        vector<vector<vector<int>>> visited (L, vector<vector<int>>(R,vector<int>(C,-1)));

        Pos start;
        rep(i,0,L){
            rep(j,0,R){
                rep(k,0,C){
                    char t;cin>> t;
                    v[i][j][k]=t;
                    if(t=='S'){
                        start.l=i;start.r=j;start.c=k;
                    }
                }
            }
        }

        int res = bfs(v,visited,start);
        if (res==-1){
            cout<<"Trapped!\n";
        } else {
            cout << "Escaped in " << res << " minute(s).\n";
        }
    }
    return 0;
}