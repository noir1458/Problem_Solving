#include <bits/stdc++.h>
using namespace std;

using ll = long long;


int A,B,K;

vector<int> best; // 한번 도달했던 숫자는 최소 결과를 저장한다.
vector<int> nxt; // 이전에 계산한 다음숫자
vector<int> min_n_res; // 여기에 저장했다가 합

int func_S_K(int N){
    int c=0;
    int x = N;
    while (x>0){
        int tmp = 1;
        for(int i=0;i<K;i++){
            tmp *= (x%10);
        }
        c += tmp;
        x /= 10;
    }
    return c;
}
// 99 같은 숫자여도 한번 커졌다가 무조건 작아지는듯?

void solve(int N){
    // N을 이용하여 수열 만들고 가장 작은숫자를 저장
    // 수열이 사이클이 나오게 되나..?
    set<int> s;
    s.insert(N);
    int t = N;

    while (1)
    {   
        // 이전에 best 저장했음
        if (best[t]!=0){
            s.insert(best[t]);
            break;
        }

        int nt;
        if (nxt[t]!=0){
            nt = nxt[t];
        } else {
            nt = func_S_K(t);
            nxt[t] = nt;
        }
        t = nt;
        
        // 사이클 발견
        if(s.find(t)!=s.end()){
            break;
        }
        s.insert(t);
    }

    int min_res = *s.begin();
    best[N] = min_res;

    min_n_res.push_back(min_res);
}

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);

    cin>>A>>B>>K;

    int pow9 = 1;
    for(int i=0;i<K;i++) pow9 *= 9;
    ll LIM = max(B,7*pow9);

    best.assign(LIM+1,0);
    nxt.assign(LIM+1,0);
    for(int i=A;i<B+1;i++){
        solve(i);
    }
    cout << accumulate(min_n_res.begin(),min_n_res.end(),0LL);

    return 0;
}