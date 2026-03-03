#include <bits/stdc++.h>
using namespace std;

int sol(string &s){
    deque<char> q;// stack
    for(int i=0;i<s.size();i++){
        q.push_back(s[i]);
        if (size(q)>1){
            if (q[size(q)-1]==q[size(q)-2]){
                q.pop_back();q.pop_back();
            }
        }
    }
    if(q.empty()) return 1;
    return 0;
}

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);

    int c=0;
    int n;cin>>n;
    for(int i=0;i<n;i++){
        string s; cin >> s;
        c += sol(s);
    }
    cout << c;

    return 0;
}