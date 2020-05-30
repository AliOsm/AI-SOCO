#include<bits/stdc++.h>
using namespace std;

int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(0);
    int n,w;
    cin >> n >> w;
    long long mn = INT_MAX, mx = INT_MIN;
    long long b = 0;
    for(int i = 0; i < n; i++)
    {
        int x;
        cin >> x;
         b += x;
        mx = max(b, mx);
        mn = min(b, mn);
    }
    if(mx > w)
    {
        cout << 0 << endl;
        return 0;
    }
     //cout << mn << " ** "<<mx << endl;
    //cout << lf << " **  "<<rg << endl;
    long long lf,rg;
    if(mn < 0) lf = -mn;
    else lf = 0;
    if(mx <= 0) rg = w;
    else rg = w - mx;
   // cout << mn << " "<<mx << endl;
   // cout << lf << " "<<rg << endl;
    if(lf > rg) cout << 0 << endl;
    else cout << (rg - lf + 1)<<endl;
    return 0;
}
