#include <bits/stdc++.h>
using namespace std;

const int ROOT = 1;
int unused = 2;
const int MX = 1000000 * 20 + 5; // 최대 노드 수: N * L
bool chk[MX];
int nxt[MX][10]; // 숫자 0-9

int c2i(char c){
    return c - '0';
}

// 접두어 여부를 반환하도록 수정한 insert
bool insert(string& s){
    int cur = ROOT;
    bool is_prefix = false;

    for(auto c : s){
        if(nxt[cur][c2i(c)] == -1)
            nxt[cur][c2i(c)] = unused++;
        
        cur = nxt[cur][c2i(c)]; 
        
        // 1. 나보다 짧은 단어가 이미 내 경로 상에 끝난 경우 (예: "12"가 있는데 "123" 삽입)
        if(chk[cur]) return false; 
    }

    // 2. 내 단어가 끝났는데 이미 자식이 있는 경우 (예: "123"이 있는데 "12" 삽입)
    for(int i = 0; i < 10; i++) {
        if(nxt[cur][i] != -1) return false;
    }

    chk[cur] = true;
    return true;
}

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);

    // 배열 초기화
    for(int i = 0; i < MX; i++) fill(nxt[i], nxt[i] + 10, -1);

    // 테스트 케이스 1: ["119", "97674223", "1195524421"] -> false
    vector<string> case1 = {"119", "97674223", "1195524421"};
    bool res1 = true;
    for(auto& s : case1) if(!insert(s)) res1 = false;
    cout << "Case 1 Result: " << (res1 ? "true" : "false") << "\n"; // false 출력 예상

    // 테스트 케이스 2: ["123","456","789"] -> true
    // (테스트를 위해 unused와 chk를 초기화하거나 새 로직 필요, 여기선 개념만 확인)
    for(int i = 0; i < MX; i++) fill(nxt[i], nxt[i] + 10, -1);
    vector<string> case2 = {"123","456","789"};
    bool res2 = true;
    for(auto &s : case2) if(!insert(s)) res2 = false;
    cout << "Case 2 Result: " << (res2 ? "true" : "false") << "\n";
    
    return 0;
}