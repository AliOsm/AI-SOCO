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

int n; vector<int> a;

void Input() {
	cin >> n; a.resize(n);
	for (auto &z: a) cin >> z;
}

void Solve() {
	int ans = 0, pre = 0, suf = 0;
	for (int i=0; i<n; i++) {
		if (!a[i]) continue;
		int j = i;
		while (j+1 < n && a[j+1]) j++;
		ans = max(ans, j-i+1); i = j;
	}
	if (ans == n) {cout << ans << endl; return;}
	while (pre < n && a[pre]) pre++;
	while (suf < n && a[n-1-suf]) suf++;
	ans = max(ans, pre + suf); cout << ans << endl;
}

int main(int argc, char* argv[]) {
	ios_base::sync_with_stdio(0); cin.tie(NULL);
	Input(); Solve(); return 0;
}

/******************************************\
 *  Thuy-Trang Tran, #Team4T's Leader     *
 *  #Team4T Primary Flagship - Salvation  *
\******************************************/