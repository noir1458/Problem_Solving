#include <iostream>
#include <bits/stdc++.h>

using namespace std;

long long calculate_comb(int N,int M){
    if (N > M-N){
        N = M-N; // N을 작은 값으로 대체하여 계산 최적화. 안할시 오버플로우
    }
    long long numerator = 1;
    long long denominator = 1;

    for (int i = 0; i < N ; i++){
        numerator *= (M-i);
    }
    for (int i = 1; i<N+1;i++){
        denominator *= i;
    }
    
    return numerator/denominator;
}

int main(void){
    ios::sync_with_stdio(0);
    cin.tie(0), cout.tie(0);

    int T;
    cin >> T;
    for (int i=0;i<T;i++){
        int N=0,M=0;
        cin >> N >> M;
        long long res = calculate_comb(N,M);
        cout << res << '\n';
    }


    return 0;
}