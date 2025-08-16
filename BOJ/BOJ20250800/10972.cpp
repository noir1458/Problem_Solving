#include <iostream>
#include <bits/stdc++.h>

using namespace std;

int n;
vector<int> p;

int main(){
	cin>>n;
	int tmp;
	for(int i=0;i<n;i++){
		cin>>tmp;
		p.push_back(tmp);
	}
	if(next_permutation(p.begin(),p.end())){
		for(auto&e:p){
			cout << e << " "; 
		}
	} else {
		cout<<"-1";
	}
	return 0;
}