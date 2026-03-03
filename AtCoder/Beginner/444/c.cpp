#include <bits/stdc++.h>
using namespace std;

using ll = long long;
ll N;

void func_L(vector<ll> &vL, ll S, ll max_v){
    ll n = S;
    for(ll i=(N+1)/2;i<=N;i++){
        if(S%i==0){
            ll t=S/i;
            if(t>=max_v){
                vL.push_back(t);
            }
        }
    }
    sort(vL.begin(),vL.end());
    vL.erase(unique(vL.begin(),vL.end()),vL.end());
}

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);

    cin>>N;
    vector<ll> v(N);
    for(ll i=0;i<N;i++){
        cin>>v[i];
    }

    ll S = 0;
    for(const auto &e:v) S += e;
    //cout << S;

    vector<ll> vL;
    func_L(vL,S,*max_element(v.begin(),v.end()));

    sort(v.begin(),v.end());

    vector<ll> res;
    for(int i=0;i<size(vL);i++){
        // vL 안의 것으로 합이 되나
        int l=0,r=size(v)-1;

        ll K = S/vL[i];
        bool possible = true;

        if (v[r] > vL[i]) break;

        while (l<=r){
            if (v[r]==vL[i]){
                r--;
                K--;
                continue;
            }

            if(l<r && v[l]+v[r] == vL[i]){
                l++; r--;
                K--;
            }
            else {
                possible=false;
                break;
            }
        }
        if (possible && K==0){
            res.push_back(vL[i]);
        }
    }

    for(const auto &e:res){
        cout << e << " ";
    }
    
}