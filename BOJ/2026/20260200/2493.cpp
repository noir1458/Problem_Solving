#include<bits/stdc++.h>
using namespace std;

struct p
{
    int value,idx;
};


int main(){
    ios::sync_with_stdio(0);cin.tie(0);

    deque<p> q;
    int n;cin>>n;
    for(int i=1;i<n+1;i++){
        int x;cin>>x;

        while (!q.empty())
        {
            // 들어온것보다 작은거 치움
            if(q.back().value < x) q.pop_back();
            else break;
        }

        if (q.empty()) cout << "0 ";
        else cout << q.back().idx << " ";

        q.push_back({x,i});
    }
    
}