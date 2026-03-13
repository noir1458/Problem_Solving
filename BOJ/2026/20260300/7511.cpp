#include <bits/stdc++.h>
using namespace std;

vector<int> parent;
vector<int> rnk;

int _find(int a){
    if(parent[a]==a) return a;
    return parent[a] = _find(parent[a]);
}

bool _union(int a, int b){
    a = _find(a);
    b = _find(b);
    if (a==b) return false;
    if (rnk[a] > rnk[b]){
        int tmp = a;
        a = b;
        b = tmp;
    }
    parent[a] = b;
    if(rnk[a]==rnk[b]){
        rnk[b]++;
    }
    return true;
}

void solv(){
    int user_num; cin>>user_num;
    int friend_num; cin>>friend_num;

    rnk.assign(user_num,1);
    parent.assign(user_num,0);
    for(int i=0;i<user_num;i++){
        parent[i]=i;
    }

    for(int i=0;i<friend_num;i++){
        int a,b; cin>>a>>b;
        _union(a,b);
    }

    int m;cin>>m;
    for(int i=0;i<m;i++){
        int a,b;cin>>a>>b;
        if(_find(a)==_find(b)){
            cout << 1 << "\n";
        } else {
            cout << 0 << "\n";
        }
    }
}

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);

    int n;cin>>n;
    for(int i=0;i<n;i++){
        cout << "Scenario " << i+1 << ":\n";
        solv();
        cout << "\n";
    }

    return 0;
}