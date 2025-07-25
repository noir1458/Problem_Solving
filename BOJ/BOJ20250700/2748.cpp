#include <iostream>
#include <bits/stdc++.h>

using namespace std;

int main() {
	cin.tie(0); cout.tie(0);
	ios::sync_with_stdio(0);
    long long n;
    cin >>n;
    vector<long> v;
    v.push_back(0);v.push_back(1);
    for(int i=2;i<=n;i++){
        v.push_back(v[i-2]+v[i-1]);
    }
    cout << v.back();
	return 0;
}