#include <iostream>
#include <bits/stdc++.h>

using namespace std;

int main() {
	cin.tie(0); cout.tie(0);
	ios::sync_with_stdio(0);
    string N,r{};int M;
    cin >> N>>M;
    while (M--)
    r += N;
    cout << r;

	return 0;
}