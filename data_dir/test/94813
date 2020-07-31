#include<bits/stdc++.h>

using namespace std;

typedef long long LL;
typedef unsigned long long uLL;
typedef long double ldb;
typedef pair<int,int> pii;

char M[1002][1002];
int D[1002][1002];
bool F[1002][1002];

int main()
{
    ios_base::sync_with_stdio(0);cin.tie(0);
    int n, m, k, x, y;
    cin>>n>>m>>k;
    if(k&1)
        return cout<<"IMPOSSIBLE"<<endl, 0;
    for(int i = 1; i <= n; ++i)
        cin>>(M[i]+1);
    string ans = "";
    for(int i = 1; i <= n; ++i)
        for(int j = 1; j <= m; ++j)
            if(M[i][j] == 'X')
            {
                x = i;
                y = j;
                break;
            }
    queue<pii> Q;
    Q.emplace(x, y);
    memset(D, 127, sizeof(D));
    D[x][y] = 0;
    while(!Q.empty())
    {
        pii cur = Q.front();
        Q.pop();
        D[cur.first][cur.second] = min(D[cur.first][cur.second], min(
                min(D[cur.first+1][cur.second], D[cur.first][cur.second+1]),
                min(D[cur.first-1][cur.second], D[cur.first][cur.second-1])
                ) + 1);
        if(D[cur.first+1][cur.second]==D[0][0] && M[cur.first+1][cur.second] == '.' && !F[cur.first+1][cur.second])
        {
            Q.emplace(cur.first+1, cur.second);
            F[cur.first+1][cur.second] = true;
        }
        if(D[cur.first-1][cur.second]==D[0][0] && M[cur.first-1][cur.second] == '.' && !F[cur.first-1][cur.second])
        {
            Q.emplace(cur.first-1, cur.second);
            F[cur.first-1][cur.second] = true;
        }
        if(D[cur.first][cur.second-1]==D[0][0] && M[cur.first][cur.second-1] == '.' && !F[cur.first][cur.second-1])
        {
            Q.emplace(cur.first, cur.second-1);
            F[cur.first][cur.second-1] = true;
        }
        if(D[cur.first][cur.second+1]==D[0][0] && M[cur.first][cur.second+1] == '.' && !F[cur.first][cur.second+1])
        {
            Q.emplace(cur.first, cur.second+1);
            F[cur.first][cur.second+1] = true;
        }
    }
    M[x][y] = '.';
    while(k--)
    {
        if(M[x+1][y] == '.' && D[x+1][y] <= k)
        {
            ans.push_back('D');
            ++x;
        }
        else if(M[x][y-1] == '.' && D[x][y-1] <= k)
        {
            ans.push_back('L');
            --y;
        }
        else if(M[x][y+1] == '.' && D[x][y+1] <= k)
        {
            ans.push_back('R');
            ++y;
        }
        else if(M[x-1][y] == '.' && D[x-1][y] <= k)
        {
            ans.push_back('U');
            --x;
        }
        else
            return cout<<"IMPOSSIBLE"<<endl, 0;
    }
    cout<<ans<<endl;
    return 0;
}
