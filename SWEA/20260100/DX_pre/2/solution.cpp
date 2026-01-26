#include<bits/stdc++.h>
using namespace std;

struct CAR {
    int mTime;
    //char locname[5];
};

struct CAR_TIME{
    int mTime;
    int xTime; // 견인시간
    //char locname[5];
    int loc_idx;
    int slot_idx;
    string XX; //char mCarNo[8];
    string Y;
    string ZZZZ;
    bool operator<(const CAR_TIME &other) const{
        if (XX==other.XX) {
            return Y<other.Y;
        }
        return XX<other.XX;
    }
};

vector<vector<int>> p; // 주차 공간
vector<int> loc_pointer; // 구역에서 미사용중인 가장 앞자리 가리키도록
vector<int> loc_using_slot; // 구역에서 현재 사용중인

deque<CAR_TIME> p_dq; // 주차된 차량 시간 기록
unordered_multimap<string,CAR_TIME> p_map; // 주차차량 검색, ZZZZ로
unordered_multimap<string,CAR_TIME> x_map; // 견인차 기록, ZZZZ차량 뒷번호로
int MAX_TIME;

struct RESULT_E
{
    int success;
    char locname[5];
};

struct RESULT_S
{
    int cnt;
    char carlist[5][8];
};


void init(int N, int M, int L)
{
    p.assign(N,vector<int>(M,0));
    MAX_TIME = L;
    loc_pointer.assign(N,0);
    loc_using_slot.assign(N,0);
    p_dq.clear();
    p_map.clear();
    x_map.clear();
    return;
}

// 이 시간대 견인처리
void check_time_x (int mTime){
    while (!p_dq.empty()){ // 주차된 차량 있는 경우만 견인체크
        CAR_TIME check = p_dq.front();
        if(check.mTime+MAX_TIME <= mTime){// 견인
            p_dq.pop_front();

            // 이미 출차된 차량인지 확인
            bool found = false;
            auto range = p_map.equal_range(check.ZZZZ);
            for(auto it=range.first;it!=range.second;it++){
                if (check.Y == it->second.Y && check.XX == it->second.XX && check.mTime == it->second.mTime){
                    p_map.erase(it);
                    found = true;
                    break;
                }
            }
            if (!found) continue; 

            // 먼저 주차공간 p에서 지우고
            p[check.loc_idx][check.slot_idx] = 0;
            loc_using_slot[check.loc_idx] --;
            for(int i=0;i<p[check.loc_idx].size();i++){ // 앞에서부터 0인거 찾아서 포인터 당겨놓는다.
                if (p[check.loc_idx][i]==0){
                    loc_pointer[check.loc_idx] = i;
                    break;
                }
            }
            check.xTime = check.mTime + MAX_TIME; 
            x_map.insert({check.ZZZZ,check});
        }
        else break;
    }
}

// mTime에 차량번호 mCarNo인 차량이 입차. 결과를 RESULT_E 구조체에 저장후 반환
// mtime에 주차된 차량번호가 전달되는 경우는 없지만
// 출차된 차량, 또는 견인된 차량 번호가 다시 전달될수 있다.
// 견인된 차량번호 전달시 주차 성공여부 무관, 견인기록 삭제하고 견인차 아닌걸로 생각
// 문자열 끝에 \0 넣기
RESULT_E enter(int mTime, char mCarNo[])
{
    string XX(mCarNo, 2);
    string Y(mCarNo + 2, 1);
    string ZZZZ(mCarNo + 3, 4);

    // 앞에 견인할 차량 있나 체크해야함
    check_time_x(mTime);
   
    // 재입차 요청시
    auto range = x_map.equal_range(ZZZZ);
    for(auto it=range.first;it!=range.second;it++){
        if (Y == it->second.Y && XX == it->second.XX){
            x_map.erase(it);
            break;
        }
    }

    RESULT_E res_e;
    res_e.success = 0; // 실패
    // 빈 슬롯이 가장 많은 구역 중 영역의 대문자 순서가 가장 앞선 구역이 선택된다.
    // 선택된 구역에서 숫자 번호가 가장 앞선 빈 슬롯에 차량이 보관이 된다.
    // 만약 어느 구역에도 빈 슬롯이 없는 경우 주차는 실패한다
    int min_using_slot = 1e9;
    int park_loc = -1;
    for(int i=0;i<p.size();i++){
        if (min_using_slot > loc_using_slot[i]){
            min_using_slot = loc_using_slot[i];
            park_loc = i;
        }
    }
    // 근데 슬롯없는경우 -1, N개 슬롯 다 채운경우, 처리하고 주차 실패해야함
    if (min_using_slot >= p[0].size()) {
        return res_e;
    }
    if(loc_pointer[park_loc] >= p[park_loc].size()){
        return res_e;
    }
    if(p[park_loc][loc_pointer[park_loc]] != 0){
        while (loc_pointer[park_loc] < p[park_loc].size() && p[park_loc][loc_pointer[park_loc]]!=0){ // 미주차(0) 슬롯까지 포인터 ++;
            loc_pointer[park_loc]++;
        }
        if(loc_pointer[park_loc] >= p[park_loc].size()){
            return res_e;
        }
    }

    // 주차 구역이 i로 정해짐(영어 대문자), 여기의 p_pointer에 주차, 하고 포인터와 주차수+1
    p[park_loc][loc_pointer[park_loc]] = mTime;
    p_map.insert({ZZZZ,{mTime,0,park_loc,loc_pointer[park_loc],XX,Y,ZZZZ}});
    p_dq.push_back({mTime,0,park_loc,loc_pointer[park_loc],XX,Y,ZZZZ});
    // 주차 성공


    res_e.success = 1; // 성공
    int tmp = loc_pointer[park_loc];
    res_e.locname[3] = '0' + tmp % 10;
    tmp /= 10;
    res_e.locname[2] = '0' + tmp % 10;
    tmp /= 10;
    res_e.locname[1] = '0' + tmp % 10;
    res_e.locname[0] = 'A' + park_loc;
    res_e.locname[4] = '\0';

    loc_using_slot[park_loc]++;
    while (loc_pointer[park_loc] < p[park_loc].size() && p[park_loc][loc_pointer[park_loc]]!=0){ // 미주차(0) 슬롯까지 포인터 ++;
       loc_pointer[park_loc]++;
    }
    return res_e;
}

// mTime에 차량번호 mCarNo인 차량 출차
// 주차된경우 주차된 기간 반환
// 견인된 경우 (주차기간+견인기간*5)*(-1) 반환
// 주차되어있지 않고, 견인되어 있지 않은 경우는 -1 반환
// 출차 요청한 차량이 견인차량인 경우 견인되었다는 기록 삭제, 더이상 견인차 아닌걸로 생각
int pullout(int mTime, char mCarNo[])
{
    string XX(mCarNo, 2);
    string Y(mCarNo + 2, 1);
    string ZZZZ(mCarNo + 3, 4);
    // 앞에 견인할 차량 있나 체크해야함
    check_time_x(mTime);

    CAR_TIME check;

    // 주차 경우
    auto range = p_map.equal_range(ZZZZ);
    for(auto it=range.first;it!=range.second;it++){
        check = it->second;
        if (Y == check.Y && XX == check.XX){
            int res = mTime - check.mTime;

            p[check.loc_idx][check.slot_idx] = 0;
            loc_using_slot[check.loc_idx]--;
            for(int i=0;i<p[check.loc_idx].size();i++){
                if (p[check.loc_idx][i]==0){
                    loc_pointer[check.loc_idx] = i;
                    break;
                }
            }


            p_map.erase(it);
            
            return res;
        }
    }

    // 견인경우
    auto range2 = x_map.equal_range(ZZZZ);
    for(auto it=range2.first;it!=range2.second;it++){
        if (Y == it->second.Y && XX == it->second.XX){
            int res = (it->second.xTime - it->second.mTime) + (mTime - it->second.xTime)*5;
            x_map.erase(it);
            return res*(-1);
        }
    }
    return -1;
}

// 검색시각, 차량 뒷4자리 번호
// mTime에 주차된차량, 견인된 차량 중 차량번호 뒷 4자리가 mStr과 일치하는 차량 우선순위순 5대 검색
// mStr=5870 이고 24Z5870 이면 일치한 경우
// 우선순위는
// 주차된 차량이 견인된 차량보다 우선순위 높다
// 위조건에서 우선순위 같은경우, XX(앞의 수) 낮은게 우선순위 높다
// 위조건에서 우선순위 같은경우, Y(알파벳) 빠른게 우선순위 높다.
//검색된 차량의 개수를 RESULT_S.cnt에 저장하고 우선 순위 순으로 찾은 i번째 차량 번호는 RESULT_S.carlist[i – 1]에 저장한다. 
//(0 ≤ RESULT_S.cnt ≤ 5, 1 ≤ i ≤ RESULT_S.cnt)
// 찾은 차량의 개수를 RESULT_S.cnt에 저장, 찾은 차량 번호를 RESULT_S.carlist에 저장. 찾은 개수는 5를 초과할 수 없다.
RESULT_S search(int mTime, char mStr[]) // ZZZZ를 받은것
{
    string ZZZZ = mStr;
    // 앞에 견인할 차량 있나 체크해야함
    check_time_x(mTime);
    RESULT_S res_s;
    res_s.cnt = 0;

    int tmp_cnt = 0;

    vector<CAR_TIME> search_tmp;
    auto range = p_map.equal_range(ZZZZ);
    for(auto it=range.first;it!=range.second;it++){
        search_tmp.push_back(it->second);
        tmp_cnt++;
    }
    sort(search_tmp.begin(),search_tmp.end());
    for(const auto &e:search_tmp){
        if(res_s.cnt >= 5) break;
        string t1 = e.XX;
        string t2 = e.Y;
        string t3 = e.ZZZZ;
        res_s.carlist[res_s.cnt][0] = t1[0];
        res_s.carlist[res_s.cnt][1] = t1[1];
        res_s.carlist[res_s.cnt][2] = t2[0];
        res_s.carlist[res_s.cnt][3] = t3[0];
        res_s.carlist[res_s.cnt][4] = t3[1];
        res_s.carlist[res_s.cnt][5] = t3[2];
        res_s.carlist[res_s.cnt][6] = t3[3];
        res_s.carlist[res_s.cnt][7] = '\0';
        res_s.cnt++;
    }

    // 견인 차량
    search_tmp.clear();
    auto range2 = x_map.equal_range(ZZZZ);
    for(auto it=range2.first;it!=range2.second;it++){
        search_tmp.push_back(it->second);
        tmp_cnt++;
    }
    sort(search_tmp.begin(),search_tmp.end());
    for(const auto &e:search_tmp){
        if(res_s.cnt >= 5) break;
        string t1 = e.XX;
        string t2 = e.Y;
        string t3 = e.ZZZZ;
        res_s.carlist[res_s.cnt][0] = t1[0];
        res_s.carlist[res_s.cnt][1] = t1[1];
        res_s.carlist[res_s.cnt][2] = t2[0];
        res_s.carlist[res_s.cnt][3] = t3[0];
        res_s.carlist[res_s.cnt][4] = t3[1];
        res_s.carlist[res_s.cnt][5] = t3[2];
        res_s.carlist[res_s.cnt][6] = t3[3];
        res_s.carlist[res_s.cnt][7] = '\0';
        res_s.cnt++;
    }

    return res_s;
}