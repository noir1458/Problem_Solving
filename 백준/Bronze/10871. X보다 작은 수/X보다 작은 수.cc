#include <iostream>
#include <bits/stdc++.h>

using namespace std;

int main(){
    ios::sync_with_stdio(0);
    cin.tie(0);
    
    int N,X;
    cin >> N >> X;
    for(int i=0;i<N;i++){
        int A;
        cin >> A;
        if (A < X) cout << A << " ";
    }
}