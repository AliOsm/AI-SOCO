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

const int oo = 1e9, MX = 1e5 + 1;

int main() {
	ios_base::sync_with_stdio(false); cin.tie(0);
	int n, k; cin >> n >> k;
	vector<int> v(n), freq(MX);
	fori(i, 0, n)
		cin >> v[i];
	int l = 0, r = 0, ndiff = 0;
	while (r < n && ndiff < k) {
		if (freq[v[r]] == 0) ndiff++;
		freq[v[r]]++;
		r++;
	}
	if (r == n && ndiff < k) {
		cout << -1 << " " << -1 << endl;
	} else {
		while (freq[v[l]] > 1) { freq[v[l]]--; l++; }
		cout << l + 1 << " " << r << endl;
	}
	return 0;
}