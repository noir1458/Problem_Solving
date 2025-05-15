#include<bits/stdc++.h>
using namespace std;

int main(){
    ios::sync_with_stdio(0);
    cin.tie(0);
    
    int A,B,C;
    cin >> A >> B >> C;
    int freq[10] = {};
    string tmp = to_string(A*B*C);
    for(auto e:tmp){
        freq[e - '0']++;
    }
    for(auto e:freq)
        cout << e << "\n";

}