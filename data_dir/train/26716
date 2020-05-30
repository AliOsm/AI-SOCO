/// upsolve: topic- BFS
#include <bits/stdc++.h>
using namespace std;
#define INF1 1<<30
#define endl '\n'
#define maxn 100005
#define FASTIO ios_base::sync_with_stdio(false), cin.tie(0), cout.tie(0);
typedef long long ll;
const double PI = acos(-1.0);
#define dbg(x) cerr << #x << " = " << x << endl;
#define dbg2(x, y) cerr << #x << " = " << x << ", " << #y << " = " << y << endl;
#define dbg3(x, y, z) cerr << #x << " = " << x << ", " << #y << " = " << y << ", " << #z << " = " << z << endl;

const ll INF = 1e12;


int main()
{
    FASTIO
    ///*
    //double start_time = clock();
#ifndef ONLINE_JUDGE
    freopen("in.txt", "r", stdin);
    freopen("out.txt", "w", stdout);
    freopen("error.txt", "w", stderr);
#endif
//*/
    int T;
    //cin >> T;
    T = 1;
    for(int cs = 1; cs <= T; cs++)
    {
        ll n, k;
        string s;
        cin >> n >> k >> s;
        --k;
        vector<vector<int>> lst(n, vector<int> (26, -1));
        for(int i = 0; i < n; i++)
        {
            for(int j = 0; j < 26; j++)
            {
                if(i > 0) lst[i][j] = lst[i - 1][j];
            }
            lst[i][s[i] - 'a'] = i;
        }

        vector<vector<ll> > dp(n+2, vector<ll> (n+2));

        for(int i = 0; i < n; i++) dp[i][1] = 1;

        for(int l = 2; l < n; l++)
        {
            for(int i = 1; i < n; i++)
            {
                for(int j = 0; j < 26; j++)
                {
                    if(lst[i - 1][j] != -1)
                    {
                        dp[i][l] = min(INF,  dp[i][l] + dp[lst[i - 1][j]][l - 1]);
                    }
                }
            }
        }
        ll ans = 0;
        for(int l = n - 1; l >= 1; l--)
        {
            ll cnt = 0;
            for(int j = 0; j < 26; j++)
            {
                if(lst[n - 1][j] != -1)
                {
                    cnt += dp[lst[n - 1][j]][l];
                }
            }
                if(cnt >= k)
                {
                    ans += k * (n - l);
                    k = 0;
                    break;
                }
                else
                {
                    ans += cnt * (n - l);
                    k -= cnt;
                }
        }

        if(k == 1)
        {
            ans += n;
            --k;
        }
        if(k > 0) cout << -1 << "\n";
        else cout << ans << endl;
    }


    //double end_time = clock();
    //printf( "Time = %lf ms\n", ( (end_time - start_time) / CLOCKS_PER_SEC)*1000);
    return 0;
}
