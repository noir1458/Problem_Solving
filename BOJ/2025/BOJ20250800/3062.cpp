#include <iostream>
#include <bits/stdc++.h>

using namespace std;

int is_valid(string s){
	for(int i=0;i<s.length()/2;i++){
		if (s[i]!=s[s.length()-1-i]) return 0;
	}
	return 1;
}

string s_rev(string s){
	string tmp="";
	for(int i=s.length()-1;i>=0;i--){
		tmp += s[i];
	}
	return tmp;
}

int main() {
	cin.tie(0); cout.tie(0);
	ios::sync_with_stdio(0);
	int t;
	cin >> t;
	while (t--){
		string s;
		cin >> s;
		string tmp = to_string(stoi(s) + stoi(s_rev(s)));
		if (is_valid(tmp))
		cout << "YES\n";
		else
		cout << "NO\n";
	}
	
	return 0;
}