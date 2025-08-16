#include <iostream>
#include <bits/stdc++.h>

using namespace std;

int main() {
	cin.tie(0); cout.tie(0);
	ios::sync_with_stdio(0);
    int c = 1;
    int t;
    cin>>t;
    cin.ignore();
    while(t--){
        cout << "Case " << c++ << ": ";
        vector<int> arr(26,0);
        string s;
        getline(cin,s);
        for(auto&e:s){
            char check = e;
            if ('A' <= check && check <= 'Z'){
                check = check + 32;
            }
            if ('a' <= check && check <= 'z'){
                arr[check - 'a'] ++;
            }
        }
        int min_v = *min_element(arr.begin(),arr.end());
        if(min_v==0) {
            cout << "Not a pangram"<<"\n";
        } else if (min_v>=3) {
            cout << "Triple pangram!!!" <<"\n";
        } else if (min_v==2) {
            cout << "Double pangram!!" << "\n";
        } else {
            cout << "Pangram!" << "\n";
        }
    }
	return 0;
}