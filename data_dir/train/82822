#include<bits/stdc++.h>
using namespace std;
const int maxn = 200005;
int a[maxn];
int ans[maxn];
vector<int>v1;
vector< pair<int,int> > v2;

int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(0);
    int n,k;
    cin >> n >> k;
    for(int i = 0; i < n; i++)
    {
        cin >> a[i];
        v1.push_back(a[i]);
        v2.push_back({a[i], i});
    }
    sort(v1.begin(), v1.end());
    sort(v2.begin(), v2.end());
    for(int i = 0; i < n; i++)
    {
        int low  = lower_bound(v1.begin(), v1.end(), v1[i]) - v1.begin();
        ans[v2[i].second] = low;
    }

    while(k--)
    {
        int x,y;
        cin >> x >> y;
        x--;
        y--;
        if(a[x] > a[y])
        {
            ans[x]--;
        }
        if(a[y] > a[x])
        {
            ans[y]--;
        }
    }
    for(int i = 0; i < n; i++)
    {
        cout << ans[i] << " ";
    }
    return 0;
}
