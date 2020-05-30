#include<bits/stdc++.h>
using namespace std;
int step(int a, int x)
{
    if(a - x > 0)
        return (a - x);
    else
        return (a + x);
}

int main()
{
    ios_base::sync_with_stdio(false);
    long long n,k,s;
    cin >> n >> k >> s;
    n--;
    if(n*k < s || s < k)
    {
        cout<<"NO"<<endl;
        return 0;
    }
    cout<<"YES"<<endl;
    int ans=1;
    while(k > 0)
    {
        int dist = min(n, s-k+1);
        ans = step(ans,dist);
        cout<<ans<<" ";
        s -= dist;
        k--;
    }
    return 0;
}
