#include<bits/stdc++.h>

using namespace std;

typedef long long LL;
typedef unsigned long long uLL;
typedef long double ldb;
typedef pair<int,int> pii;

int main()
{
    ios_base::sync_with_stdio(0);cin.tie(0);
    int n;
    vector<int> ans;
    cin>>n;
    for(int i = max(n-100, 1); i < n; ++i)
    {
        int sum = 0, t = i;
        while(t)
        {
            sum += t%10;
            t /= 10;
        }
        if(sum + i == n)
            ans.push_back(i);
    }
    cout<<ans.size()<<'\n';
    for(int i:ans)
        cout<<i<<'\n';
    return 0;
}
