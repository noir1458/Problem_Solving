#include<iostream>
#include<bits/stdc++.h>
using namespace std;
int main(){
    cin.tie(0); cout.tie(0);
    ios::sync_with_stdio(0);

    string s1,s2;
    cin >> s1 >> s2;
    sort(s1.begin(),s1.end());
    sort(s2.begin(),s2.end());
    int i{},j{},c{};
    while(i < s1.length() && j < s2.length()){
        if(s1[i]==s2[j]){
            i++;j++;c++;
        } else if (s1[i] > s2[j]){
            j++;
        } else {
            i++;
        }
    }
    cout << (s1.length()-c) + (s2.length()-c);
    return 0;
}