#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);

    int a;cin>>a;
    string s = to_string(a);
    char x = s[0];
    bool res = true;
    for(int i=1;i<s.size();i++){
        if (s[i]!=x){
            res = false; break;
        }
    }
    if(res) cout << "Yes";
    else cout << "No";
    return 0;
}