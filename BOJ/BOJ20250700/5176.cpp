#include <iostream>
#include <bits/stdc++.h>

using namespace std;

int main() {
	cin.tie(0); cout.tie(0);
	ios::sync_with_stdio(0);
    int T{};
    for(cin>>T;T--;){
        int P{},M{},tmp{},c{};
        cin >> P >> M;
        vector<int> v;
        v.resize(M,0);
        while(P--){
            cin >> tmp;
            if (v[tmp-1]==0){
                v[tmp-1]=1;
            } else {
                c += 1;
            }
        }
        cout << c << "\n";
    }
	return 0;
}