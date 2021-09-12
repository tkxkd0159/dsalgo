# Compile option
```
clang++ Main.cc -std=c++17 -O2 -Wno-unused-result -o Main
g++ Main.cc -o Main -O2 -Wall -lm -static -std=gnu++17
```

# Tips
VS 사용 시 SDL 검사 해제
```c++
printf("%.6f", a)
// 아래 옵션 사용 시 endl 대신 '\n' 사용
// cin,cout 안쓰고 printf, scanf 쓸거면 아래 옵션 필요 x
cin.tie(NULL);
ios_base::sync_with_stdio(false); // C와 C++ 버퍼 분리, 따라서 C의 scanf, gets, getchar, printf, puts, putchar 등 사용 불가

// STL initialization
vector<int> v {p, q, r}
vector<int> v;
v = {p, q, r};
```
```c++
#include <iostream>
using namespace std;
int main(){
    int a,b;
    while(cin >> a >> b)
        cout << a+b << endl;

    int a,b;
    while(scanf("%d %d",&a, &b) != EOF)
        printf("%d\n",a+b);
        
    return 0;
}
```
## Essential headers
```c++
// #include <bits/stdc++.h>, 어느 헤더에 무슨 함수가 있는지 파악할 정도 되면 사용
#include <iostream>
#include <string>
#include <map>
#include <set>
#include <stack>
#include <vector>
#include <functional>
#include <algorithm>
```
## macro
```c++
#include <stdio.h>

#define ADD1(x,y) (x) + (y)
#define ADD2(x,y) #x "+" #y  //문자열로 바꿔주는 연산자 #

int main()
{
    printf("매크로 함수(ADD1) : %d\n", ADD1(10, 20));  // 30
    printf("매크로 함수(ADD2) : %s\n", ADD2(10, 20));  // 10+20

    return 0;
}
```
