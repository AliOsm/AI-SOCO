#include<bits/stdc++.h>

using namespace std;

typedef long long LL;
typedef unsigned long long uLL;
typedef long double ldb;
typedef pair<int,int> pii;

vector<int> chats[11];
int Y[11];
int ans[20001];

int main()
{
    ios_base::sync_with_stdio(0);cin.tie(0);
    int n, m, k;
    cin>>n>>m>>k;
    int inp;
    for(int i = 1; i <= n; ++i)
        for(int j = 1; j <= m; ++j)
        {
            cin>>inp;
            if(inp)
                chats[j].push_back(i);
        }
    while(k--)
    {
        int x, y;
        cin>>x>>y;
        Y[y] += 1;
        ans[x] -= 1;
    }
    for(int i = 1; i <= m; ++i)
        for(int j:chats[i])
            ans[j] += Y[i];
    for(int i = 1; i <= n; ++i)
        cout<<ans[i]<<' ';
    cout<<endl;
    return 0;
}
