#include <bits/stdc++.h>
using namespace std;

using ll = long long;
ll N;
vector<int>v;

int cnt[500001];
int suff[500001];


int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);

    cin>>N;
    for(int i=0;i<N;i++){
        int x;cin>>x;
        v.push_back(x);
        cnt[x]++;
    }
    int max_v = *max_element(v.begin(),v.end());

    suff[max_v] = cnt[max_v];
    for(int i=max_v;i>0;i--){
        suff[i] = cnt[i] + suff[i+1];
    }
    
    for(int i=0;i<size(cnt)-1;i++){
        suff[i+1] += suff[i]/10;
        suff[i] %= 10;
    }

    bool pr = false;
    for(int i=size(cnt)-1;i>0;i--){
        if (suff[i]!=0){
            pr = true;
        }
        if(pr) cout << suff[i];
    }

    return 0;
}