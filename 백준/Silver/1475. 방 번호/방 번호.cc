#include<bits/stdc++.h>
using namespace std;

int main(){
    ios::sync_with_stdio(0);
    cin.tie(0);
    
    // 숫자 개수를 전부 세는대신 (9+6)/2 올림한다
    int freq[9] = {}; // 0-8까지. 9는 6에 더함
    int N;
    cin >> N;
    while(N > 0){
        if (N%10 == 9){
            freq[6]++;
        } else {
            freq[N%10]++;
        }
        N /= 10;
    }
    
    freq[6] = (freq[6]/(int)2) + (freq[6]%2);
    int max = 0;
    for(int e: freq){
        if(max < e){
            max = e;
        }
    }
    cout << max;
}