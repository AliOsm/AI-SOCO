#include<bits/stdc++.h>
using namespace std;
const int maxn = 3e5 + 5;
int visit[maxn];
int a[maxn];
vector<int>graph[maxn];
int red,blue;
int cnt[maxn][3];
void dfs(int s, int p = -1)
{
    cnt[s][a[s]]++;
    for(auto x: graph[s]){
        if(x == p)continue;
        dfs(x,s);
        for(int i = 0; i < 3; i++){
            cnt[s][i] += cnt[x][i];
        }
    }
}

int main()
{
    int n;
    cin >> n;
     red = 0, blue = 0;
    for(int i = 1; i <= n; i++){
        cin >> a[i];
        if(a[i] == 1)red++;
        else if(a[i] == 2)blue++;
    }
    for(int i = 0; i < n-1; i++){
        int u,v;
        cin >> u >> v;
        graph[u].push_back(v);
        graph[v].push_back(u);
    }
    dfs(1);
    int ans = 0;
    for(int i = 1; i <= n; i++){
        if( (cnt[i][1] == red && cnt[i][2] == 0) || (cnt[i][1] == 0 && cnt[i][2] == blue) )ans++;
    }
    cout << ans << endl;
    return 0;
}
