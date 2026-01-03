#include<bits/stdc++.h>
#include<iostream>
using namespace std;

void print_v(vector<vector<int>> &v){
    for(const auto&e:v){
        for(const auto &e2:e){
            cout << e2 << " ";
        }
        cout << "\n";
    }
}

int main(){
    ios::sync_with_stdio(0);
    cin.tie(0);cout.tie(0);

    int N; cin>>N;

    vector<int> prev_max(3);
    vector<int> dp_max(3);
    vector<int> prev_min(3);
    vector<int> dp_min(3);
    vector<int> v(3);

    // 처음 부분 삽입
    int t;
    for(int j=0;j<3;j++){
        cin >> t;
        prev_min[j] = t;
        prev_max[j] = t;
    }
    N--;
    
    // N-1회 입력 받으면서 dp 계산
    while (N--)
    {
        for(int j=0;j<3;j++){
        cin >> t;
        v[j] = t;
        v[j] = t;
        }

        dp_min[0] = v[0] + min(prev_min[0],prev_min[1]);
        dp_min[1] = v[1] + min({prev_min[0],prev_min[1],prev_min[2]});
        dp_min[2] = v[2] + min(prev_min[1],prev_min[2]);

        dp_max[0] = v[0] + max(prev_max[0],prev_max[1]);
        dp_max[1] = v[1] + max({prev_max[0],prev_max[1],prev_max[2]});
        dp_max[2] = v[2] + max(prev_max[1],prev_max[2]);

        for(int j=0;j<3;j++){
            prev_min[j]=dp_min[j];
            prev_max[j]=dp_max[j];
        }
    }
    cout << max({prev_max[0],prev_max[1],prev_max[2]}) << " " << min({prev_min[0],prev_min[1],prev_min[2]});
}