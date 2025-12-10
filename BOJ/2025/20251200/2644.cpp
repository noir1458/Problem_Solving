#include<bits/stdc++.h>
#include<iostream>
using namespace std;

int bfs(vector<vector<int>> &v, vector<int> &visited, int start, int end)
{
    visited[start]=1;
    deque<pair<int,int>> q;
    q.push_back({start,0});
    while(q.size()!=0){
        auto [x,l] = q.front();
        if (x==end) return l;
        q.pop_front();

        for(const auto &e:v[x]){
            if (visited[e] != 1){
                q.push_back({e,l+1});
                visited[e] = 1;
            }
        }
    }
    return -1;
}

int main(){
    ios::sync_with_stdio(0);cin.tie(0);cout.tie(0);
    int n,a,b,k;
    cin >> n >> a >> b >> k;
    vector<vector<int>> v(n+1);
    while (k--)
    {
        int x,y;
        cin>>x>>y;
        v[x].push_back(y);
        v[y].push_back(x);
    }
    vector<int> visited(n+1);
    int res = bfs(v,visited,a,b);
    cout << res;
}