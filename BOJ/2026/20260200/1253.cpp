#include <bits/stdc++.h>
using namespace std;

int N;
vector<int> v;

bool func(int now){
    int i=0,j=N-1;
    int a = v[now];

    while (i<j){
        if(i==now){
            i++;
            continue;
        }
        if(j==now){
            j--;
            continue;
        }
        int res = v[i] + v[j];
        if (res < a){
            i++;
            
        } else if (res > a){
            j--;
            
        } else {
            return true;
        }
    }
    return false;
}


int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);

    cin>>N;
    v.assign(N,0);
    for(int i=0;i<N;i++){
        cin>>v[i];
    }

    int c=0;
    sort(v.begin(),v.end());
    for(int i=0;i<N;i++){
        if(func(i)){
            c++;
        }
    }
    cout << c;

    return 0;
}