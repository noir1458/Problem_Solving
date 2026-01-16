#include<bits/stdc++.h>
#include<iostream>
using namespace std;

int add_num(int n){
    int res = 0;
    while (n > 0){
        res += (n%10)*(n%10);
        n /= 10;
    }
    return res;
}

int main(){
    ios::sync_with_stdio(0);
    cin.tie(0);cout.tie(0);

    int n; cin>>n;
    bool visited[2027] = {0,};
    visited[n] = true;

    while (true)
    {
        if (n==1) break;
        n = add_num(n);
        if(visited[n]) {
            cout << "No";
            return 0;
        }
        visited[n] = true;
    }
    cout << "Yes";

    return 0;
}