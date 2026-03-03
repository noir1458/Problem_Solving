#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);

    int a,b;cin>>a>>b;
    if (20<=a && a<24){
        a = 24-a;
        cout << a + b;
    } else {
        cout << b-a;
    }
    return 0;
}