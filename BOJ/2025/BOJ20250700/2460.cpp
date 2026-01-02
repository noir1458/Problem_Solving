#include <iostream>
#include <bits/stdc++.h>

using namespace std;

int main() {
	cin.tie(0); cout.tie(0);
	ios::sync_with_stdio(0);

    int n=0;
    int T = 10;
    int M_val = INT_MIN;
    int m_val = INT_MAX;
    while(T--){
        int in{},out{};
        cin >> out >> in;
        n -= out;
        if(n > M_val){
            M_val = n;
        }
        n += in;
        if(n > M_val){
            M_val = n;
        }
    }
    cout << M_val;
	return 0;
}