#include <iostream>
#include <bits/stdc++.h>

using namespace std;
typedef long long ll;

int main() {
	cin.tie(0); cout.tie(0);
	ios::sync_with_stdio(0);

    ll a;
    cin >> a;
    while(a--){
        ll b;
        cin >> b;
        vector<int> v;
        while(b--){
            ll c;
            cin>>c;
            v.push_back(c);
        }
        ll s=0;
        ll m_idx=-1;
        ll m_val = 0;
        bool d = false;
        for(int i=0;i<v.size();i++){
            s += v[i];
            if(m_val==v[i]) d = true;
            if (m_val < v[i]){
                m_idx = i;
                m_val = v[i];
                d = false;
            }
        }
        if(d){
            cout << "no winner\n";
        } else if(s/2 < m_val){
            cout << "majority winner "<<m_idx+1<<"\n";
        } else {
            cout << "minority winner "<<m_idx+1<<"\n";
        }
    }

	return 0;
}