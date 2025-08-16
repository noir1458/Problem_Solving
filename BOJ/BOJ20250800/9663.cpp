#include <iostream>
#include <bits/stdc++.h>

using namespace std;

vector<bool> diag1,diag2,col;
int c = 0;

void search(int N,int y){
    if (y==N){
        c++;
        return;
    }
    for(int x=0;x<N;x++){
        if (col[x] || diag1[x+y] || diag2[x-y+N-1]) continue;
        col[x] = true;
        diag1[x+y] = true;
        diag2[x-y+N-1] = true;

        search(N,y+1);

        col[x] = false;
        diag1[x+y] = false;
        diag2[x-y+N-1] = false;
    }
}

int main() {
	cin.tie(0); cout.tie(0);
	ios::sync_with_stdio(0);

    int N; cin >> N;

    col.resize(N, false);
    diag1.resize(2*N-1, false);
    diag2.resize(2*N-1, false);

    search(N,0);

    cout << c;

	return 0;
}