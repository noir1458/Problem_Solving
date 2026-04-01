#include <bits/stdc++.h>
using namespace std;

vector<vector<int>> v;
vector<int> indeg;
int N,M;

deque<int> q;
vector<int> res;

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);

    cin>>N>>M;
    v.assign(N+1,vector<int> {});
    indeg.assign(N+1,0);

    for(int i=0;i<M;i++){
        int a,b;cin>>a>>b;
        v[a].push_back(b);
        indeg[b]++;
    }

    // indeg == 0 에서 시작
    for(int i=1;i<N+1;i++){
        if (indeg[i]==0){
            q.push_back(i);
        }
    }

    // q가 비게 될때까지 진행, 방문시 indeg-- , indeg == 0 되면 q에 넣는다
    while (!q.empty())
    {
        int cur = q.front();q.pop_front();
        res.push_back(cur);
        for(int nxt:v[cur]){
            indeg[nxt]--;
            if(indeg[nxt]==0){
                q.push_back(nxt);
            }
        }
    }

    // 최종적으로 len(res) == n 체크, 아니라면 cycle exist
    if(size(res) != N){
        cout<<"Cycle exist";
    } else {
        for(auto e: res){
            cout << e << " ";
        }
    }

    return 0;
}