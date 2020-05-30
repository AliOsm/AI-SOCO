#pragma comment(linker, "/stack:252457298")
#pragma GCC optimize("Ofast")

#include <bits/stdc++.h>
using namespace std;

#define endl '\n'
mt19937 rng32(chrono::steady_clock::now().time_since_epoch().count());
mt19937_64 rng64(chrono::steady_clock::now().time_since_epoch().count());

int n, x, y; char cmd;
int MaxLo = 0, MaxHi = 0;

void Input() {
	cin >> n;
}

void Solve() {
	while (n--) {
		cin >> cmd >> x >> y;
		if (cmd == '+') {
			MaxLo = max(MaxLo, min(x, y));
			MaxHi = max(MaxHi, max(x, y));
		}
		else if (cmd == '?') {
			if (min(x, y) < MaxLo) cout << "NO\n";
			else if (max(x, y) < MaxHi) cout << "NO\n";
			else cout << "YES\n";
		}
	}
}

int main(int argc, char* argv[]) {
	ios_base::sync_with_stdio(0); cin.tie(NULL);
	Input(); Solve(); return 0;
}

/**********************************************\
*  Ngoc-Mai Ngo, #Team4T's Deputy Leader     *
*  #Team4T Secondary Flagship - Destruction  *
\**********************************************/
