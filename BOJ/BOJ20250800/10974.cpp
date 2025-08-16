#include <iostream>
#include <bits/stdc++.h>

using namespace std;

int n;
vector<bool> v;
vector<int> p;

void permutation(int c){
    if (p.size()==n){
        for(const auto &e:p){
            cout << e << " ";
        }
        cout << "\n";
        return;
    }
    for(int i=0;i<n;i++){
        if(v[i+1]==false){
            v[i+1]=true;
            p.push_back(i+1);
            permutation(c+1);
            v[i+1]=false;
            p.pop_back();
        }
    }
}

int main() {
	cin.tie(0); cout.tie(0);
	ios::sync_with_stdio(0);

    cin >> n;
    v.resize(n+1,false);

    permutation(0);

	return 0;
}