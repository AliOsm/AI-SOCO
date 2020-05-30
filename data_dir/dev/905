#include <bits/stdc++.h>

using namespace std;

#define MOD 1000000007
#define ll long long int
#define ld long double
#define pb push_back
#define mkp make_pair
#define pii pair<int, int> 
#define pll pair<long long int, long long int>
#define sci(x) scanf("%d", &x)
#define scl(x) scanf("%lld", &x)
#define fi first
#define sc second
#define eps 1e-9

string s[2005];
int M[2005][2005], L[2005][2005], R[2005][2005];
int n, m, l, r;
int xr[] = {-1, 0, 0, 1};
int xc[] = {0, -1, 1, 0};
int xL[] = {0, 1, 0, 0};
int xR[] = {0, 0, 1, 0};

bool safe(int a, int b, int c, int d) {
	return (a >= 0 && a < n && b >= 0 && b < m && c <= l && d <= r && s[a][b] == '.' && M[a][b] == 0); 
}

void fill(int x, int y) {
	multiset<pair<int, pii>> q;
	q.insert(mkp(0, mkp(x, y)));
	L[x][y] = R[x][y] = 0;
	while (!q.empty()) {
		auto it = *q.begin();
		q.erase(q.begin());
		x = it.sc.fi, y = it.sc.sc;
		if (M[x][y]) continue;
		M[x][y] = 1;
		for (int i = 0; i < 4; ++i) {
			int a = x + xr[i];
			int b = y + xc[i];
			int l = L[x][y] + xL[i];
			int r = R[x][y] + xR[i];
			if (safe(a, b, l, r) && l < L[a][b] && r < R[a][b]) {
				L[a][b] = l;
				R[a][b] = r;
				q.insert(mkp(l, mkp(a, b)));
			}
		}
	}
}

int count() {
	int ans = 0;
	for (int i = 0; i < n; ++i) {
		for (int j = 0; j < m; ++j) {
			ans += M[i][j];
		}
	}

	return ans;
}

int main()
{
	ios_base::sync_with_stdio(false);cout.tie(0);cin.tie(0);

	int i, j, k, x, y, z;
	cin >> n >> m;
	cin >> x >> y;
	cin >> l >> r;
	for (i = 0; i < n; ++i) cin >> s[i];
	for (i = 0; i < n; ++i) {
		for (j = 0; j < m; ++j) L[i][j] = R[i][j] = MOD;
	}
	fill(x-1, y-1);
	cout << count() << endl;

	return 0;
}
