#include <bits/stdc++.h>
using namespace std;
#define INF 1<<30
#define maxn 100005
#define FASTIO ios_base::sync_with_stdio(false), cin.tie(0), cout.tie(0);
typedef long long ll;


int main()
{
    FASTIO
    ///*
    //double start_time = clock();
#ifndef ONLINE_JUDGE
    freopen("in.txt", "r", stdin);
    freopen("out.txt", "w", stdout);
    freopen("error.txt", "w", stderr);
#endif    //*/
    string t;
    cin >> t;
    int n = t.size();
    int cnt = 0;
    string s_prime = "";
    map<char, int> mp;
    for(int i = 0; i <n; i++){
        if(t[i] == 'a')continue;
        else {
            mp[t[i]]++;
            //if(mp[t[i]] & 1) s_prime += t[i];
        }
    }
    for(int i = 0; i < n; i++){
        if(t[i] == 'a')continue;
        else {
            if(mp[t[i]] > 0)
             s_prime += t[i];
             mp[t[i]] -= 2;
        }
        if(mp[t[i]] % 2 != 0){
            cout << ":(\n";
            return 0;
        }
    }
    reverse(s_prime.begin(), s_prime.end());
    int sz = s_prime.size();
    int idx = n - 1;
    bool flag = false;
   // cerr << sz << endl;
    for(int i = 0; i < sz; i++){
        if(t[idx] == s_prime[i]){
            idx--;
        }
        else{
            flag = true;
            break;
        }
    }
    if(flag)cout << ":(\n";
    else{
        for(int i = 0; i <= idx; i++){
            cout << t[i];
        }
        cout << endl;
    }
    //double end_time = clock();
    //printf( "Time = %lf ms\n", ( (end_time - start_time) / CLOCKS_PER_SEC)*1000);

    return 0;
}