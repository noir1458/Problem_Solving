#include <bits/stdc++.h>
using namespace std;

using ll = long long;

int n;
vector<unordered_map<ll,int>> v;

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);

    cin>>n;
    v.assign(n, {});
    for(int i=0;i<n;i++){
        int m;cin>>m;
        for(int j=0;j<m;j++){
            ll x;cin>>x;
            v[i][x]++;
        }

        // 순회를 돌고, 절반초과하는것 출력
        bool res_find = false;
        ll res=-1;
        for(const auto &e:v[i]){
            if (e.second > m/2){
                res = e.first;
                res_find = true;
            }
        }
        
        if (!res_find){
            cout << "SYJKGW\n";
        } else {
            cout << res << '\n';
        }
    }

    return 0;
}