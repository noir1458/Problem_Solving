#include <bits/stdc++.h>
using namespace std;

using ll = long long;

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);

    ll N;cin>>N;
    vector<ll> dp(N+1,0); // 중복 허락
    dp[1] = 1;
    dp[2] = 3;
    for(int i=3;i<N+1;i++){
        dp[i] = dp[i-1] + dp[i-2]*2;
    }

    vector<ll> dp2(N+1,0);
    dp2[1] = 1;
    dp2[2] = 3;
    for(int i=3;i<N+1;i++){
        if (i%2==0){
            dp2[i] = dp[i/2] + dp[(i-2)/2]*2;
        }
        else {
            dp2[i] = dp[(i-1)/2];
        }
    }

    cout << dp2[N] + (dp[N] - dp2[N])/2; // 대칭 + (비대칭 - 대칭)/2

    return 0;
}