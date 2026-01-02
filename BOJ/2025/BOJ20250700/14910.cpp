#include <iostream>
#include <bits/stdc++.h>
using namespace std;
int main(){
    cin.tie(0);cout.tie(0);
    ios::sync_with_stdio(0);
    
    int res = 1;
    int n=INT_MIN;
    int tmp;
    while(cin >> tmp){
        if(n > tmp){
            res = 0;
            break;
        }
        n = tmp;
    }
    if (res){
    cout << "Good";
    } else {
    cout << "Bad";
    }
    return 0;
}