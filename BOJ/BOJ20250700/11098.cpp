#include <iostream>
#include <bits/stdc++.h>

using namespace std;

int main() {
	cin.tie(0); cout.tie(0);
	ios::sync_with_stdio(0);
    int T;
    cin >> T;
    while(T--){
        int len=0;
        cin >> len;
        vector<int> price;
        vector<string> name;
        while(len--){
            int p=0;
            string n="";
            cin >> p >> n;
            price.push_back(p);
            name.push_back(n);
        }
        int find_idx=-1;
        int max_p = INT_MIN;
        for (int i=0;i<price.size();i++){
            if (max_p < price[i]){
                max_p = price[i];
                find_idx = i;
            }
        }
        cout << name[find_idx]<<"\n";
    }
	return 0;
}