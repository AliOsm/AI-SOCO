// I can't tell you what it really is,
// I can only tell you what it feels like.
#include "bits/stdc++.h"
using namespace std;
 
#define int long long
#define F first
#define S second
#define sz(x) ((int)x.size())
#define rep(i,a,n) for (int i = a; i <= n; ++i)
#define all(v)  v.begin(), v.end()
#define pb push_back
#define P pair < int, int >
#define E cout << '\n'

const int mod = 1e9 + 7;
const int N = 4e5 + 5;

int a[3][N];
vector < int > v[N];
vector < int > temp(1);

void dfs(int x, int p) {
	temp.pb(x);
	// cout << x << ' ';
	for (int i : v[x]) {
		if (i != p)
			dfs(i, x);
	}
}
int arr[N];
 
inline void solve() {
   int n;
   cin >> n;
   rep(i,0,2)
   	rep(j,1,n) {
   		cin >> a[i][j];
   	}
   rep(i,2,n) {
   	int l, r;
   	cin >> l >> r;
   	v[l].pb(r);
   	v[r].pb(l);
   }
   int st = -1;
   rep(i,1,n) {
   	if (sz(v[i]) > 2) {
   		cout << "-1\n";
   		return;
   	}
   	if (sz(v[i]) == 1) {
   		st = i;
   	}
   }
   dfs(st,st);
   // E;
   vector< int > col = {0, 1, 2};
   vector < int > ok;
   int fin = 1e18;
   while (1) {
   	int ans = 0;
   	// for (int i : col) {
   	// 	cout << i << ' ';
   	// }
   		for (int i = 1; i <= n; ++i) {
   			ans += a[col[(i-1)%3]][temp[i]];
   		}
   		// cout << ans << '\n';
   		if (ans < fin) {
   			fin = ans;
   			ok = col;
   		}
   	bool f = next_permutation(all(col));
   	if (!f)break;
   }
   // for (int x : col) {
   // 	cout << x << ' ';
   // }
   // E;
   cout << fin << '\n';
   rep(i,1,n) {
   	arr[temp[i]] = ok[(i-1)%3];
   }
   rep(i,1,n) {
   	cout << arr[i]+1 << ' ';
   }

}
signed main() {
  ios_base::sync_with_stdio(0);
  cin.tie(NULL);
  cout.tie(NULL);
  int t = 1;
  //cin >> t; while(t--)
  solve();
  return 0;
}