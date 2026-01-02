#include <iostream>
#include <bits/stdc++.h>

typedef long long ll;

using namespace std;

int main() {
	cin.tie(0); cout.tie(0);
	ios::sync_with_stdio(0);
    
    ll N;
    cin >> N;
    if ((N%4)%2==1){
        cout << "SK";
    } else {
        cout << "CY";
    }
	return 0;
}