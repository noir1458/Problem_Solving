#include <iostream>
#include <bits/stdc++.h>

using namespace std;

int main() {
	cin.tie(0); cout.tie(0);
	ios::sync_with_stdio(0);
	int T;
	for(cin>>T;T--;){
		vector<int> v;
		int t1 = 10;
		while(t1--){
			int tmp;
			cin >> tmp;
			v.push_back(tmp);
		}
		sort(v.begin(),v.end());
		cout << v[7] << "\n";
	}
    
	return 0;
}