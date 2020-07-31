#include <bits/stdc++.h>
#define endl '\n'
#define debug(X) cout << #X << " = " << X << endl
#define fori(i,b,e) for (int i = (b); i < (e); ++i)
#define mod(x,m) ((((x) % (m)) + (m)) % (m))
#define sq(x) (x) * (x)

using namespace std;

typedef long long ll;
typedef vector<int> vi;
typedef vector<vi> vvi;
typedef pair<int, int> ii;
typedef vector<ii> vii;

const int oo = 1e9, MX = 1e5;

int maxh[MX], ren[MX], out[MX];

struct Event {
	int tm, id, h, tp;
	Event() {}
	Event(int _tm, int _id, int _h, int _tp) : tm(_tm), id(_id), h(_h), tp(_tp) {}
	bool operator < (const Event &o) const {
		if (tm != o.tm) return tm > o.tm;
		return tp > o.tp;
	}
};

int main() {
	ios_base::sync_with_stdio(false); cin.tie(0);
	int n, m; cin >> n >> m;
	ll bou, inc, dam; cin >> bou >> inc >> dam;
	priority_queue<Event> pq;
	int flag = 0;
	fori(i, 0, n) {
		int sh; cin >> maxh[i] >> sh >> ren[i];
		if (maxh[i] <= dam) flag = 1;
		pq.push(Event(0, i, sh, 0));
	}
	while (m--) {
		int t, e, h; cin >> t >> e >> h; e--;
		pq.push(Event(t, e, h, 0));
	}
	if (flag && inc != 0) {
		cout << -1 << endl;
		return 0;
	}
	memset(out, -1, sizeof out);
	ll ans = 0, cnt = 0;
	flag = 0;
	while (!pq.empty()) {
		Event e = pq.top(); pq.pop();
		//cout << e.tm << " " << e.tp << " " << e.id << " " << cnt << endl;
		if (inc != 0 && e.tm == oo) { flag = 1; continue; }
		if (e.tp == 0) {
			if (e.h > dam) {
				if (out[e.id] != -1) {
					ans = max(ans, cnt * (bou + (e.tm - 1) * inc));
					cnt--;
				}
				out[e.id] = -1;
			} else {
				if (out[e.id] == -1) cnt++;
				int time_out = (ren[e.id] == 0 || maxh[e.id] <= dam) ? oo : (dam - e.h) / ren[e.id] + e.tm;
				pq.push(Event(time_out, e.id, -1, 1));
				out[e.id] = time_out;
				ans = max(ans, cnt * (bou + e.tm * inc));
			}
		} else {
			if (out[e.id] != e.tm) continue;
			ans = max(ans, cnt * (bou + e.tm * inc));
			out[e.id] = -1;
			cnt--;
		}
	}
	cout << (flag ? -1 : ans) << endl;
	return 0;
}