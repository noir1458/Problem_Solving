#include <bits/stdc++.h>
using namespace std;

int N,res;
vector<vector<int>> g;
vector<int> parent;

void dfs(int now){
    if(size(g[now])==0){
        res++; return;
    }
    for(const auto&next:g[now]){
        dfs(next);
    }
}

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);

    cin >> N;
    g.assign(N,vector<int> (0));
    parent.assign(N,-1);
    int root;

    for(int i=0;i<N;i++){
        int t;cin>>t;
        parent[i]=t;
        if (t==-1) root = i;
        //g[p].push_back(i);
    }

    int x; cin>>x;
    if(x==root){
        cout<<0;return 0;
    }

    for(int i=0;i<N;i++){
        if (i!=x && parent[i]!=-1) g[parent[i]].push_back(i);
    }

    dfs(root);
    cout << res;

    return 0;
}