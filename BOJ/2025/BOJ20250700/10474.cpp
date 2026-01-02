#include <iostream>
#include <bits/stdc++.h>

using namespace std;

int main() {
	cin.tie(0); cout.tie(0);
	ios::sync_with_stdio(0);
    long long u,d;
    while(1){
    cin>>u>>d;
    if(u==0&&d==0)break;
    cout << (long long)u/d << " " <<u%d <<" / " << d << "\n";
    }
	return 0;
}