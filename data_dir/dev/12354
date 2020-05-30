#pragma GCC optimize("Ofast")

#include <bits/stdc++.h>
using namespace std;

#define y0 holdtheflower
#define y1 enjoythecolorandscent
#define yn walkthroughthesoulgarden
#define j1 feelthewarmbreathofkindnessandsalvation

#define endl '\n'
mt19937 rng32(chrono::steady_clock::now().time_since_epoch().count());
mt19937_64 rng64(chrono::steady_clock::now().time_since_epoch().count());

long long H; int n; vector<int> d;
vector<long long> ps;

bool possibleClear(long long cycles) {
	long long Rem = H + cycles * ps[n-1];
	if (Rem <= 0) return true;
	for (int i=0; i<n-1; i++) {
		if (Rem + ps[i] <= 0) return true;
	}
	return false;
}

long long binsearch(long long L, long long R) {
	long long res = R;
	while (L <= R) {
		long long mid = (L + R) / 2;
		if (possibleClear(mid)) {res = mid; R = mid - 1;}
		else L = mid + 1;
	}
	return res;
}

void Input() {
	cin >> H >> n; d.resize(n);
	for (auto &z: d) cin >> z;
}

void Solve() {
	ps.resize(n, d[0]);
	for (int i=1; i<n; i++) ps[i] = ps[i-1] + d[i];
	if (ps[n-1] >= 0) {
		for (int i=0; i<n-1; i++) {
			if (H + ps[i] <= 0) {cout << i + 1 << endl; return;}
		}
		cout << "-1\n"; return;
	}
	long long MinCycles = binsearch(0LL, -H / ps[n-1] + 4);
	if (H + ps[n-1] * MinCycles <= 0) {cout << (MinCycles * n) << endl; return;}
	for (int i=0; i<n-1; i++) {
		if (H + ps[n-1] * MinCycles + ps[i] <= 0) {
			cout << (MinCycles * n + i + 1) << endl;
			return;
		}
	}
}

int main(int argc, char* argv[]) {
	ios_base::sync_with_stdio(0); cin.tie(NULL);
	Input(); Solve(); return 0;
}

/******************************************\
 *  Thuy-Trang Tran, #Team4T's Leader     *
 *  #Team4T Primary Flagship - Salvation  *
\******************************************/