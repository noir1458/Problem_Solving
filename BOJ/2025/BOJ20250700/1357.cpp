#include <iostream>
#include <bits/stdc++.h>

using namespace std;
string Rev(string& s){
    string t{};
    for (int i=s.length()-1;i>=0;i--){
        t += s[i];
    }
    return t;
}

int main() {
	cin.tie(0); cout.tie(0);
	ios::sync_with_stdio(0);
    string s1,s2;
    cin >> s1 >> s2;
    string tmp = to_string(stoi(Rev(s1)) + stoi(Rev(s2))); //int
    cout << stoi(Rev(tmp));
	return 0;
}