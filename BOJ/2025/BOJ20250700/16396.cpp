#include <iostream>
#include <bits/stdc++.h>
using namespace std;

int main(){
    cin.tie(0); cout.tie(0);
    ios::sync_with_stdio(0);

    int arr[10002] = {};
    int n;
    cin >> n;
    for(int i=0;i<n;i++){
        int start,end;
        cin >> start >> end;
        if (start>end){
            int tmp = start;
            start = end;
            end = tmp;
        }
        for(int j=start;j<end;j++){
            arr[j] = 1;
        }
    }
    int c{0};
    int s=-1;
    for(int i=0;i<=10001;i++){
        // 시작 -1 -> 좌표
        // 끝 -> 길이합 + 좌표 -1로
        if((s==-1) && (arr[i]==1)){
            s=i;
        }
        if((s!=-1) && (arr[i]==0)){
            c += (i-s);
            //cout << s << " "<< i<<" "<< c <<"\n"; 
            s=-1;
        }
    }
    cout << c;
    return 0;
}