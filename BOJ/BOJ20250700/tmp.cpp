#include <iostream>
#include <bits/stdc++.h>

using namespace std;

int main() {
	cin.tie(0); cout.tie(0);
	ios::sync_with_stdio(0);

    unsigned int a = 0xFFFFFFFF;
    unsigned int b = a * 128 / 256;
    printf("0x%08X\n", b);

	return 0;
}