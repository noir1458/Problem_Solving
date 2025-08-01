#include <iostream>
#include <bits/stdc++.h>

using namespace std;

char dec(char c){
    char tmp = c - 'A';
    if (tmp -3 < 0){
        tmp += 26;
    }
    return (tmp - 3) % 26 + 'A';
}

int main() {
	cin.tie(0); cout.tie(0);
	ios::sync_with_stdio(0);
    string s;
    cin >> s;
    for(auto &e:s){
        cout << dec(e);
    }
	return 0;
}