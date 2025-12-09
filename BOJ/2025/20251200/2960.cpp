#include <bits/stdc++.h>
#include <iostream>
using namespace std;

// void print_vec(vector<int>& v){
//     for(int i=0;i<v.size();i++){
//         cout << i << " ";
//     }
//     cout << "\n";
//     for(auto e:v){
//         cout << e << " ";
//     }
//     cout << "\n\n";
// }

int main(){
    ios::sync_with_stdio(0);cin.tie(0);cout.tie(0);

    int n,k,c=0;
    cin >> n >> k;
    vector<int> v(n+1); // 지우면 1로 표시

    for(int i=2;i<n+1;i++){
        //지워지지 않은 수중 가장 작은수
        if(v[i] == 1) continue; // 지워졌다면 다음으로
        // i 가 p인 상태
        for(int j=i;j<n+1;j+=i){
            if (v[j]==1) continue; // 지워졌다면 다음 루프로
            v[j]=1;
            //cout << c << " : " << j << "\n";
            c++;
            //print_vec(v);
            if (c==k){
                cout << j;
                return 0;
            }
        }
    }
}