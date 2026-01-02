#include <iostream>
#include <bits/stdc++.h>
using namespace std;
int main(){
    cin.tie(0);cout.tie(0);
    ios::sync_with_stdio(0);
    
    string s;
    cin >> s;
    if(s.length()%2==1){
        for(int i=0;i<s.length()/2;i++){
            cout << s[i] << s[s.length()-i-1]<<"\n";
            if(s[i]!=s[s.length()-i-1]){
                cout << "Or not.";
                return 0;
            }
        }
        cout << "Odd.";
        return 0;
    }
    cout << "Or not.";
    return 0;
}