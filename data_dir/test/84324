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

const int oo = 1e9;

bool check(int a, int b) { return a <= b && b <= 2 * a; }

int main() {
	ios_base::sync_with_stdio(false); cin.tie(0);
	int gl, gr; cin >> gl >> gr;
	int bl, br; cin >> bl >> br;
	if (check(gl - 1, br) || check(gl, br) || check(gl + 1, br) || 
		check(gr - 1, bl) || check(gr, bl) || check(gr + 1, bl))
		cout << "YES" << endl;
	else
		cout << "NO" << endl;
	return 0;
}