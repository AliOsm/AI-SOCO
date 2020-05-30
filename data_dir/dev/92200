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
    int n, m;
    cin >> n >> m;
    vector<int > a(n);
    for (int i = 0; i < n; i++) cin >> a[i];

    map<int, int > cnt;
    cnt[0] = 1;
    bool flag = false;

    ll ans = 0;
    ll sum = 0;
    for (int l = 0; l  < n; l++) {
      if (a[l] < m) sum--;
      else if (a[l] > m) sum++;
      if (a[l] == m) flag = true;
      if (flag) ans += cnt[sum] + cnt[sum - 1];
      else cnt[sum]++;
    }
    cout << ans << endl;
  }

  //double end_time = clock();
  //printf( "Time = %lf ms\n", ( (end_time - start_time) / CLOCKS_PER_SEC)*1000);
  return 0;
}