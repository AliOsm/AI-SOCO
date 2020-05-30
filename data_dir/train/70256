#include<bits/stdc++.h>
using namespace std;
typedef long long LL;
const int maxn = 100005;
int main()
{
    #ifndef ONLINE_JUDGE
    freopen("in.txt", "r", stdin);
    freopen("out.txt", "w", stdout);
    freopen("error.txt", "w", stderr);
   #endif
    ios_base::sync_with_stdio(false);
    cin.tie(0);  
    int n;
    string s;
    cin >> n >> s;
    int a[11];
    for(int i = 1; i <= 9; i++){
            cin >> a[i];
    }
    string mx = s;
int f = 0;
    for(int i = 0; i < n; i++){
        int x = s[i] - '0';
        if(x > a[x] && f){
           break;
        }
        else if(x<a[x]){
          f = 1;
            s[i]  = a[x] + '0';
            //cerr << s[i] << endl;
          mx = max(mx, s);
        }
    }
    cout << mx << endl;
    //cout << mx << " "<<s<<endl;
    return 0;
}