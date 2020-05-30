#include<bits/stdc++.h>
#include <cstdio>
#include <iostream>
#define FAST ios_base::sync_with_stdio(0); cin.tie(0);

using namespace std;
typedef long long ll;

int n, d;
string s;
bool visited[101];
int main() {
    FAST;

    cin >> n >> d >> s;
    int cur = 0;
    int cnt = 0;
    if (n == 1) { return puts("0");}
    while(1) {
        while(cur >= 0 && s[cur] == '0') cur--;
        if (visited[cur] || cur == -1) {return puts("-1");}
        visited[cur] = true;
        cur = min(cur + d, n - 1);
        cnt++;
        if (cur == n - 1) {cout << cnt << "\n"; return 0;}
    }
}