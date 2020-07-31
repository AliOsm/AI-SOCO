#include<bits/stdc++.h>

using namespace std;

typedef long long LL;
typedef unsigned long long uLL;
typedef long double ldb;
typedef pair<int,int> pii;

int A[101][101];

int main()
{
    ios_base::sync_with_stdio(0);cin.tie(0);
    int n, m, q;
    cin>>n>>m>>q;
    vector<vector<int>> op;
    int t, r, c, x;
    for(int i = 0; i < q; ++i)
    {
        cin>>t;
        if(t == 1)
            cin>>r;
        else if(t == 2)
            cin>>c;
        else
            cin>>r>>c>>x;
        op.push_back({t,r,c,x});
    }
    for(auto it = op.rbegin(); it != op.rend(); ++it)
    {
        t = (*it)[0];
        r = (*it)[1];
        c = (*it)[2];
        x = (*it)[3];
        if(t == 1)
        {
            A[r][0]= A[r][m];
            for(int i = m; i > 0; --i)
                A[r][i] = A[r][i-1];
        }
        else if(t == 2)
        {
            A[0][c]= A[n][c];
            for(int i = n; i > 0; --i)
                A[i][c] = A[i-1][c];
        }
        else
            A[r][c] = x;
    }
    for(int i = 1; i <= n; ++i)
    {
        for(int j = 1; j <= m; ++j)
            cout<<A[i][j]<<' ';
        cout<<'\n';
    }
    return 0;
}
