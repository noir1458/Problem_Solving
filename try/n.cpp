#include <iostream>
#include <bits/stdc++.h>

using namespace std;


int main() {
	cin.tie(0); cout.tie(0); // fastio
	ios::sync_with_stdio(0); // fastio
	// 풀이 작성

	long long A,B;
	
	cin >> A >> B;
	if (A>B){
		int tmp=0;
		tmp = A;
		A = B;
		B = tmp;
	}

	if (A==B){
		cout <<0;
	}
	else{
	cout << B-A-1;
	}
	cout << '\n';
	for (int i=A+1;i<B;i++){
		cout << i << ' ';
	}

	return 0;
}