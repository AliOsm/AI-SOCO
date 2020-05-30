#include<bits/stdc++.h>

using namespace std;

typedef long long LL;
typedef unsigned long long uLL;
typedef long double ldb;
typedef pair<int,int> pii;

int main()
{
    ios_base::sync_with_stdio(0);cin.tie(0);
    int n, p;
    cin>>n>>p;
    p/=2;
    stack<int> v;
    for(int i = 0; i < n; ++i)
    {
        string s;
        cin>>s;
        v.push(s.size() > 4);
    }
    LL sum = 0, cur = 0;
    while(!v.empty())
    {
        cur += v.top();
        v.pop();
        sum += cur;
        cur *= 2;
    }
    cout<<sum*p<<endl;
    return 0;
}
