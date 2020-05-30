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

const int oo = 1e9, mxn = 100010;
int A[mxn];

int main() {
	ios_base::sync_with_stdio(false); cin.tie(0);
	int n, t; cin >> n >> t;
	fori(i, 0, n)
		cin >> A[i];
	int l = 0, r = 0, ans = 0, sum = 0;
	while (r < n) {
		sum += A[r];
		while (l <= r && sum > t) sum -= A[l], l++;
		ans = max(ans, r - l + 1);
		r++;
	}
	cout << ans << endl;
	return 0;
}