#include <bits/stdc++.h>
using namespace std;
#define INF 1<<30
#define endl '\n'
#define maxn 1005
#define FASTIO ios_base::sync_with_stdio(false), cin.tie(0), cout.tie(0);
typedef long long ll;
const double PI = acos(-1.0);
#define dbg(x) cerr << #x << " = " << x << endl;
#define dbg2(x, y) cerr << #x << " = " << x << ", " << #y << " = " << y << endl;
#define dbg3(x, y, z) cerr << #x << " = " << x << ", " << #y << " = " << y << ", " << #z << " = " << z << endl;

int n;
vector<int> a;
ll solve(int m)
{
    map<int, int>v;
    int sum = 0;
    ll ans = 0;
    v[sum] = 1;
    ll res = 0;
    for (int i = 0; i < n; i++) {
        if (a[i] < m) {
            sum--;
            res -= v[sum];
        }
        else {
            res += v[sum];
            sum++;
        }
        ans += res;
        v[sum]++;
    }
    return ans;
}


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
    for (int cs = 1; cs <= T; cs++) {
        int m;
        cin >> n >> m;
        a = vector<int> (n);
        for (int i = 0; i < n; i++) cin >> a[i];
        cout << solve(m) - solve(m + 1) << endl;
    }

    //double end_time = clock();
    //printf( "Time = %lf ms\n", ( (end_time - start_time) / CLOCKS_PER_SEC)*1000);
    return 0;
}