#include <iostream>
#include <bits/stdc++.h>

using namespace std;

char *days[] = {"SUN","MON","TUE","WED","THU","FRI","SAT"};
int dfin[] = {0,31,28,31,30,31,30,31,31,30,31,30,31};

int main() {
	cin.tie(0); cout.tie(0);
	ios::sync_with_stdio(0);
    int x,y;
    cin >> x >> y;
    int d1[13] = {-1,1};
    for(int i=2;i<13;i++){
        d1[i] = (d1[i-1] + dfin[i-1])%7;
    }
    cout << days[(d1[x] + y-1)%7];
	return 0;
}