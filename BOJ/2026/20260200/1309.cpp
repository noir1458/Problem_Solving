#include <bits/stdc++.h>
using namespace std;

const int MOD_NUM = 9901;
int N;
vector<vector<int>> dp; 

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);

    cin>>N;
    dp.assign(N+1, vector<int> (3));
    // dp[i][0] = i번 줄에 사자 안놓은 경우의수
    // dp[i][1] = 왼쪽만
    // dp[i][2] = 오른쪽만

    fill(dp[1].begin(), dp[1].end(), 1);
    for(int i=2;i<N+1;i++){
        dp[i][0] = (dp[i-1][0] + dp[i-1][1] + dp[i-1][2]) % MOD_NUM;
        dp[i][1] = (dp[i-1][0] + dp[i-1][2]) % MOD_NUM;
        dp[i][2] = (dp[i-1][0] + dp[i-1][1]) % MOD_NUM;
    }

    cout << accumulate(dp[N].begin(),dp[N].end(),0) %MOD_NUM;

    return 0;
}