#include <iostream>
#include <bits/stdc++.h>

using namespace std;
typedef long long ll;

int main() {
	cin.tie(0); cout.tie(0);
	ios::sync_with_stdio(0);
    string s;
    cin >> s;
    ll a=0;
    ll t=1;
    if (s.substr(0,2)=="0x"){
        for (int i=s.length()-1;i>=2;i--){
            if (s[i]>='0' && s[i] <= '9'){
                a += (s[i]-'0')*t;
            } else {
                a += (s[i]-'a'+10)*t;
            }
            t *= 16;
        }
    } else if (s[0]=='0'){
        for (int i=s.length()-1;i>=1;i--){
            if (s[i]>='0' && s[i] <= '9'){
                a += (s[i]-'0')*t;
            }
            t *= 8;
        }
    } else {
        cout<<s; return 0;
    }
    cout << a;

	return 0;
}