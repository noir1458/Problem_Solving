#include <iostream>
#include <bits/stdc++.h>

using namespace std;

int main() {
	cin.tie(0); cout.tie(0);
	ios::sync_with_stdio(0);
    int T;
    string s;
    for(cin>>T;T--;){
        cin >> s;
        cout << (s[0] - '0') + (s[2] - '0') << "\n";
    }

	return 0;
}