#include <bits/stdc++.h>
using namespace std;

long double PI = acosl(-1.0L);


int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);

    long double x;cin>>x;
    long double r = x/2.0L;
    cout << fixed << setprecision(15) << r * r * PI << '\n';


    return 0;
}
