#include<bits/stdc++.h>
using namespace std;

int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(NULL),cout.tie(NULL);
    long long n,m;
    cin >> n >> m;
    long long ex=0;
    for(int i = 0; i < n; i++){
        int x;
        cin >> x;
        x += ex;
        long long ans = x/m;
        ex = x - (m*ans);
        cout<<ans<<" ";
    }
    return 0;
}
