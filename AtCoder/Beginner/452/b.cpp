#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);

    int h,w;cin>>h>>w;
    for(int i=0;i<w;i++){
        cout << "#";
    }
    cout << "\n";
    for(int j=0;j<h-2;j++){
        cout <<"#";
        for(int i=0;i<w-2;i++)
        cout << ".";
        cout <<"#\n";
    }
    for(int i=0;i<w;i++){
        cout << "#";
    }
    

    return 0;
}