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

const int oo = 1e9, mxn = 500010;
int A[mxn];

int main() {
	ios_base::sync_with_stdio(false); cin.tie(0);
	int n; cin >> n;
	fori(i, 0, n)
		cin >> A[i];
	sort(A, A + n);
	int mid = n / 2, ans = 0;
	for (int i = 0, j = mid; i < mid; i++) {
		while (j < n && 2 * A[i] > A[j]) j++;
		if (j == n) break;
		j++;
		ans++;
	}
	cout << n - ans << endl;
	return 0;
}