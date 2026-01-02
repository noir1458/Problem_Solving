#include <iostream>
#include <bits/stdc++.h>

using namespace std;

int main() {
	cin.tie(0); cout.tie(0);
	ios::sync_with_stdio(0);

    int n,t;
    vector<int> p;
    cin>>n;
    for(int i=0;i<n;i++){
        cin>>t;
        p.push_back(t);
    }

    if(prev_permutation(p.begin(),p.end())){
        for(auto&e:p)
        cout<<e<<" ";
    }else{
        cout<<"-1";
    }

	return 0;
}