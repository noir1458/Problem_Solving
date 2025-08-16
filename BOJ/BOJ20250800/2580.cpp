#include <iostream>
#include <bits/stdc++.h>

using namespace std;

void print_m(vector<vector<int>> &m){
    for(auto &e:m){
        for(auto &e2:e){
            cout << e2 << " ";
        }
        cout << "\n";
    }
}

bool col_check(vector<vector<int>> &m, int y, int x){ // col num
    set<int> check;
    for(int i=0;i<9;i++){
        if(!check.count(m[i][x]) && m[i][x] > 0){
            check.insert(m[i][x]);
        }
    }
    return check.size()==9;
}

bool row_check(vector<vector<int>> &m, int y, int x){ // row num
    set<int> check;
    for(int i=0;i<9;i++){
        if(!check.count(m[y][i]) && m[y][i] > 0){
            check.insert(m[y][i]);
        }
    }
    return check.size()==9;
}

bool sq33_check(vector<vector<int>> &m, int y, int x){
    int row_02,col_02;
    if (0<= y && y <=2) row_02 = 0;
    else if (3<= y && y <= 5) row_02 = 1;
    else row_02 = 2;
    if (0<= x && x <=2) col_02 = 0;
    else if (3<= x && x <= 5) col_02 = 1;
    else col_02 = 2;

    set<int> check;
    for(int y2 = row_02*3 ; row_02*3+2 >= y2 ; y2++){
        for(int x2 = col_02*3 ; col_02*3+2 >= x2 ; x2++){
            if(!check.count(m[y2][x2]) && m[y2][x2] > 0){
                check.insert(m[y2][x2]);
            }
        }
    }
    return check.size()==9;
}

void solve(int c, vector<vector<int>> &m, vector<pair<int,int>> &zero_idx){
    // 가로, 세로, 33사각형에 1-9 검사되어야 한다.
    if (c==zero_idx.size()){
        print_m(m);
        exit(0);
    }
    int y = zero_idx[c].first;
    int x = zero_idx[c].second;
    for(int k=1;k<10;k++){
        m[y][x] = k;
        if(col_check(m,y,x) && row_check(m,y,x) && sq33_check(m,y,x)){
            solve(c+1,m,zero_idx);
        }
        m[y][x] = 0;
    }
}

int main() {
	cin.tie(0); cout.tie(0);
	ios::sync_with_stdio(0);
    
    vector<vector<int>> m;
    for(int i=0;i<9;i++){
        vector<int> m2;
        m2.resize(9,-1);
        m.push_back(m2);
    }

    int n;
    vector<pair<int,int>> zero_idx;

    for(int i=0;i<9;i++){
        for(int j=0;j<9;j++){
            cin >> n;
            m[i][j] = n;
            if (!n)
            zero_idx.push_back({i,j});
        }
    }

    // 0부터 zero_idx.length()-1 까지 순회하기로 하자
    solve(0,m,zero_idx);

    //print_m(m);


	return 0;
}