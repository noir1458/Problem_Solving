#include <iostream>
#include <bits/stdc++.h>

using namespace std;

int main() {
	cin.tie(0); cout.tie(0);
	ios::sync_with_stdio(0);
    int T;
    for(cin>>T;T--;){
        int t2=5;
        vector<int> v;
        while(t2--){
            int tmp;
            cin >> tmp;
            v.push_back(tmp);
        }
        sort(v.begin(),v.end());
        if(v[3]-v[1] >= 4){
                cout << "KIN" << "\n";
        } else {
        cout << accumulate(v.begin(),v.end(),0)-v[4]-v[0] <<"\n";
        }
        }
    return 0;
    }