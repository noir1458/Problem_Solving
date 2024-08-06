#include <iostream>
#include <bits/stdc++.h>

using namespace std;

int main() {
	cin.tie(0); cout.tie(0); // fastio
	ios::sync_with_stdio(0); // fastio
	// 풀이 작성
    int n,x;
    cin >> n >> x;

    int inp;
    vector<int> v(n);
    for (int i = 0; i < n; i++){
        cin >> inp;
        v[i] = inp;
    }

    for (int i = 0; i < n; i++){
        if (v[i] < x){
            cout << v[i];
            if (i < n-1){
                cout << ' ';
            }
        }
    }
    
	return 0;
}