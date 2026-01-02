#include <iostream>
#include <bits/stdc++.h>

using namespace std;

int main() {
	cin.tie(0); cout.tie(0);
	ios::sync_with_stdio(0);
    
    int T;
    cin >> T;
    while(T--){
        string q;
        cin >> q;
        list<char> F{};
        list<char> B{};
        
        for(auto e:q){
            // for(auto e:F){
            // cout << e;
            // }
            // for(auto e:B){
            //     cout << e;
            // }
            // cout << "\n";
            if (e=='<'){
                if(F.empty()==0){
                char tmp = F.back();
                F.pop_back();
                B.push_front(tmp);
                }
            } else if (e=='>'){
                if(B.empty()==0){
                    char tmp = B.front();
                    F.push_back(tmp);
                    B.pop_front();
                }
            } else if (e=='-'){
                if(F.empty()==0){
                    F.pop_back();
                }
            } else {
                F.push_back(e);
            }
        }
        for(auto e1:F){
            cout << e1;
        }
        for(auto e1:B){
            cout << e1;
        }
        cout <<"\n";
    }
	return 0;
}