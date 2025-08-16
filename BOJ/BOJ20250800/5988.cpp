#include <iostream>
#include <bits/stdc++.h>

using namespace std;

int main(){
    cin.tie(0); cout.tie(0);
    ios::sync_with_stdio(0);
    int t;
    for(cin>>t;t--;){
        string s; cin>>s;
        int a = s.back() - '0';
        if(a%2==0)cout<<"even"<<"\n";
        else cout<<"odd"<<"\n";
    }
    return 0;
}