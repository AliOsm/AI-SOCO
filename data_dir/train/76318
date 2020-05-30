#include <bits/stdc++.h>
using namespace std;
#define INF 1<<30
#define endl '\n'
#define maxn 1000006
#define FASTIO ios_base::sync_with_stdio(false), cin.tie(0), cout.tie(0);
typedef long long ll;
const double PI = acos(-1.0);
#define dbg(x) cerr << #x << " = " << x << endl;
#define dbg2(x, y) cerr << #x << " = " << x << ", " << #y << " = " << y << endl;
#define dbg3(x, y, z) cerr << #x << " = " << x << ", " << #y << " = " << y << ", " << #z << " = " << z << endl;

string s[maxn];
int row[maxn], col[maxn];

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
  cin >> T;
  for (int cs = 1; cs <= T; cs++) {
    int n, m;
    cin >> n >> m;
    for (int i = 0; i <= n; i++) row[i] = 0;
    for (int i = 0; i <= m; i++) col[i] = 0;

    for (int i = 0;  i < n; i++) cin >> s[i];

      for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) {
          if (s[i][j] == '.') {
            row[i]++;
            col[j]++;
          }
        }
      }
    int ans = INF;
    for (int i = 0; i < n; i++) {
      for (int j = 0; j < m; j++) {
        int tm = row[i] + col[j];
        if (s[i][j] == '.') tm--;
        ans = min(ans, tm);
      }
    }
    cout << ans << endl;
  }

  //double end_time = clock();
  //printf( "Time = %lf ms\n", ( (end_time - start_time) / CLOCKS_PER_SEC)*1000);
  return 0;
}