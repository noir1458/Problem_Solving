#include <bits/stdc++.h>
using namespace std;

int N,K;
deque<int> q; // 위치
vector<int> visited; // 여기에 시간

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);

    visited.assign(100001,-1);
    cin>>N>>K;

    // 1초후 x-1 x+1
    // 0초후 2*x

    q.push_back(N);
    visited[N] = 0;

    while (true){
        auto n = q.front(); q.pop_front();
        if (n==K){
            cout << visited[n];
            break;
        }
        // 0초 걸리는건 앞으로, 그리고 0인건 곱해도 계속 0이다.
        if (n!=0 && n*2 <= 100000 && visited[n*2] == -1){
            q.push_front(n*2);
            visited[n*2] = visited[n];
        }
        // t+1 하는건 뒤로 넣기
        if (n-1 >= 0 && visited[n-1] == -1){
            q.push_back(n-1);
            visited[n-1] = visited[n]+1;
        }
        if (n+1 <= 100001 && visited[n+1] == -1){
            q.push_back(n+1);
            visited[n+1] = visited[n]+1;
        }  
    }
    return 0;
}