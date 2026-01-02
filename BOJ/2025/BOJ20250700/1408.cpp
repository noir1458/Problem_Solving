#include <iostream>
#include <bits/stdc++.h>

using namespace std;
class Time{
    public:
        int h;
        int m;
        int s;
        Time(int h, int m, int s){
            self->h=h;
            self->m=m;
            self->s=s;
        }
        Time operator-(Time time){
            // 시간 뺴기
            int rs,rm,rh;
            if(self->s < time.s){
                self->s += 60;
                self->m -= 1;
            }
            if(self->m < time.m){
                self->m += 60;
                self->h -= 1;
            }
            if(self->h < time.h){
                self->h += 23;
            }
        }

};

time Parse_to_time(string s){
    int h = s.substr(0,1);
    int m = s.substr(3,4);
    int s = s.substr(6,7);
    return Time(h,m,s);
}

int main() {
	cin.tie(0); cout.tie(0);
	ios::sync_with_stdio(0);

    string s1,s2;
    cin >> s1 >> s2;
    Time t1,t2,t;
    t1 = Parse_to_time(s1);
    t2 = Parse_to_time(s2);
    cout << t.h << t.m << t.s;


	return 0;
}