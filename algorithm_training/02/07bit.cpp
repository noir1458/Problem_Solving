#include <iostream>
#include <bits/stdc++.h>

using namespace std;

void bit_mask(int x){
    for(int k=31;k>=0;k--){
        if (x&(1<<k)) cout << "1";
        else cout << "0";
    }
}

int main() {
	cin.tie(0); cout.tie(0);
	ios::sync_with_stdio(0);
    bit_mask(14);

    int x = 5328;
    cout << __builtin_clz(x) << "\n"; // 비트표현에서 왼쪽에 연속해서 있는 비트 0 개수
    cout << __builtin_ctz(x) << "\n"; // 오른쪽에 연속해서 있는 비트 0 개수
    cout << __builtin_popcount(x) << "\n"; // 비트표현에서 비트 1 개수
    cout << __builtin_parity(x) << "\n"; // ㅂ
	return 0;
}