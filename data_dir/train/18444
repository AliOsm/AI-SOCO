#include<bits/stdc++.h>
using namespace std;

int main()
{
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    int n;
    cin >> n;
    int  L[n+2];
    for(int i = 1; i <= n; i++)cin >> L[i];
    int deth = 0;
    int j = n+2;
   for(int i = n; i >= 1; i--){
       // cout << "Enter-----\n";
        if(j <= i)deth++;
        j = min(j, i - L[i]);
   }
    cout << n - deth<<endl;
    return 0;
}

