#include <iostream>
#include <bits/stdc++.h>

using namespace std;

int main() {
	cin.tie(0); cout.tie(0);
	ios::sync_with_stdio(0);
    string s;
    cin >> s;
    int i{};
    for (auto &e:s){
        cout << e;
        if (i%10==9){
            cout <<"\n";
        }
        i++;
    }

	return 0;
}