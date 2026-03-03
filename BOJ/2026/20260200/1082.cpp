#include <bits/stdc++.h>
using namespace std;

int N,M;
vector<int> v;
struct num_cost
{
    int num,cost;
};


int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);

    cin>>N;
    v.assign(N,0);
    for(int i=0;i<N;i++){
        cin>>v[i];
    }
    cin>>M;

    vector<int> room_num;

    // 0말고 다른 제일싼걸로 앞에 넣고
    // 0포함 제일 싼걸로 나머지 금액 채워서 최대 자리수 계산
    int low_cost_not0 = *min_element(v.begin()+1,v.end());
    int low_cost = *min_element(v.begin(),v.end());

    int low_idx_not0 = 1;
    for(int i=1;i<N;i++){
        if (v[i] <= v[low_idx_not0]) low_idx_not0 = i;
    }

    int low_idx = 0;
    for(int i=0;i<N;i++){
        if (v[i] <= v[low_idx]) low_idx = i;
    }

    int num_length;
    if(M < low_cost_not0){
        num_length = 1;
        room_num.push_back(0);
        cout << 0;
        return 0;
    }

    if(N==1){
        cout << 0;
        return 0;
    }

    num_length = (M - low_cost_not0)/low_cost +1;
    room_num.push_back(low_idx_not0);
    for(int i=0;i<num_length-1;i++){
        room_num.push_back(low_idx);
    }
    int remain = M - (low_cost_not0 + low_cost*(num_length-1));

    // 가장 높은 자리수부터 
    for(int i=0;i<size(room_num);i++){
        for(int j=N-1;j>=0;j--){
            if((room_num[i] < j) && (0 <= remain - v[j] + v[room_num[i]])){
                remain -= (v[j] - v[room_num[i]]);
                room_num[i] = j;
                break;
            }
        }
    }
    for(const auto&e:room_num){
        cout << e;
    }

    return 0;
}