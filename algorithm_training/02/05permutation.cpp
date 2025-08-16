#include <iostream>
#include <bits/stdc++.h>

using namespace std;

const int n = 3;
vector<int> permutation;
bool chosen [n+1];

void search(){
    if(permutation.size()==n){
        //순열을 처리한다
        for(auto &e:permutation) cout << e << " ";
        cout << "\n";
    } else {
        for(int i=1;i<=n;i++){
            if (chosen[i]) continue;
            chosen[i] = true;
            permutation.push_back(i);
            search();
            chosen[i] = false;
            permutation.pop_back();
        }
    }
}

int main() {
	cin.tie(0); cout.tie(0);
	ios::sync_with_stdio(0);

    search();

	return 0;
}