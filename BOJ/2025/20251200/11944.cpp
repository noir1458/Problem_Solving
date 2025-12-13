#include<bits/stdc++.h>
#include<iostream>
using namespace std;

int main(){
    ios::sync_with_stdio(0);
    cin.tie(0);cout.tie(0);

    int N,M;
    cin>>N>>M;
    string s = to_string(N);
    if (s.length()*N > M){
        for(int i=0;i<M/s.length();i++){
        cout << s;
        }
        for(int i=0;i<M%s.length();i++){
            cout << s[i];
        }
    } else {
        for (int i=0;i<N;i++){
            cout << s;
        }
    }
}