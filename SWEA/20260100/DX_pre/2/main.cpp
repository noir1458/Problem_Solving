#ifndef _CRT_SECURE_NO_WARNINGS
#define _CRT_SECURE_NO_WARNINGS
#endif

#include <stdio.h>
#include <string.h>

#define CMD_INIT            (100)
#define CMD_ENTER           (200)
#define CMD_PULL_OUT        (300)
#define CMD_SEARCH          (400)


struct RESULT_E // 입차
{
    int success; // 주차 성공시 1 실패시 0
    char locname[5]; // 주차 위치
};

struct RESULT_S
{
    int cnt;
    char carlist[5][8];
};

extern void init(int N, int M, int L); // 초기화
extern RESULT_E enter(int mTime, char mCarNo[]); // 입차
// mTime에 차량번호 mCarNo인 차량이 입차. 결과를 RESULT_E 구조체에 저장후 반환
// mtime에 주차된 차량번호가 전달되는 경우는 없지만
// 출차된 차량, 또는 견인된 차량 번호가 다시 전달될수 있다.
// 견인된 차량번호 전달시 주차 성공여부 무관, 견인기록 삭제하고 견인차 아닌걸로 생각
// 문자열 끝에 \0 넣기

extern int pullout(int mTime, char mCarNo[]); // 출차
// mTime에 차량번호 mCarNo인 차량 출차
// 주차된경우 주차된 기간 반환
// 견인된 경우 (주차기간+견인기간*5)*(-1) 반환
// 주차되어있지 않고, 견인되어 있지 않은 경우는 -1 반환
// 출차 요청한 차량이 견인차량인 경우 견인되었다는 기록 삭제, 더이상 견인차 아닌걸로 생각

extern RESULT_S search(int mTime, char mStr[]); // 검색
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


static bool run()
{
    int Q, N, M, L; // q, 구역수, 각 구역당 슬롯수, 최대 주차가능 기간
    int mTime; // 이 시간에 입차

    char mCarNo[8]; // XXYZZZZ 수수영수수수수, 입차될 차량 번호
    char mStr[5];
	 
    int ret = -1, ans;

    RESULT_E res_e;
    RESULT_S res_s;

    scanf("%d", &Q);

    bool okay = false;

    for (int q = 0; q < Q; ++q)
    {
        int cmd;
        scanf("%d", &cmd);
        switch(cmd)
        {
        case CMD_INIT:
            scanf("%d %d %d", &N, &M, &L);
            init(N, M, L);
            okay = true;
            break;
        case CMD_ENTER:
            scanf("%d %s", &mTime, mCarNo);
            res_e = enter(mTime, mCarNo);
            scanf("%d", &ans);
            if (res_e.success != ans)
                okay = false;
            if (ans == 1)
            {
                scanf("%s", mStr);
                if (strcmp(res_e.locname, mStr) != 0)
                    okay = false;
            }
            break;
        case CMD_PULL_OUT:
            scanf("%d %s", &mTime, mCarNo);
            ret = pullout(mTime, mCarNo);
            scanf("%d", &ans);
            if (ret != ans)
                okay = false;
            break;
        case CMD_SEARCH:
            scanf("%d %s", &mTime, mStr);
            res_s = search(mTime, mStr);
            scanf("%d", &ans);
            if (res_s.cnt != ans)
                okay = false;
            for (int i = 0; i < ans; ++i)
            {
                scanf("%s", mCarNo);
                strcat(mCarNo, mStr);
                if (strcmp(res_s.carlist[i], mCarNo) != 0)
                    okay = false;
            }
            break;
        default:
            okay = false;
            break;
        }
    }

    return okay;
}

int main()
{
    setbuf(stdout, NULL);
    freopen("sample_input.txt", "r", stdin);

    int TC, MARK;

    scanf("%d %d", &TC, &MARK);
    for (int tc = 1; tc <= TC; ++tc)
    {
        int score = run() ? MARK : 0;
        printf("#%d %d\n", tc, score);
    }

    return 0;
}