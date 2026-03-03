#include <bits/stdc++.h>
using namespace std;

int digit_sum(int x){
    string s = to_string(x);
    int res = 0;
    for(const auto&e:s){
        res += (e-'0');
    }
    return res;
}

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);
    
    int N,K;cin>>N>>K;
    //N안남고 digitsum k인거
    vector<int> v;
    for(int i=1;i<N+1;i++){
        if (digit_sum(i)==K){
            v.push_back(i);
        }
    }
    cout << size(v);
    return 0;
}