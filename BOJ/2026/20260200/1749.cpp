#include <bits/stdc++.h>
using namespace std;

using ll = long long;

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);

    int N,M;cin>>N>>M;
    vector<vector<int>> v(N+1,vector<int> (M+1));
    for(int i=1;i<N+1;i++){
        for(int j=1;j<M+1;j++){
            cin >> v[i][j];
        }
    }

    vector<vector<int>> v2(N+1,vector<int> (M+1)); // 세로 열로 누적합
    for(int i=1;i<N+1;i++){
        for(int j=1;j<M+1;j++){
                v2[i][j] = v2[i-1][j] + v[i][j];
        }
    }

    ll res = -2e18;
    for(int i1=1;i1<N+1;i1++){
        for(int i2=i1;i2<N+1;i2++){
            ll local_sum = 0;
            
            for(int j=1;j<M+1;j++){
                int val = v2[i2][j] - v2[i1-1][j];
                local_sum = max((ll)val, val+local_sum);
                res = max(res,local_sum);
            }
        }
    }
    cout << res;
    return 0;
}