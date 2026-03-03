#include <bits/stdc++.h>
using namespace std;

int N;
vector<int> v;
vector<int> L;
vector<int> idx_v;

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);

    cin>>N;
    v.assign(N,0);
    idx_v.assign(N,0);

    for(int i=0;i<N;i++){
        cin>>v[i];
    }

    for(int i=0;i<N;i++){
        if(L.empty() || L.back() < v[i]){
            L.push_back(v[i]);
            idx_v[i] = size(L)-1;
        } else {
            auto it = lower_bound(L.begin(),L.end(),v[i]);
            *it = v[i];
            idx_v[i] = it - L.begin();
        }
    }

    cout << size(L) << "\n"; 
    vector<int> res;

    int use_idx = size(L)-1;
    for(int i=N-1;i>=0;i--){
        if(idx_v[i] == use_idx){
            res.push_back(v[i]);
            use_idx--;
        }
    }

    reverse(res.begin(),res.end());
    for(auto e:res){
        cout << e <<" ";
    }

    return 0;
}