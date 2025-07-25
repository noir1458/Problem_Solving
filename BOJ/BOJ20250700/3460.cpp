#include <iostream>
#include <bits/stdc++.h>

using namespace std;

int main() {
	cin.tie(0); cout.tie(0);
	ios::sync_with_stdio(0);
    int T;
    cin>>T;
    while(T--){
        int n;
        cin >> n;
        list<int> v;
        while(n!=0){
            if (n%2==0){
                v.push_back(0);
            } else {
                v.push_back(1);
            }
            n = (int)n/2;
        }
        int i=0;
        for(auto e:v){
            if(e==1){
                cout << i << " ";
            }
            i++;
        }
    }
    
	return 0;
}