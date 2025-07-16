#include <iostream>
#include <bits/stdc++.h>
using namespace std;
int main(){
    cin.tie(0);cout.tie(0);
    ios::sync_with_stdio(0);
    
    int n=-1000001;
    while(1){
        int tmp;
        cin >> tmp;
        if(n <= tmp){
            cout << "Good";
            return 0;
        }
    }
    cout << "Bad";
    return 0;
}