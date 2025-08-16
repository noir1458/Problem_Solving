#include <iostream>
#include <bits/stdc++.h>

using namespace std;

int n;
vector<int> subset;

void search(int k){
    if(k==n+1){
        //부분집합을 처리한다
        for(int x:subset){
            cout << x << " ";
        }
        cout << "\n";
    } else {
        //k를 부분집합에 포함시킨다
        subset.push_back(k);
        search(k+1);
        subset.pop_back();
        //k를 부분집합에 포함시키지 않는다
        search(k+1);
    }
}

int main() {
	cin.tie(0); cout.tie(0);
	ios::sync_with_stdio(0);

    // 1부터 3까지 수로 부분집합
    n=3;
    search(1);


	return 0;
}