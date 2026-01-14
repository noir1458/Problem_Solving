#include <bits/stdc++.h>
using namespace std;

using ll = long long;
using pii = pair<int, int>;
using pll = pair<ll, ll>;

const int INF = 1e9;
const ll LINF = 1e18;
const int MOD = 998244353; // or 1e9 + 7

#define rep(i, a, b) for (int i = (a); i < (b); ++i)
#define all(x) (x).begin(), (x).end()

bool sieve[1000001];

void func(int N, vector<int> &prime){
    int res = 0;
    for(auto p: prime){
        if (p > N/2) break;
        if(sieve[N-p]){
            res ++;
        }
    }
    cout << res << "\n";
}

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);

    fill(sieve,sieve+1000001,true);
    sieve[0]=sieve[1]=false;

    for(int i=2;i*i<1000001;i++){
        if (sieve[i]){
            for(int j=i*i;j<1000001;j+=i){
                sieve[j]=false;
            }
        }
    }

    vector<int> prime;
    rep(i,0,1000001){
        if(sieve[i])
        prime.push_back(i);
    }

    int n;cin>>n;
    while (n--){
        int a; cin >> a;
        func(a, prime);
    }
    

    return 0;
}