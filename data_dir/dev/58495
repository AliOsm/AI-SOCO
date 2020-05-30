#include <bits/stdc++.h>
#define f(i, j, n) for(int i = j; i < n; i++)
#define all(v) v.begin(), v.end()
#define ll long long
using namespace std;

int main(){
    ios_base::sync_with_stdio(0);
    cin.tie(0);

    int n; cin >> n;
    string s; cin >> s;
    int cnt8 = 0;
    f(i, 0, n)cnt8 += s[i] == '8';
    int can = 0;
    int rem = n - cnt8;
    while(cnt8){
        if(rem >= 10)cnt8--, rem -= 10, can++;
        else break;
    }
    while(1){
        if(cnt8 && rem + cnt8 >= 11){
            cnt8 -= 11 - rem;
            rem = 0;
            can++;
        }else break;
    }
    cout << can << "\n";
}