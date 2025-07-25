#include <iostream>
#include <bits/stdc++.h>

using namespace std;
char ENC(char c){
    char c2;
    if ('A' <= c && c <= 'Z'){
        c2 = ((c - 'A') + 13) % 26 + 'A';
    } else if ('a' <= c && c <= 'z'){
        c2 = ((c - 'a') + 13) % 26 + 'a';
    } else {
        c2 = c;
    }
    return c2;
}

int main() {
	cin.tie(0); cout.tie(0);
	ios::sync_with_stdio(0);
    string s,r;
    getline(cin,s);
    for(auto &e:s){
        r += ENC(e);
    }
    cout << r;
	return 0;
}