#include <bits/stdc++.h>
using namespace std;
#define INF 1<<30
#define endl '\n'
#define maxn 100005
#define tc printf("Case %d: ", cs)
#define tcn printf("Case %d:\n", cs);
#define FASTIO ios_base::sync_with_stdio(false), cin.tie(0), cout.tie(0);
typedef long long ll;
const double PI = acos(-1.0);

#define dbg1(x) cerr << #x << " = " << x << endl;
#define dbg2(x, y) cerr << #x << " = " << x << ", " << #y << " = " << y << endl;
#define dbg3(x, y, z) cerr << #x << " = " << x << ", " << #y << " = " << y << ", " << #z << " = " << z << endl;
#define dbg4(w,x, y, z) cerr << #w << " = " << w << ", " <<#x << " = " << x << ", " << #y << " = " << y << ", " << #z << " = " << z << endl;

template < typename F, typename S >
ostream& operator << ( ostream& os, const pair< F, S > & p ) {
	return os << "(" << p.first << ", " << p.second << ")";
}

template < typename T >
ostream &operator << ( ostream & os, const vector< T > &v ) {
	os << "{";
	for (auto it = v.begin(); it != v.end(); ++it) {
		if ( it != v.begin() ) os << ", ";
		os << *it;
	}
	return os << "}";
}

template < typename T >
ostream &operator << ( ostream & os, const set< T > &v ) {
	os << "[";
	for (auto it = v.begin(); it != v.end(); ++it) {
		if ( it != v.begin()) os << ", ";
		os << *it;
	}
	return os << "]";
}

template < typename F, typename S >
ostream &operator << ( ostream & os, const map< F, S > &v ) {
	os << "[";
	for (auto it = v.begin(); it != v.end(); ++it) {
		if ( it != v.begin() ) os << ", ";
		os << it -> first << " = " << it -> second ;
	}
	return os << "]";
}

#define dbg(args...) do {cerr << #args << " : "; faltu(args); } while(0)

clock_t tStart = clock();
#define timeStamp dbg("Execution Time: ", (double)(clock() - tStart)/CLOCKS_PER_SEC)

void faltu () { cerr << endl; }

template <typename T>
void faltu( T a[], int n ) {
	for (int i = 0; i < n; ++i) cerr << a[i] << ' ';
	cerr << endl;
}

template <typename T, typename ... hello>
void faltu( T arg, const hello &... rest) { cerr << arg << ' '; faltu(rest...); }
// Program showing a policy-based data structure.
#include <ext/pb_ds/assoc_container.hpp> // Common file 
#include <ext/pb_ds/tree_policy.hpp>
#include <functional> // for less 
#include <iostream>
using namespace __gnu_pbds;
using namespace std;
// GNU link : https://goo.gl/WVDL6g
typedef tree<int, null_type, less_equal<int>, rb_tree_tag,
        tree_order_statistics_node_update>
        new_data_set;

/**___________________________________________________**/

set<int> st[maxn];
int cnt[maxn];

int main()
{
	FASTIO
	///*
#ifndef ONLINE_JUDGE
	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);
	freopen("error.txt", "w", stderr);
#endif
//*/

	int n;
	cin >> n;
	for (int i = 0; i < n - 2; i++) {
		int a, b, c;
		cin >> a >> b >> c;
		st[a].insert(b);
		st[a].insert(c);

		st[b].insert(a);
		st[b].insert(c);

		st[c].insert(a);
		st[c].insert(b);
	}
	int val = 0;
	for (int i = 1; i <= n; i++) {
		//dbg(i, st[i]);
		cnt[i] = (int)st[i].size();
		//dbg(i, cnt[i]);
	}

	for (int i = 1; i <= n; i++) {
		if ((int)st[i].size() == 2) {
			val = i;
			break;
		}
	}

	for (int i  = 1; i <= n; i++) {
		cout << val << " ";
		pair<int, int>  nxt = {INT_MAX, 0};
		//dbg(val,st[val]);
		for (auto x : st[val]) {
			//dbg(x, st[x]);
			st[x].erase(val);
			//dbg(x, st[x]);
			if (nxt.first == (int)st[x].size()) {
				if (cnt[nxt.second] < cnt[x]) {
					nxt = {(int)st[x].size(), x};
				}
			}
			else nxt = min(nxt, {(int)st[x].size(), x});
			//dbg(nxt);
		}
		val = nxt.second;
		//cerr << "-----------------------------------\n";
	}

}