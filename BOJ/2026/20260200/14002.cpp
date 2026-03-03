#include <bits/stdc++.h>
using namespace std;

int N;
vector<int> v;
vector<int> dp;
vector<int> idx;

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);

    cin>>N;
    v.resize(N);
    dp.assign(N,1);
    idx.assign(N,-1);
    for(int i=0;i<N;i++){
        cin>>v[i];
    }

    for(int i=0;i<N;i++){
        for(int j=0;j<i;j++){
            if(v[j] < v[i]){
                if (dp[i] < dp[j] + 1){ 
                dp[i] = dp[j] + 1;
                idx[i] = j;
                }
            }
        }
    }

    cout << *max_element(dp.begin(),dp.end()) << "\n";

    // cout << "\n";
    // for(auto e:dp){
    //     cout << e << " ";
    // }
    // cout << "\n";

    // for(auto e:idx){
    //     cout << e << " ";
    // }
    // cout << "\n";

    vector<int> res;
    int max_idx = max_element(dp.begin(),dp.end()) - dp.begin();
    for(int i=max_idx;i!=-1;i=idx[i]){
        res.push_back(v[i]);
    }
    reverse(res.begin(),res.end());

    for(const auto &e:res){
        cout << e << " ";
    }
    return 0;
}