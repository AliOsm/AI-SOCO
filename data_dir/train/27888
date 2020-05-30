#include<bits/stdc++.h>

using namespace std;

typedef long long LL;
typedef unsigned long long uLL;
typedef long double ldb;
typedef pair<int,int> pii;

int M[1001];
int C[1001];

int Mc[1001][1001];
int Cc[1001][1001];

int main()
{
    ios_base::sync_with_stdio(0);cin.tie(0);
    int n, m, a, b;
    cin>>n>>m;
    for(int i = 0; i < n; ++i)
    {
        cin>>a>>b;
        ++M[b];
        ++Mc[b][a];
    }
    for(int i = 0; i < m; ++i)
    {
        cin>>a>>b;
        ++C[b];
        ++Cc[b][a];
    }
    int u = 0, v = 0;
    for(int i = 0; i < 1001; ++i)
        u += min(M[i], C[i]);
    for(int i = 0; i < 1001; ++i)
        for(int j = 0 ; j < 1001; ++j)
            v += min(Mc[i][j], Cc[i][j]);;
    cout<<u<<' '<<v<<endl;
    return 0;
}
