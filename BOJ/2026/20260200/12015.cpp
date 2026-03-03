#include <bits/stdc++.h>
using namespace std;

int N;
vector<int> v;
vector<int> L;


int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);

    cin>>N;
    v.assign(N,0);
    for(int i=0;i<N;i++){
        cin >> v[i];
    }

    for(int i=0;i<N;i++){
        int val = v[i];
        
        if(L.empty() || L.back() < val){
            // 연장
            L.push_back(val);
        } else{
            // 최적화
            auto it = lower_bound(L.begin(),L.end(), val);
            *it = val;
        }
    }

    cout << size(L);
    
    return 0;
}