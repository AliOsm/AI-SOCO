//.cpp
#include <bits/stdc++.h>

using namespace std;

long long i, n, m, x, ans, p, l, y, z;
string s;

int main(){
    ios::sync_with_stdio(false);
    cin>>n;
    x = n;
    while(x)
      x/=10,
      m++;
    cin>>s;
    l = s.size();
    reverse(s.begin(), s.end());
    i = 0;
    p = 1;
    while(i<l) {
      x = 0LL;
      y = 1LL;
      z = i+1;
      for(;i<l && y<n && x+y*(s[i]-'0')<n; i++)
        x += y*(s[i]-'0'),
        y *= 10,
        z = (s[i]=='0' ? z : i+1);
      ans += x*p;
      p *= n;
      i = z;
    }
    cout<<ans<<endl;
    return 0;
}
