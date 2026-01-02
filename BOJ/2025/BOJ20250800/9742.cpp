#include <iostream>
#include <bits/stdc++.h>

using namespace std;

string s; // 순열 돌릴 문자
int res_t; // 순열 순번
int res_cnt; // input 2번째 인자
bool find_ = false;

void permutation(int c, vector<char> &p, vector<bool> &visited){
    if (c==s.length()){
        res_cnt ++;
        if(res_cnt==res_t){
            cout << s << " " << res_t << " = ";
            for(auto&e:p) cout<<e;
            cout << "\n";
            find_ = true;
        }
        return;
    }
    for(int i=0;i<s.length();i++){
        //cout<<"----1";
        if(visited[i]==false){
            visited[i]=true;
            p.push_back(s[i]);
            //cout<<"222";
            permutation(c+1,p,visited);
            if(find_) return;
            visited[i]=false;
            p.pop_back();
        }
    }
}

int main() {
	cin.tie(0); cout.tie(0);
	ios::sync_with_stdio(0);
    while(cin>>s){
        find_ = false;
        cin >> res_t;
        res_cnt = 0;
        vector<char> p;
        vector<bool> visited;
        visited.resize(s.length(),false);
        permutation(0,p,visited);
        if(!find_) cout << s << " " << res_t << " = No permutation\n";
    }

	return 0;
}