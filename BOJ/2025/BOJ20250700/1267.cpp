#include<iostream>
#include<bits/stdc++.h>
using namespace std;
int main(){
    cin.tie(0); cout.tie(0);
    ios::sync_with_stdio(0);

    int N{};
    vector<int> v;
    cin >> N;
    for(int i=0;i<N;i++){
        int tmp;
        cin >> tmp;
        v.push_back(tmp);
    }
    int c1{};
    int c2{};
    for(auto e:v){
        c1 += (int)(e/30+1)*10;
        c2 += (int)(e/60+1)*15;
    }
    if (c1 > c2){
        cout << "M " << c2;
    } else if (c1 < c2){
        cout << "Y " << c1;
    } else {
        cout << "Y " << "M " << c1;
    }
    return 0;
}