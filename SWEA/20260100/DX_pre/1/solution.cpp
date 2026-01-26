#include<bits/stdc++.h>
using namespace std;
#define WIDTH (8)

int dy[4] = {0,1,0,-1};
int dx[4] = {1,0,-1,0};

vector<vector<int>> tile;
vector<vector<int>> board;
vector<int> use_tile_idx;

struct POS{
	int x,y; // x가 먼저오게
};

struct ERASE_POS{
	int score;
	vector<POS> pos_v;
	bool operator<(const ERASE_POS &other)const{ // score높은거 찾도록
		return score < other.score;
	}
};

struct SWAP_CASE{
	// 점수가 높은 경우
	// y좌표가 작은 경우
	// x좌표가 작은 경우
	// 오른쪽, 위 둘중에서 오른쪽
	int score;
	POS p1,p2; // p1 기준
	bool operator< (const SWAP_CASE &other) const{
		if (score == other.score){
			if (p1.y == other.p1.y){
				if (p1.x == other.p1.x){
					// p1 같을때 오른쪽
					return p2.x < other.p2.x;
				}
				return p1.x > other.p1.x;
			}
			return p1.y > other.p1.y;
		}
		return score<other.score;
	}
};

vector<vector<bool>> visited;
vector<ERASE_POS> erase_v;
priority_queue<SWAP_CASE> pq; // 지울거 훑고 저장해서, 점수 높은것부터 뽑아내기


// void print_board(){
// 	for(int i=0;i<8;i++){
// 		for(int j=0;j<8;j++){
// 			cout << board[i][j] << " ";
// 		}
// 		cout << "\n";
// 	}
// }

void init(int N, int mTiles[][WIDTH]){
	tile.assign(8,vector<int> (N));
	board.assign(8,vector<int> (8,-1));
	use_tile_idx.assign(8,0);
	pq = {};

	for(int y=0;y<N;y++){
		for(int x=0;x<8;x++){
			tile[x][y] = mTiles[y][x];
		}
	}
	
	// 보드에서 y=x대칭시킨다
	for(int x=0;x<8;x++){
		for(int y=0;y<8;y++){
			board[x][y] = tile[x][y];
		}
		use_tile_idx[x] = 8;
	}
	//print_board();
}

// 8*8안에 들어오는 좌표 확인
bool in_board(POS pos){
	return (0<=pos.y && pos.y<8 && 0<=pos.x && pos.x<8);
}

// 현재 좌표에서부터 지워나갈 수 있는지
// y좌표(위),x좌표(우측) 방향으로 가면서 연달아 체크
// {좌표들} 이렇게 저장해둬야 할듯
bool can_erase(POS start){
	int res = false;
	int start_num = board[start.x][start.y]; // 시작좌표 번호
	if (start_num == -1) return false;
	for(int i=0;i<2;i++){
		ERASE_POS will_erase;
		int j=1;
		will_erase.pos_v.push_back({start.x,start.y});
		if (i==0){
			if (in_board({start.x-1,start.y}) && (board[start.x-1][start.y] == start_num)) continue;
		} else if (i==1){
			if (in_board({start.x,start.y-1}) && (board[start.x][start.y-1] == start_num)) continue;
		}

		while (true){
			int nx = start.x + dx[i]*j;
			int ny = start.y + dy[i]*j;
			j++;
			if (in_board({nx,ny}) && start_num == board[nx][ny]){
				will_erase.pos_v.push_back({nx,ny});
			}
			else break;
		}
		
		int check_score = will_erase.pos_v.size();
		if(check_score==3){
			will_erase.score = 1;
			erase_v.push_back(will_erase);
			res = true;
		} else if (check_score==4){
			will_erase.score = 4;
			erase_v.push_back(will_erase);
			res = true;
		} else if (check_score >= 5){
			will_erase.score = 9;
			erase_v.push_back(will_erase);
			res = true;
		}
	}
	return res;
}

// 지울수 있는지 체크하고, 지울수 있는 좌표 기록
bool erase_check(){
	erase_v.clear();
		for(int i=0;i<8;i++){
			for(int j=0;j<8;j++){
			can_erase({i,j});
			}
	}
	if (erase_v.size()>0) return true;
	return false;
}

// 현재 보드에서 점수 획득 가능한지 체크
bool can_get_score(){
	for (int x=0;x<8;x++){
		for(int y=0;y<8;y++){
			if(x+1<8){
				swap(board[x][y], board[x+1][y]);
				if (erase_check()){
					swap(board[x][y], board[x+1][y]);
					return true;
				}
				swap(board[x][y], board[x+1][y]);
			}
			if(y+1<8){
				swap(board[x][y], board[x][y+1]);
				if (erase_check()){
					swap(board[x][y], board[x][y+1]);
					return true;
				}
				swap(board[x][y], board[x][y+1]);
			}
		}
	}
	return false;
}

int erase_all(){
	int get_score = 0;
	for(int i=0;i<erase_v.size();i++){
		get_score+=erase_v[i].score;
		for(int j=0;j<erase_v[i].pos_v.size();j++){
			board[erase_v[i].pos_v[j].x][erase_v[i].pos_v[j].y] = -1;
		}
	}
	erase_v.clear();
	return get_score;
}

// -1 부분 타일 채움
void drop_tile() {
	for(int x=0;x<8;x++){
		vector<int> tmp;
		for(int y=0;y<board[x].size();y++){
			if(board[x][y]!=-1){
				tmp.push_back(board[x][y]);
			}
		}
		while (tmp.size() < 8){
			tmp.push_back(tile[x][use_tile_idx[x]]);
			use_tile_idx[x]++;
		}
		board[x] = tmp;
	}
}


int mRet[5];
int* takeTurn(){
	int turn_score = 0;

	// 1. 격자를 준비 상태로
	// 1-1. 격자 내 빈 공간이 없게, 빈공간을 위에서부터 채운다
	// 1-2. 같은 타일이 3개 이상 연속되는 경우가 없어야 한다. 있다면 삭제
	// 1-3. 인접한 2개 타일을 교환하여, 
	// 점수를 획득할 수 있는 방법이 최소 1가지 존재
	// 하나도 없다면 전체 타일 삭제

	while (true){
		// -1 타일 채움
		drop_tile();

		// 지우기
		if (erase_check()) {
			erase_all();
			continue;
		}

		if (can_get_score()) break;
			// 점수획득 방법 없다면 전체 타일 지움
		else {
			for(int x=0;x<8;x++){
				for(int y=0;y<8;y++){
					board[x][y] = -1;
				}
			}
		}
	}
	// 2. 인접 타일 위치 교환하여 타일 삭제후 점수 얻는다. 우선순위 잇음
	// 2-1. 교환후 받는 점수가 가장 큰경우
	// 연속 3개: 1점, 4개: 4점, 5개이상: 9점, 2줄이상 동시 지워지면 점수합산
	// 2-2. Y좌표가 가장 작은 위치
	// 2-3. X좌표가 가장 작은 위치
	// 2-4. 오른쪽과 위쪽 중 오른쪽 타일과 교환

	pq = {};
	for (int x=0;x<8;x++){
		for(int y=0;y<8;y++){
			if(x+1<8){
				swap(board[x][y], board[x+1][y]);
				if(erase_check()){
					int tmp_score = 0;
					for(int i=0;i<erase_v.size();i++){
						tmp_score += erase_v[i].score;
					}
					pq.push({tmp_score,{x,y},{x+1,y}});
				}
				swap(board[x][y], board[x+1][y]);
			}
			if(y+1<8){
				swap(board[x][y], board[x][y+1]);
				if(erase_check()){
					int tmp_score = 0;
					for(int i=0;i<erase_v.size();i++){
						tmp_score += erase_v[i].score;
					}
					pq.push({tmp_score,{x,y},{x,y+1}});
				}
				swap(board[x][y], board[x][y+1]);
			}
		}
	}

	SWAP_CASE c = pq.top();pq.pop();
	turn_score += c.score;
	mRet[1] = c.p1.y;
	mRet[2] = c.p1.x;
	mRet[3] = c.p2.y;
	mRet[4] = c.p2.x;
	swap(board[c.p1.x][c.p1.y],board[c.p2.x][c.p2.y]);
	erase_check();
	erase_all();

	// 3. 삭제 후 빈공간 채우기
	// 채운 뒤 3개 이상 같은 타일 일치시 타일 삭제, 삭제한만큼 점수 추가 획득
	// 삭제될 타일이 없을 때까지 이 과정 반복
	drop_tile();
	while (true)
	{
		drop_tile();

		// 지울수 있는 타일 존재한다
		erase_v.clear();
		for(int i=0;i<8;i++){
			for(int j=0;j<8;j++){
			can_erase({i,j});
			}
		}
		// 지우기
		if (!erase_v.empty()) {
			turn_score += erase_all();
			continue;
		} else break;
	}
	
	
	mRet[0] = turn_score;
	return mRet;
}