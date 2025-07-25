#include <iostream>
#include <bits/stdc++.h>

using namespace std;

int main() {
	cin.tie(0); cout.tie(0);
	ios::sync_with_stdio(0);
    int T;
    for(cin>>T;T--;){
        int t2=7;
        int s{},m=INT_MAX;
        while(t2--){
            int tmp;
            cin >> tmp;
            if(tmp%2==0){
                if (tmp < m){
                    m = tmp;
                }
                s += tmp;
            }
        }
        cout << s << " " << m << "\n";
    }

	return 0;
}