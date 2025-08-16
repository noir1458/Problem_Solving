#include <iostream>
#include <bits/stdc++.h>

using namespace std;

typedef long long ll;
typedef vector<int> vi;
typedef vector<pair<int,int>> vpi;
typedef pair<int,int> pi;

#define F first
#define S second
#define PB push_back
#define MP make_pair
#define REP(i,a,b) for(int i=a;i<=b;i++)

int main() {
	cin.tie(0); cout.tie(0);
	ios::sync_with_stdio(0);

    // typedef 로 코드 짧게 만들기
    ll a = 123456789;
    ll b = 123456789;
    cout << a*b << "\n";

    // 코드 짧게 만들기
    vector<pair<int,int>> v1;
    v1.push_back(make_pair(1,2));
    v1.push_back(make_pair(3,4));
    int d = v1[0].first + v1[1].second;
    cout << d << "\n";

    vpi v2;
    v2.PB(MP(1,2));
    v2.PB(MP(3,4));
    int d2 = v2[0].F + v2[1].S;
    cout << d2 <<"\n";

    //for문 단축
    REP(i,1,5){
        cout << i;
    }

	return 0;
}