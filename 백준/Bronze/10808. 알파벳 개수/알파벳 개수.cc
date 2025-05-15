#include<bits/stdc++.h>
using namespace std;

int main(){
    ios::sync_with_stdio(0);
    cin.tie(0);
    
    int arr[26];
    fill(arr,arr+26,0);
    
    string S;
    cin >> S;
    
    for(auto e: S){
        arr[(int)e - 97] ++;
    }
    
    for(auto e: arr){
        cout << e << " ";
    }
}