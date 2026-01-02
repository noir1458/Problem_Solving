#include<bits/stdc++.h>
#include<iostream>
using namespace std;

int main(){
    ios::sync_with_stdio(0);
    cin.tie(0);cout.tie(0);

    int T; cin>>T;
    vector<int> v; // input 저장
    while (T--){
        int a; cin>>a;
        v.push_back(a);
    }

    // 최대값까지 인덱스 필요
    auto max_it = max_element(v.begin(), v.end());
    vector<int> s(*max_it + 1);

    // s 벡터에 약수합 구하기
    for(int i=1;i<s.size();i++){
        for(int j=i;j<s.size();j+=i){
            s[j] += i;
        }
    }

    // 누적합으로 벡터에 약수 합 구하기
    vector<long long> prefix_s(s.size());
    for(int i=1;i<s.size();i++){
        prefix_s[i] =  s[i] + prefix_s[i-1];
    }

    for(const auto &e:v){
        cout << prefix_s[e] << "\n"; 
    }
}