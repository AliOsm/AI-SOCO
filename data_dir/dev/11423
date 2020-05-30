#include<bits/stdc++.h>

using namespace std;

typedef long long LL;
typedef unsigned long long uLL;
typedef long double ldb;
typedef pair<int,int> pii;

vector<int> G[100001];
int color[100001];

bool can = true;
void f(int v, int c=1)
{
    if(color[v])
    {
        if(color[v] != c)
            can = false;
        return;
    }
    color[v] = c;
    c = 3 - c;
    for(int i:G[v])
        f(i, c);
}

int main()
{
    ios_base::sync_with_stdio(0);cin.tie(0);
    int n, m;
    cin>>n>>m;
    int u, v;
    for(int i = 0; i < m; ++i)
    {
        cin>>u>>v;
        G[v].push_back(u);
        G[u].push_back(v);
    }
    for(int i = 1; i <= n; ++i)
        if(!color[i])
            f(i);
    if(!can)
        return cout<<"-1\n", 0;
    m = 0;
    for(int i = 1; i <= n; ++i)
        m += color[i] == 1;
    cout<<m<<endl;
    for(int i = 1; i <= n; ++i)
        if(color[i] == 1)
            cout<<i<<' ';
    cout<<endl;
    cout<<n-m<<endl;
    for(int i = 1; i <= n; ++i)
        if(color[i] == 2)
            cout<<i<<' ';
    cout<<endl;
    return 0;
}
