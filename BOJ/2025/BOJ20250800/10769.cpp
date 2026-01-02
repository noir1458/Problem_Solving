#include <iostream>
#include <bits/stdc++.h>

using namespace std;

int main() {
	cin.tie(0); cout.tie(0);
	ios::sync_with_stdio(0);
    string st;
    int h=0,s=0;
    getline(cin,st);
    for(int i=3;i<st.length()+1;i++){
        //cout << st.substr(i-3,3) << "\n";
        if(st.substr(i-3,3)==":-)") h++;
        else if(st.substr(i-3,3)==":-(") s++;
    }
    if (h==0&&s==0) cout << "none";
    else if (h==s) cout << "unsure";
    else if (h>s) cout << "happy";
    else cout << "sad";
	return 0;
}