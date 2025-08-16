#include <iostream>
#include <bits/stdc++.h>

using namespace std;

int main() {
	cin.tie(0); cout.tie(0);
	ios::sync_with_stdio(0);
    int t;
    cin >> t;
    while(t--){
        int Ys{},Ks{};
        for (int i=0;i<9;i++){
            int Y,K;
            cin >> Y >> K;
            Ys += Y; Ks += K;
        }
        if(Ys==Ks)
        cout << "Draw"<<"\n";
        else if (Ys>Ks)
        cout << "Yonsei"<<"\n";
        else
        cout << "Korea"<<"\n";
    }

	return 0;
}