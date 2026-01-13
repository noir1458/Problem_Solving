#include<bits/stdc++.h>
#include<iostream>
using namespace std;

#define rep(i,a,b) for(int i = (a);i < (b);++i)

int main(){
    ios::sync_with_stdio(0);
    cin.tie(0);

    int N,M;cin>>N>>M;
    vector<vector<int>> v (N+1,vector<int>(N+1,0));
    vector<vector<int>> s (N+1,vector<int>(N+1,0));
    rep(i,1,N+1){
        rep(j,1,N+1){
            cin>>v[i][j];
        }
    }

    rep(i,1,N+1){
        rep(j,1,N+1){
            s[i][j] = v[i][j] + s[i-1][j] + s[i][j-1] - s[i-1][j-1];
        }
    }

    int x1,y1,x2,y2;
    rep(i,0,M){
        cin>>x1>>y1>>x2>>y2;
        int res = s[x2][y2] - s[x1-1][y2] - s[x2][y1-1] + s[x1-1][y1-1];
        cout << res << "\n";
    }
    return 0;
}