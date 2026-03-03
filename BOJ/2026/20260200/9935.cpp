#include <bits/stdc++.h>
using namespace std;

string s,c; 
deque<char> q;

void check_func(){
    if(size(q) < size(c)) return;
    for(int i=size(c)-1;i>=0;i--){
        if (q[size(q)-1-i] != c[size(c)-1-i]){
            return;
        }
    }
    for(int i=0;i<size(c);i++){
        q.pop_back();
    }
}

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);

    cin>>s>>c;
    for(int i=0;i<size(s);i++){
        q.push_back(s[i]);
        check_func();
    }

    if (size(q)==0){
        cout << "FRULA";
        return 0;
    }
    for(auto e:q){
        cout <<e;
    }

    return 0;
}