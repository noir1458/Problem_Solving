#include <iostream>
#include <bits/stdc++.h>

using namespace std;

int main() {
	cin.tie(0); cout.tie(0);
	ios::sync_with_stdio(0);
    int s;
    cin>>s;
    for(int i=0;i<9;i++){
        int a;
        cin>>a;
        s-=a;
    }
    cout <<s;

	return 0;
}