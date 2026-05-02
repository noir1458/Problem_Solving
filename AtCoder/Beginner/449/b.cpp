#include <bits/stdc++.h>
using namespace std;

int H,W,Q;
// H*W 7 9

void func_1(int x){
    // bottom
    H -= x;
    cout << W*x<<"\n";

}

void func_2(int x){
    // rightmost
    W -= x;
    cout << H*x<<"\n";
}

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);

    cin>>H>>W>>Q;
    for(int i=0;i<Q;i++){
        int n,x;cin>>n>>x;
        if(n==1){
            func_1(x);
        } else if (n==2){
            func_2(x);
        }
    }

    return 0;
}
