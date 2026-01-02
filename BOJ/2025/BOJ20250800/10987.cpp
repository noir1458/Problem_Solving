#include <iostream>
#include <bits/stdc++.h>

using namespace std;

int main() {
	cin.tie(0); cout.tie(0);
	ios::sync_with_stdio(0);
    string s; cin>>s;
    unordered_set<char> l = {'a','e','i','o','u'};
    int c{};
    for (auto &e:s){
        if (l.count(e)==1){
            c ++;
        }
    }
    cout << c;
	return 0;
}