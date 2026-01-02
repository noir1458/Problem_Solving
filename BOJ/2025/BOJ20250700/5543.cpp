#include <iostream>
#include <bits/stdc++.h>

using namespace std;

int main() {
	cin.tie(0); cout.tie(0);
	ios::sync_with_stdio(0);
    int t1=3,t2=2;
    int m1=INT_MAX,m2=INT_MAX;
    while(t1--){
        int tmp{};
        cin >> tmp;
        if (tmp < m1){
            m1 = tmp;
        }
    }
    while(t2--){
        int tmp{};
        cin >> tmp;
        if (tmp < m2){
            m2 = tmp;
        }
    }
    cout << m1+m2-50;
	return 0;
}