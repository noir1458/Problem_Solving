#include <iostream>
#include <bits/stdc++.h>

using namespace std;

int main() {
	cin.tie(0); cout.tie(0);
	ios::sync_with_stdio(0);

    string s;
    cin >> s;
    vector<string> v;
    for(int i=0;i<s.length();i++){
        v.push_back(s.substr(i,s.length()));
    }
    sort(v.begin(),v.end());
    for(auto&e:v){
        cout << e <<"\n";
    }
	return 0;
}