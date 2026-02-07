#include <bits/stdc++.h>
using namespace std;

struct cost_addCustomer
{
    int cost,customer;
};


int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);

    vector<cost_addCustomer> v;
    int C,N;cin>>C>>N;
    for(int i=0;i<N;i++){
        int a,b;cin>>a>>b;
        v.push_back({a,b});
    }

    // dp[고객수] = 최소 비용
    vector<int> dp(C+100,1e9);
    dp[0] = 0;
    for(int i=0;i<N;i++){
        for(int j=v[i].customer;j<C+100;j++){
            dp[j] = min(dp[j],dp[j-v[i].customer] + v[i].cost);
        }   
    }
    cout << *min_element(dp.begin()+C,dp.end());


    return 0;
}