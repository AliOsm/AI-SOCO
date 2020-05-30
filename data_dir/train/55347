#include <bits/stdc++.h>
#define endl '\n'
#define debug(X) cout << #X << " = " << X << endl
#define fori(i,b,e) for (int i = (b); i < (e); ++i)
#define mod(x,m) ((((x) % (m)) + (m)) % (m))
#define sq(x) (x) * (x)

using namespace std;

typedef long long ll;
typedef vector<int> vi;
typedef vector<vi> vvi;
typedef pair<int, int> ii;
typedef vector<ii> vii;

const int oo = 1e9;

bool cmp(ii a, ii b) {
	return abs(a.first) + abs(a.second) < abs(b.first) + abs(b.second);
}

int main() {
	ios_base::sync_with_stdio(false); cin.tie(0);
	int n; cin >> n;
	vii points(n);
	fori(i, 0, n)
		cin >> points[i].first >> points[i].second;
	sort(points.begin(), points.end(), cmp);
	int cnt = 0;
	fori(i, 0, n) {
		cnt += 2;
		if (abs(points[i].first) > 0) cnt += 2;
		if (abs(points[i].second) > 0) cnt += 2;
	}
	cout << cnt << endl;
	fori(i, 0, n) {
		int x = points[i].first, y = points[i].second;
		if (abs(x) > 0)
			cout << 1 << " " << abs(x) << " " << (x < 0 ? "L" : "R") << endl;
		if (abs(y) > 0)
			cout << 1 << " " << abs(y) << " " << (y < 0 ? "D" : "U") << endl;
		cout << 2 << endl;
		if (abs(x) > 0)
			cout << 1 << " " << abs(x) << " " << (x < 0 ? "R" : "L") << endl;
		if (abs(y) > 0)
			cout << 1 << " " << abs(y) << " " << (y < 0 ? "U" : "D") << endl;
		cout << 3 << endl;
	}
	return 0;
}