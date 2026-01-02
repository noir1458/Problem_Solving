#include <iostream>
#include <bits/stdc++.h>

using namespace std;

int main() {
	cin.tie(0); cout.tie(0);
	ios::sync_with_stdio(0);
    int M,N;
    cin >> M >> N;

    int a = 1;
    int min=-1,sum=0;
    while (a*a <= N){
        if (a*a >= M && a*a <= N){
            if (min==-1){
                min = a*a;
            }
            sum += a*a;
        }
        a++;
    }
    if (sum!=0){
    cout << sum << "\n";
    }
    cout << min;
	return 0;
}