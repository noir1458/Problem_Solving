#include <iostream>
#include <bits/stdc++.h>

using namespace std;

int main() {
	cin.tie(0); cout.tie(0);
	ios::sync_with_stdio(0);
    int t;
    int c = 1;
    for(cin>>t;t--;){
        int n; cin>>n;
        vector<int> v;
        while (n--){
           int tmp;cin>>tmp;
           v.push_back(tmp);
        }
        sort(v.begin(),v.end());
        int m_gap = 0;
        for(int i=1;i<v.size();i++){
            if (v[i-1] - v[i] > 0) {
                if (v[i-1] - v[i] > m_gap)
                m_gap = v[i-1] - v[i];
            } else {
                if (v[i] - v[i-1] > m_gap)
                m_gap = v[i] - v[i-1];
            }
        }
        cout << "Class " << c++ <<"\n";
        cout << "Max " << v.back() << ", Min " << v.front() <<", Largest gap " << m_gap <<"\n";
    }
	return 0;
}