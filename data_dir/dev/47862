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

vector<int> prefixFunction(const string& s)
{
	int n = s.size();
	int k = 0;

	vector<int> v(n + 1);
	v[1] = 0;
	for (int i = 2; i <= n; i++) {
		while (k > 0 && s[k] != s[i - 1]) k = v[k];
		if (s[k] == s[i - 1]) k++;
		v[i] = k;
	}
	return v;
}

vector<int> KMP(const string& text, const string& pattern)
{
	vector<int> pi = prefixFunction(pattern);
	int k = 0;
	int match = 0;
	vector<int> z;
	for (int i = 0; i < (int)text.size(); i++) {
		while (k > 0 && text[i] != pattern[k]) k = pi[k];
		if (text[i] == pattern[k])k++;
		z.push_back(k);
		if (k == (int)pattern.size()) {
			// full pattern match found
			match++;
			k = pi[k];
		}
	}

	for (int i = 1; i < (int)text.size(); i++) {
		z[i] = max(z[i], z[i - 1]);
	}
	return z;
}

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
	string s;
	cin >> s;
	string rs(s);
	reverse(rs.begin(), rs.end());
	int n = s.size();
	int m;
	cin >> m;
	int ans = 0;
	while (m--) {
		string p;
		cin >> p;
		int x = p.size();
		if (x == 1) continue;

		string rp = p;
		reverse(rp.begin(), rp.end());
		vector<int> z1 = KMP(s, p);
		vector<int> z2 = KMP(rs, rp);
		reverse(z2.begin(), z2.end());

		for (int i = 0; i + 1 < n; i++) {
			if (z1[i] + z2[i + 1] >= x) {
				ans++;
				break;
			}
		}
	}
	cout << ans << endl;
}