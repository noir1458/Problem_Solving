#include <bits/stdc++.h>
using namespace std;

int N;
vector<vector<int>> v;

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);

    cin>>N;

    v.assign(N+1,vector<int> (N+1));

    for(int i=1;i<N;i++){
        for(int j=i+1;j<N+1;j++){
            cin>>v[i][j];
        }
    }

    for(int a=1;a<N-1;a++){
        for(int b=a+1;b<N;b++){
            for(int c=b+1;c<N+1;c++){
                if(v[a][b] + v[b][c] < v[a][c]){
                    cout << "Yes";
                    exit(0);
                }
            }
        }
    }

    cout << "No";

    return 0;
}