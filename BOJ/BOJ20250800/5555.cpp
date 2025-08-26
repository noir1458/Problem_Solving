#include <iostream>
#include <bits/stdc++.h>

using namespace std;

int main() {
	cin.tie(0); cout.tie(0);
	ios::sync_with_stdio(0);
    string s;
    cin >> s;
    int t,c=0;
    cin >> t;
    while(t--){
        string a;
        cin >> a;
        bool f = false;
        for(int i=0;i<a.length();i++){
            string cmp;
            for(int j=0;j<s.length();j++){
                cmp += a[(i+j)%a.length()];
            }
            //cout << cmp << " " << s << "\n";
            if(cmp==s) {
                c++;
                f=true;
                break;
            }
            if(f) break;
        }
    }
    cout << c;
	return 0;
}