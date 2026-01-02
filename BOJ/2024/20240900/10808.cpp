#include <iostream>
#include <bits/stdc++.h>

using namespace std;



int main() {
	cin.tie(0); cout.tie(0); // fastio
	ios::sync_with_stdio(0); // fastio
	// 풀이 작성

	int l[26];

	for (int i=0;i<sizeof(l)/sizeof(l[0]);i++){
		l[i] = 0;
	}

	string S;
	cin >> S;


	for (char c : S){
		l[int(c)-'a'] ++;
	}

	for (int i : l){
		cout << i << ' ';
	}

	return 0;
}