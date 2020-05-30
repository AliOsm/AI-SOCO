#include<bits/stdc++.h>
using namespace std;
typedef long long LL;
const int maxn = 200009;
int a[maxn];
int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(0);
    int n;
    cin >> n;
    for(int i = 1; i <= n; i++)
    {
        cin >> a[i];
    }
    int l = 1, r = n;
    int cnt = 0;
    string ans = "";
    //vector<int> v;
    int x = 0;
    // ans += "L";
    //v.push_back(x);
    while(r > l)
    {
       // cout << x << " "<<a[l] << "----- "<<a[r]<<endl;
        if(a[r] > a[l])
        {
            if(x < a[l])
            {
                cnt++;
                ans += "L";
                //cout << a[l] << " ";
            //    v.push_back(a[l]);
                x = a[l];
                l++;
                continue;
            }
            else if (x < a[r])
            {
              //  v.push_back(a[r]);
                cnt++;
                ans += "R";
                x = a[r];
                r--;
                continue;
            }
            else break;
        }
        else if(a[r] < a[l])
        {
            //   cout << a[r] << " ";
            if(x < a[r])
            {
             //   v.push_back(a[r]);
                cnt++;
                ans += "R";
                x = a[r];
                r--;
               // continue;
            }
            else if(x < a[l])
            {
                cnt++;
                ans += "L";
                //cout << a[l] << " ";
               // v.push_back(a[l]);
                x = a[l];
                l++;
                //continue;
            }
            else break;
        }
        else break;
    }
  //  cout << l << " "<<r <<" "<< x << endl;
    if(x < a[r]){
        cnt++;
        ans += "R";
      //  v.push_back(a[r]);
    }
    cout << cnt << endl;
    cout << ans << endl;
   // for(auto x: v)cout << x << " ";
    return 0;
}


