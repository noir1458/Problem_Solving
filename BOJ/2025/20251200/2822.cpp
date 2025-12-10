#include<bits/stdc++.h>
using namespace std;
bool cmp(pair<int,int> &a, pair<int,int> &b){
    if (a.first != b.first) return a.first > b.first;
    return a.second < b.second;
}

int main(){
    ios::sync_with_stdio(0);cin.tie(0);cout.tie(0);
    vector<pair<int,int>> v;
    for(int i=0;i<8;i++){
        int x; cin>>x;
        v.push_back({x,i+1});
    }
    sort(v.begin(), v.end(), cmp);
    vector<int> v2;
    int res=0;

    for (int i=0;i<5;i++){
        auto [n,j] = v[i];
        res += n;
        v2.push_back(j);
    }
    cout << res << "\n";
    sort(v2.begin(),v2.end());
    for(auto e:v2){
        cout << e << " ";
    }
}