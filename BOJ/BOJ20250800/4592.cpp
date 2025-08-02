#include <iostream>
#include <bits/stdc++.h>

using namespace std;

int main() {
	cin.tie(0); cout.tie(0);
	ios::sync_with_stdio(0);
    while(1){
        int t{};
        cin >> t;
        if(t==0) return 0;
        vector<int> v{};
        while(t--){
            int tmp;
            cin >> tmp;
            if (v.size()!=0 && v.back()==tmp) continue;
            v.push_back(tmp);
        }
        for(auto&e:v){
            cout << e << " ";
        }
        cout << "$\n";
    }
	return 0;
}