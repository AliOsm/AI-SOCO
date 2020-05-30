// Not my code
#include<bits/stdc++.h>
using namespace std;
const int N = 2e5 + 5;
long long dp[N][3];
int arr[N][5];
int nxt[N],bef[N];
vector<int>good;
int n,m,k,q;
long long solve(int r , int f);
long long calls(int r, int c, int sum)
{
    long long ret = 1e15;
    if(c > arr[r][0] && c < arr[r][1])
    {
        ret = min(ret , solve(r+1, 1) + arr[r][1] - c + arr[r][2] - 1+sum);
        ret = min(ret , solve(r+1, 0) + c - arr[r][0] + arr[r][2] - 1+sum);
    }
    else if(c <= arr[r][0])
    {
        ret = min(ret , solve(r+1, 1) + arr[r][1] - c+arr[r][2]-1+sum);
        ret = min(ret , solve(r+1, 0) + arr[r][1] - c+sum);
    }
    else {
        ret = min(ret , solve(r+1, 1) + c - arr[r][0]+sum);
        ret = min(ret , solve(r+1, 0) + c - arr[r][0]+sum+arr[r][2]-1);
    }
    return ret;
}
long long solve(int r , int f)
{
    if(r == n) return 0;
    long long & ret = dp[r][f];
    if(~ret) return ret;
    if(arr[r][2] == 0) return ret = solve(r+1 , f);
    ret = 1e15;
    if(f == 1)
    {
        int cur = arr[r-1][0];
        if(nxt[cur] != -1)
        {
            int c = nxt[cur];
            int sum = c - arr[r-1][0];
            ret = min(ret, calls( r,  c,  sum));
        }
        if(bef[cur] != -1)
        {
            int c = bef[cur];
            int sum = arr[r-1][0] - c;
            ret = min(ret, calls( r,  c,  sum));
        }
    }
    else {
        int cur = arr[r-1][1];
        if(nxt[cur] != -1)
        {
            int c = nxt[cur];
            int sum = c - arr[r-1][1];
            ret = min(ret, calls( r,  c,  sum));
        }
        if(bef[cur] != -1)
        {
            int c = bef[cur];
            int sum = arr[r-1][1] - c;
            ret = min(ret, calls( r,  c,  sum));
        }
    }
    return ret;
}
int main() {
    cin>>n>>m>>k>>q;
    for(int i = 0 ; i<n ; ++i) arr[i][0] = 1e9;
    for(int i = 0 ; i<k ; ++i)
    {
        int x,y;
        scanf("%d %d" , &x , &y);
        x--,y--;
        arr[x][0] = min(arr[x][0] , y);
        arr[x][1] = max(arr[x][1] , y);
    }
    for(int i = 0 ; i<q ; ++i)
    {
        int x;
        scanf("%d" , &x);
        x--;
        good.push_back(x);
    }
    sort(good.begin() , good.end());
    for(int i = 0 ; i<m ; ++i)
    {
        int idx = upper_bound(good.begin(), good.end(), i) - good.begin();
        if(idx == good.size()) bef[i] = good[idx - 1], nxt[i] = -1;
        else if(idx == 0) bef[i] = -1, nxt[i] = good[idx];
        else bef[i] = good[idx-1],nxt[i] = good[idx];
    }
    int xx;
    int mm = 0 , mmm = 0;
    for(int i = 0 ; i<n ; ++i) 
    {
        if(arr[i][0] != 1e9) xx = i, arr[i][2] = arr[i][1] - arr[i][0] + 1 , mm = arr[i][0] , mmm = arr[i][1];
        else arr[i][0] = mm, arr[i][1] = mmm;
    }
    n = xx+1;
    memset(dp , -1 , sizeof dp);
    if(arr[0][2] == 0) cout<<solve(1,1)+xx<<endl;
    else cout<<solve(1,0) + arr[0][1]+xx<<endl;
    return 0;
}