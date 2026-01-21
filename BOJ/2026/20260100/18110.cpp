#include <bits/stdc++.h>
using namespace std;

using ll = long long;

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);

    ll n;cin>>n;
    if (n==0){
        cout << 0; return 0;
    }
    vector<int> v(n);
    for(int i=0;i<n;i++){
        cin>>v[i];
    }

    sort(v.begin(),v.end());

    double d = n*0.15;
    int d_int = round(d);

    int s = 0;
    for(int i=d_int;i<n-d_int;i++){
        s += v[i];
    }

    double res = (double)s/(n-2*d_int);
    cout << round(res);


    return 0;
}  