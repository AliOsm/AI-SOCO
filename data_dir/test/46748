#include <bits/stdc++.h> 
using namespace std;
typedef long long ll;

bool left(pair<int, int> f, pair<int, int> s, pair<int, int> t) {
	return s.second > f.second xor t.first < s.first or s.first > f.first xor t.second > s.second;
}

int main() {
	ios_base::sync_with_stdio(0), cin.tie(0), cout.tie(0);
	int n, ans = 0;
	cin >> n;
	int x, y;
	deque<pair<int, int> > q;
	while (n--) {
		cin >> x >> y;
		q.push_front( { x, y });

		if (q.size() == 3) {
			ans += left(q[0], q[1], q[2]);
			q.pop_back();
		}
	}
	cout << ans;
}
