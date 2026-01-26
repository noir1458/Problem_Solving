#include <bits/stdc++.h>
using namespace std;

//시계방향
int dy[4] = {-1,0,1,0};
int dx[4] = {0,1,0,-1};

struct Pos{
    int y,x;
};

struct Worm {
    int to; // 방향, 0->3 시계방향 순
    int ID;
    Pos head;
    Pos next_head;
    int growth; // 성장 잠재력
    deque<Pos> body; // 머리포함 몸 전체
    bool dead;

    // 길이가 긴것, 그다음은 ID가 큰것
    bool operator<(const Worm &other) const{
        if (body.size() == other.body.size()){
            return ID > other.ID;
        }
        return body.size() > other.body.size();
    }
};

struct RESULT{
    int cnt = 0;
    int IDs[5] = {0, 0, 0, 0, 0};
};

vector<vector<int>> board;
vector<vector<int>> next_board;
int BOARD_SIZE; // 보드 크기
vector<Worm> v; // 랭킹 반환용
int NOW_TIME;
unordered_map<int, int> m_id_idx; // id:Worm

// 보드 안에 들어오는지 좌표 확인
bool in_board(Pos pos){
	return (0<=pos.y && pos.y<BOARD_SIZE && 0<=pos.x && pos.x<BOARD_SIZE);
}

// 애벌레가 일직선인지 판별
bool body_straight(Worm w){
    int sy = true;
    int sx = true;
    for(int i=0;i<w.body.size();i++){
        if (w.body[0].y != w.body[i].y) sy = false;
        if (w.body[0].x != w.body[i].x) sx = false;
    }
    return (sy||sx);
}

// 보드에 애벌레 표시
void write_board(Worm w, vector<vector<int>> &b){
    for(int i=0;i<w.body.size();i++){
        b[w.body[i].y][w.body[i].x] = w.ID;
    }
}

// 죽은거 지우기
void del_board(Worm w, vector<vector<int>> &b){
    for(int i=0;i<w.body.size();i++){
        b[w.body[i].y][w.body[i].x] = 0;
    }
}

// 전체 죽은 애벌레 지우기
void del_dead_worm(vector<vector<int>> &b){
    for(int i=0;i<v.size();i++){
        if(v[i].dead){
            del_board(v[i],b);
        }
    }
}

void game_calculate(int time){
    while (NOW_TIME < time){
        NOW_TIME ++;
        // ★ [수정 1] 시간초과의 원인이었던 next_board.assign 삭제

        // 1. 방향 전환 및 next_head 계산
        for(int i=0; i<v.size(); i++){
            if(v[i].dead) continue;
            if (body_straight(v[i])){
                v[i].to = (v[i].to + 1)%4;
            }
            v[i].next_head = {v[i].body[0].y + dy[v[i].to], v[i].body[0].x + dx[v[i].to]};
        }

        // 2. 충돌 체크 (Phase 2)
        for(int i=0; i<v.size(); i++){
            if(v[i].dead) continue;
            int ny = v[i].next_head.y;
            int nx = v[i].next_head.x;
            
            // 2-1. 벽 충돌
            if(!in_board({ny,nx})){
                v[i].dead = true; 
                continue;
            }
            
            // 2-2. 머리 vs 머리 동시 충돌
            if (next_board[ny][nx] != 0){
                v[i].dead = true;
                v[m_id_idx[next_board[ny][nx]]].dead = true;
            } else {
                next_board[ny][nx] = v[i].ID;
            }

            // 2-3. 머리 vs 몸통 충돌 (★ 자기 몸통 제외 조건 추가)
            if (board[ny][nx] != 0 && board[ny][nx] != v[i].ID) {
                Worm &check = v[m_id_idx[board[ny][nx]]];

                int tail_y = check.body.back().y;
                int tail_x = check.body.back().x;

                // 상대방이 성장 중이 아니고 살아있다면 꼬리가 비워짐 (무사 통과)
                bool tail_safe = (ny == tail_y && nx == tail_x && check.growth == 0 && !check.dead);

                if (!tail_safe){
                    v[i].dead = true;
                    // 죽은 애벌레에게 박아도 연쇄 충돌 조건에 따라 길이는 흡수함
                    check.growth += v[i].body.size(); 
                }
            } 
        }

        // 3. 죽은 애벌레 보드에서 지우기
        del_dead_worm(board);

        // ★ [수정 2] 이동 로직 분리 (꼬리 먼저 지우기 -> 머리 그리기)
        for(int i=0; i<v.size(); i++){
            if(v[i].dead) continue;
            // 성장하지 않으면 꼬리가 줄어들 예정이므로 보드에서 미리 지움
            if (v[i].growth == 0){
                board[v[i].body.back().y][v[i].body.back().x] = 0;
            }
        }

        // 머리 전진 및 데이터 갱신
        for(int i=0; i<v.size(); i++){
            if(v[i].dead) continue;
            
            board[v[i].next_head.y][v[i].next_head.x] = v[i].ID;
            v[i].body.push_front(v[i].next_head);
            
            if (v[i].growth > 0){
                v[i].growth--;
            } else {
                // 보드판은 위에서 지웠으니 deque만 빼줌
                v[i].body.pop_back();
            }
        }

        // 4. 애벌레 벡터 재구성 및 next_board 증분 초기화
        vector<Worm> tmp;
        m_id_idx.clear();
        for(int i=0; i<v.size(); i++){
            // ★ [수정 3] 사용했던 next_board 좌표만 O(1)로 초기화
            if (in_board(v[i].next_head)) {
                next_board[v[i].next_head.y][v[i].next_head.x] = 0;
            }
            if(!v[i].dead){
                m_id_idx[v[i].ID] = tmp.size();
                tmp.push_back(v[i]);
            }
        }
        v = tmp;
    }
}

void init(int N){
    BOARD_SIZE=N;
    NOW_TIME = 0;
    board.assign(N,vector<int> (N));
    next_board.assign(N,vector<int> (N));
    v.clear();
    m_id_idx.clear();
}

void join(int mTime, int mID, int mX, int mY, int mLength){
    // mTime까지 진행
    game_calculate(mTime);

    Worm new_worm;
    new_worm.to = 0;
    new_worm.ID = mID;
    new_worm.head = {mY,mX};
    new_worm.next_head = {0,0};  // game_calculate에서 계산됨
    new_worm.growth = 0;
    new_worm.dead = false;
    for(int i=0;i<mLength;i++){
        new_worm.body.push_back({mY+i,mX}); 
    }
    v.push_back(new_worm);
    m_id_idx[mID] = v.size()-1;
    write_board(new_worm,board);
}

RESULT top5(int mTime){
    game_calculate(mTime);

    RESULT ret = RESULT();
    ret.cnt = min((int)v.size(), 5);
    sort(v.begin(),v.end());

    m_id_idx.clear();
    for(int i=0;i<v.size();i++){
        m_id_idx[v[i].ID] = i;
        if(i<5) ret.IDs[i] = v[i].ID;
    }
    return ret; // dummy
}