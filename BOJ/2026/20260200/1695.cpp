#include <bits/stdc++.h>
using namespace std;

int dp[5001][5001];

void print_v(int N){
    for(int i=0;i<N;i++){
        for(int j=0;j<N;j++){
            cout << dp[i][j] << " ";
        }
        cout << "\n";
    }
    cout << "\n";
}

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);

    int N;cin>>N;
    vector<int> v;
    for(int i=0;i<N;i++){
        int x;cin>>x;
        v.push_back(x);
    }

    for(int j=1;j<N;j++){
        for(int i=j-1;i>=0;i--){
            if (v[i]==v[j]){
                dp[i][j] = dp[i+1][j-1];
            } else {
                dp[i][j] = min(dp[i+1][j],dp[i][j-1]) + 1;
            }
        }
    }
    cout << dp[0][N-1];

    return 0;
}