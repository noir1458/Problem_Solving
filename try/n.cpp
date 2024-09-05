#include <iostream>
#include <bits/stdc++.h>

using namespace std;


int main() {
	cin.tie(0); cout.tie(0); // fastio
	ios::sync_with_stdio(0); // fastio
	// 풀이 작성

	int N = 0;
	cin >> N;

	for (int i=0;i<N;i++){
		for (int a=0;a<i;a++){
			cout << ' ';
		}
		for (int a=0;a<N-i;a++){
			cout << '*';
		}
		cout << '\n';
	}

	return 0;
}