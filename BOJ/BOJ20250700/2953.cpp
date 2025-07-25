#include <iostream>
#include <bits/stdc++.h>

using namespace std;

int main() {
	cin.tie(0); cout.tie(0);
	ios::sync_with_stdio(0);
    int arr[5] = {};
    int max_v = 0;
    int max_i = -1;
    for(int i=0;i<5;i++){
        int t=4;
        while(t--){
            int add;
            cin >> add;
            arr[i] += add;
        }
        if(arr[i]>max_v){
            max_v = arr[i];
            max_i = i;
        }
    }
    cout << max_i+1 <<" "<< max_v;
	return 0;
}