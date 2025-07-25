#include<iostream>
#include<unordered_map>
#include<cstring>
#include<iterator>

using namespace std;

int main() {
	cin.tie(0); cout.tie(0);
	ios::sync_with_stdio(0);
	int n{},sum{},cnt{};
	unordered_map<int,int> m;
	while (cin >> n) {
		sum += n;
		cnt ++;
		m[n] = m[n] + 1;
	}

	int k{},v{};
	for (auto &e:m){
		if (e.second > v){
			k = e.first;
			v = e.second;
		}
	}
	cout <<  sum/cnt << "\n" << k;
	
	
	return 0;
}