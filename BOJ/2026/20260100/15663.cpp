#include<bits/stdc++.h>
#include<iostream>
using namespace std;

int N,M;
vector<int> v{};
vector<int> res{};
vector<bool> visited{};

void dfs(){
    if (size(res)==M){
        for(const auto &e:res){
            cout << e << " ";
        }
        cout << "\n";
        return;
    }
    int last=-1;
    for(int i=0;i<N;i++){
        if(!visited[i] && v[i]!=last){
            visited[i] = true;
            res.push_back(v[i]);
            last = v[i];
            dfs();
            visited[i]=false;
            res.pop_back();
        }
    }
}

int main(){
    ios::sync_with_stdio(0);
    cin.tie(0);

    cin>>N>>M;
    for(int i=0;i<N;i++){
        int x; cin >>x;
        v.push_back(x);
    }

    sort(v.begin(),v.end());
    for(int i=0;i<size(v);i++){
        visited.push_back(false);
    }

    dfs();
}