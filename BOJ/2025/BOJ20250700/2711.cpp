#include <iostream>
#include <bits/stdc++.h>

using namespace std;

int main() {
	cin.tie(0); cout.tie(0);
	ios::sync_with_stdio(0);
    int T;
    for(cin>>T;T--;){
        int i;
        string s;
        cin>>i>>s;
        cout << s.substr(0,i-1) <<s.substr(i,s.length()-1) <<"\n";
    }
	return 0;
}