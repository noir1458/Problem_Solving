#include <bits/stdc++.h>
using namespace std;

int N;
vector<int> v;
vector<int> L;

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);

    cin>>N;
    v.resize(N);
    for(int i=0;i<N;i++){
        cin>>v[i];
    }

    for(int i=0;i<N;i++){
        if(L.empty() || L.back() < v[i]){
            L.push_back(v[i]);
        } else {
            auto it = lower_bound(L.begin(),L.end(),v[i]);
            *it = v[i];
        }
    }

    cout << size(L);

    return 0;
}