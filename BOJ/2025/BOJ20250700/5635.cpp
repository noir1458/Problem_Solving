#include <iostream>
#include <bits/stdc++.h>

using namespace std;

class Student {
    public:
        string name;
        int y;
        int m;
        int d;
        Student(string name, int y, int m, int d){
            this->name=name;
            this->y=y;
            this->m=m;
            this->d=d;
        }
        bool operator <(Student &student){
            if (this->y==student.y){
                if (this->m==student.m){
                    return this->d < student.d;
                }
                return this->m < student.m;
            }
            return this->y < student.y;
        }
};

int main() {
	cin.tie(0); cout.tie(0);
	ios::sync_with_stdio(0);

    int n;
    vector<Student> v;
    for(cin>>n;n--;){
        string n1;
        int y,m,d;
        cin >> n1 >> d >> m >> y;
        v.push_back(Student(n1,y,m,d));
    }
    sort(v.begin(),v.end());
    cout << v.back().name << "\n" << v.front().name ;
	return 0;
}