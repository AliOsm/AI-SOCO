#include<bits/stdc++.h>
using namespace std;
const int maxn = 100005;
int a[maxn], cp[maxn];
int cng1[9] = {0, 0, 0, 1, 1, 1, -1, -1, -1};
int cng2[9] = {0, 1, -1, 0, 1, -1, 0, 1, -1};
map<int,int>mp;
set<int> st;
int vst[maxn];

int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(0);

    int n;
    cin >> n;
    for(int i = 0; i < n; i++)
    {
        cin >> a[i];
    }

    for(int i = 0; i < 9; i++)
    {
        int p = a[0] + cng1[i];
        int q = a[1] + cng2[i];
        st.insert(q - p);
    }
    if(n <= 2)
    {
        cout << 0 << endl;
        return 0;
    }
    int mn = INT_MAX;
    int val = 420;
    for(int t = -1; t <= 1; t++)
    {
        for(int s = -1; s <= 1; s++)
        {
            cp[0] = a[0] + t;
            cp[1] = a[1] + s;
            int cnt = abs(s) + abs(t);
            int x = cp[1] - cp[0];
            for(int i = 2; i < n; i++)
            {
                if(a[i] - cp[i - 1] == x)
                {
                    cp[i] = a[i];
                }
                else if(a[i]+1 - cp[i - 1] == x)
                {
                    cp[i] = a[i] + 1;
                    cnt++;
                }
                else if(a[i] - 1 - cp[i - 1] == x)
                {
                    cp[i] = a[i] - 1;
                    cnt++;
                }
                else
                {
                    cnt = INT_MAX;
                    break;
                }
            }
            mn = min(mn, cnt);
        }
    }
    // cout << val << " ";
    if(mn >= INT_MAX) mn = -1;
    cout << mn << endl;
    return 0;
}
