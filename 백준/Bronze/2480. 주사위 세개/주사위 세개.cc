#include <iostream>
#include <bits/stdc++.h>

using namespace std;

int main() {
	ios::sync_with_stdio(0);
	cin.tie(0);

	int A,B,C;
	cin >> A>>B>>C;
	
	if (A==B && B == C){
	    cout << 10000 + A*(1000);
	} else if (A==B || A==C){
	    cout << 1000 + A*(100);
	} else if (B==C) {
	    cout << 1000 + B*(100);
	} else {
	    int m = 0;
	    if (A > m) m = A;
	    if (B > m) m = B;
	    if (C > m) m = C;
	    cout << m*100;
	}
}