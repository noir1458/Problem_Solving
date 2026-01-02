#include <iostream>
#include <bits/stdc++.h>

using namespace std;

int main() {
	cin.tie(0); cout.tie(0);
	ios::sync_with_stdio(0);
    string s;
    while(1){
        getline(cin,s);
        if (s=="END")break;
        for(int i=s.length()-1;i>=0;i--){
            cout << s[i];
        }
        cout << "\n";
    }
	return 0;
}