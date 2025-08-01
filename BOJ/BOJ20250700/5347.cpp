#include <iostream>
#include <bits/stdc++.h>

using namespace std;

int gcd(int a,int b){
    if (b==0) return a;
    return gcd(b,a%b);
}

int main() {
	cin.tie(0); cout.tie(0);
	ios::sync_with_stdio(0);
    long long t;
    cin >> t;
    while(t--){
        long long a,b;
        cin >>a>>b;
        long long g=gcd(a,b);
        cout << a*b/g << "\n";
    }
	return 0;
}