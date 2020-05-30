#include <bits/stdc++.h>
#define endl '\n'
#define debug(X) cout << #X << " = " << X << endl
#define fori(i,b,e) for (int i = (b); i < (e); ++i)
#define mod(x,m) ((((x) % (m)) + (m)) % (m))
#define sq(x) (x) * (x)

using namespace std;

typedef long long ll;
typedef vector<int> vi;
typedef pair<int, int> ii;
typedef vector<ii> vii;

const int oo = 1e9, mxn = 200010;
int A[mxn];

int main() {
	ios_base::sync_with_stdio(false); cin.tie(0);
	int n, q; cin >> n >> q;
	priority_queue<int> pq1;
	fori(i, 0, n) {
		int x; cin >> x;
		pq1.push(x);
	}
	while (q--) {
		int a, b; cin >> a >> b; a--; b--;
		A[a]++;
		if (b + 1 < n) A[b + 1]--;
	}
	priority_queue<int> pq2;
	pq2.push(A[0]);
	fori(i, 1, n) {
		A[i] += A[i - 1];
		pq2.push(A[i]);
	}
	ll ans = 0;
	while (!pq1.empty()) {
		ll u = pq1.top(); pq1.pop();
		ll v = pq2.top(); pq2.pop();
		ans += u * v;
	}
	cout << ans << endl;
	return 0;
}