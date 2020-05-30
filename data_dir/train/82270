#include<bits/stdc++.h>

using namespace std;

typedef long long LL;
typedef unsigned long long uLL;
typedef long double ldb;
typedef pair<int,int> pii;

int main()
{
    ios_base::sync_with_stdio(0);cin.tie(0);
    int n, x;
    cin>>n>>x;
    set<int> s;
    int inp;
    for(int i = 0; i < n; ++i)
    {
        cin>>inp;
        s.insert(inp);
    }
    inp = s.find(x) != s.end();
    for(int i = 0; i < x; ++i)
        inp += s.find(i) == s.end();
    cout<<inp<<endl;
    return 0;
}
