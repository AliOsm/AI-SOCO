#pragma comment(linker, "/stack:247474112")
#pragma GCC optimize("Ofast")

#include <bits/stdc++.h>
using namespace std;

#define endl '\n'
mt19937 rng32(chrono::steady_clock::now().time_since_epoch().count());
mt19937_64 rng64(chrono::steady_clock::now().time_since_epoch().count());

int n; vector<int> a;

void Input() {
	cin >> n; a.resize(n);
	for (auto &z: a) cin >> z;
}

void Solve() {
	sort(a.begin(), a.end());
	long long res = 0;
	for (int i=0; i<n; i++) {
		int j = n - 1 - i;
		if (i > j) continue;
		res += 1LL * (a[i] + a[j]) * (a[i] + a[j]);
	}
	cout << res << endl;
}

int main(int argc, char* argv[]) {
	ios_base::sync_with_stdio(0); cin.tie(NULL);
	Input(); Solve(); return 0;
}

/******************************************\
*  Thuy-Trang Tran, #Team4T's Leader     *
*  #Team4T Primary Flagship - Salvation  *
\******************************************/
