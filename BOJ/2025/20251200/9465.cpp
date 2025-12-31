#include<bits/stdc++.h>
#include<iostream>
using namespace std;

int main(){
    ios::sync_with_stdio(0);
    cin.tie(0);cout.tie(0);

    int c; cin>>c;
    while (c--)
    {
        int n; cin >> n;
        vector<vector<int>> v(2,vector<int>(n));
        for(int j=0;j<2;j++){            
            for(int i=0;i<n;i++){
                cin >> v[j][i];
            }
        }
        vector<vector<int>> dp(2,vector<int>(n,-1e9));
        dp[0][0] = v[0][0];
        dp[1][0] = v[1][0];

        dp[0][1] = v[0][1] + dp[1][0];
        dp[1][1] = v[1][1] + dp[0][0];

        for(int i=2;i<n;i++){
            dp[0][i] = v[0][i] + max(dp[1][i-1], dp[1][i-2]);
            dp[1][i] = v[1][i] + max(dp[0][i-1], dp[0][i-2]);
        }
        cout << max(dp[0][n-1],dp[1][n-1])<<"\n";
    }
}