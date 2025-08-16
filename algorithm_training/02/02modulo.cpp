#include<iostream>
#include<bits/stdc++.h>

using namespace std;

int main(){
    // 결과에 mod 한것과, 각 항에 mod후 연산한것 결과가 같다
    // (a+b)mod m = (a mod m+b mod m) mod m
    // (a-b)mod m = (a mod m-b mod m) mod m
    // (a*b)mod m = (a mod m*b mod m) mod m

    // n! mod m
    // long long x = 1;
    // long long m = 11;
    // for(int i=1;i<=n;i++){
    //     x = (x%i)%m;
    // }
    // cout << x << "\n";

    // 음수의 mod, 결과가 음수라면 +m
    // x = x%m;
    // if(x<0) x+= m;

    // 부동소수점 실수
    // 64bit-double, 80bit-long double
    double x2 = 0.3;
    printf("%.9f\n",x2);

    double x = 0.3*3 + 0.1;
    printf("%.20f\n",x); //0.99999999999999988898


    //부동소수점 실수를 == 로 비교시 위험
    double a = 0.1;
    double b = 0.1;
    if(abs(a-b)<1e-9){
        cout << "abs(a-b)<1e-9 true??";
    }

    
}