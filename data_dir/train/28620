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

const int oo = 1e9, mxn = 3010;
int A[mxn], B[mxn];

int main() {
	ios_base::sync_with_stdio(false); cin.tie(0);
	int n, v; cin >> n >> v;
	fori(i, 0, n) {
		int a, b; cin >> a >> b;
		A[a] += b;
	}
	int ans = 0;
	fori(i, 0, mxn) {
		int x = min(v, B[i]);
		int d = v - x;
		int y = min(d, A[i]);
		B[i + 1] = A[i] - y;
		ans += x + y;
	}
	cout << ans << endl;
	return 0;
}