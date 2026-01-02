#include <iostream>
#include <bits/stdc++.h>

using namespace std;

int is_pair(char t, char inp){
    if (t=='[' && inp==']'){
        return 3;
    }
    if (t=='(' && inp==')'){
        return 2;
    }
    return 0;
}

int is_vaild(string t){
    stack<char> s;
    for(auto&e:t){
        if (!s.empty() && is_pair(s.top(),e)){
            s.pop();
        } else {
            s.push(e);
        }
    }
    if (s.empty()){
        return 1;
    }
    return 0;
}

int main() {
	cin.tie(0); cout.tie(0);
	ios::sync_with_stdio(0);
    stack<int> s;
    string t;
    cin >> t;

    // if (is_vaild(t)==0){
    //     cout << 0;
    //     return 0;
    // }

    for(auto &e:t){
        if (e=='(') s.push(-2);
        else if (e=='[') s.push(-3);

    }
    cout << res << "\n";

	return 0;
}