#include <bits/stdc++.h>
using namespace std;
#define INF 1<<30
#define endl '\n'
#define maxn 300005
#define FASTIO ios_base::sync_with_stdio(false), cin.tie(0), cout.tie(0);
typedef long long ll;
const double PI = acos(-1.0);
#define dbg(x) cerr << #x << " = " << x << endl;
#define dbg2(x, y) cerr << #x << " = " << x << ", " << #y << " = " << y << endl;
#define dbg3(x, y, z) cerr << #x << " = " << x << ", " << #y << " = " << y << ", " << #z << " = " << z << endl;

int v[maxn];
int pos[maxn];
int tmp[maxn];

pair<int, int>a[maxn];
pair<int, int> b[maxn];

bool solve(int l, int r)
{
	if (l == r) return true;

	int mid = (l + r) / 2;
	if (!solve(l, mid)) return false;
	if (!solve(mid + 1, r)) return false;

	int mx = 0, x = l, y = l;

	for (int i = mid + 1; i <= r; i++) {
		while (y <= mid && v[y] < v[i]) {
			mx = max(mx, pos[v[y]]);
			tmp[x++] = v[y++];
		}
		if (pos[v[i]] < mx) return false;
		tmp[x++] = v[i];
	}

	while (y <= mid)tmp[x++] = v[y++];
	for (int i = l; i <= r; i++)
		v[i] = tmp[i];

	return true;
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
	//T = 1;
	scanf("%d", &T);
	for (int cs = 1; cs <= T; cs++) {
		int n;
		scanf("%d", &n);
		for (int i = 1; i <= n; i++) {
			scanf("%d", &a[i].first);
			a[i].second = i;
		}

		for (int i = 1; i <= n; i++) {
			scanf("%d", &b[i].first);
			b[i].second = i;
		}

		sort(a + 1, a + n + 1);
		sort(b + 1, b + n + 1);

		bool ok = true;

		for (int i = 1; i <= n; i++) {
			if (a[i].first != b[i].first) {
				ok = false;
				cout << "NO\n";
				break;
			}
		}
		if (!ok) continue;

		for (int i = 1; i <= n; i++) {
			a[i].first = i;
			swap(a[i].first, a[i].second);
		}

		for (int i = 1; i <= n; i++) {
			b[i].first = i;
			swap(b[i].first, b[i].second);
		}

		sort(a + 1, a + n + 1);
		sort(b + 1, b + n + 1);

		for (int i = 1; i <= n; i++) {
			swap(a[i].first, a[i].second);
		}
		for (int i = 1; i <= n; i++) {
			swap(b[i].first, b[i].second);
		}

		for (int i = 1; i <= n; i++) {
			v[i] = a[i].first;
		}
		for (int i = 1; i <= n; i++) {
			pos[b[i].first] = i;
		}

		if (solve(1, n)) cout << "YES\n";
		else cout << "NO\n";
	}

	//double end_time = clock();
	//printf( "Time = %lf ms\n", ( (end_time - start_time) / CLOCKS_PER_SEC)*1000);
	return 0;
}