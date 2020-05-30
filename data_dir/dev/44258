#include <bits/stdc++.h>

using namespace std;
#define ll long long
#define ull unsigned long long
#define all(v)  	((v).begin()),((v).end())
#define sz(x)  		((ll) (x).size())
#define clr(a,b)	memset(a,b,sizeof(a))
const double EPS = 1e-8;
const double pi = acos(-1);
ll dcmp(double a, double b) {
	return fabs(a - b) <= EPS ? 0 : a < b ? -1 : 1;
}
void debug() {
#ifndef ONLINE_JUDGE
	freopen("input.in", "rt", stdin);
//	freopen("output.in", "wt", stdout);
#endif
}

int const N = 200000 + 9, M = 100 + 9, OO = 1e9;

vector<vector<int>> vec1(130);
vector<vector<int>> vec2(130);

vector<pair<int, int>> ans;

int main() {
	cout << fixed << setprecision(12);
	ios::sync_with_stdio(false), cin.tie(nullptr), cout.tie(nullptr);
	debug();
	int n;
	cin >> n;
	char c;
	for (int i = 0; i < n; ++i) {
		cin >> c;
		vec1[c].push_back(i);
	}
	for (int i = 0; i < n; ++i) {
		cin >> c;
		vec2[c].push_back(i);
	}
	for (int i = 'a'; i <= 'z'; ++i) {
		int mn = min(vec1[i].size(), vec2[i].size());
		for (int j = mn - 1; j >= 0; --j) {
			ans.push_back(
					{ vec1[i][vec1[i].size() - 1], vec2[i][vec2[i].size() - 1] });
			vec1[i].pop_back();
			vec2[i].pop_back();
		}
	}
	for (int i = 'a'; i <= 'z'; ++i) {
		int mn = vec2[i].size();
		if (vec1['?'].empty())
			break;
		for (int j = mn - 1; j >= 0; --j) {
			if (vec1['?'].empty())
				break;
			ans.push_back( { vec1['?'][vec1['?'].size() - 1], vec2[i][j] });
			vec1['?'].pop_back();
			vec2[i].pop_back();
		}
		if (i == 'z') {
			i = '?';
			int mn = vec2[i].size();
			if (vec1['?'].empty())
				break;
			for (int j = mn - 1; j >= 0; --j) {
				if (vec1['?'].empty())
					break;
				ans.push_back( { vec1['?'][vec1['?'].size() - 1], vec2[i][j] });
				vec1['?'].pop_back();
				vec2[i].pop_back();
			}
			i = 'z';
		}
	}
	for (int i = 'a'; i <= 'z'; ++i) {
		int mn = vec1[i].size();
		if (vec2['?'].empty())
			break;
		for (int j = mn - 1; j >= 0; --j) {
			if (vec2['?'].empty())
				break;
			ans.push_back( { vec1[i][j], vec2['?'][vec2['?'].size() - 1] });
			vec2['?'].pop_back();
			vec1[i].pop_back();
		}
		if (i == 'z') {
			i = '?';
			int mn = vec1[i].size();
			if (vec2['?'].empty())
				break;
			for (int j = mn - 1; j >= 0; --j) {
				if (vec2['?'].empty())
					break;
				ans.push_back( { vec2[i][j], vec1['?'][vec1['?'].size() - 1] });
				vec2['?'].pop_back();
				vec1[i].pop_back();
			}
			i = 'z';
		}
	}
	cout << ans.size() << "\n";
	for (auto it : ans) {
		cout << it.first + 1 << " " << it.second + 1 << "\n";
	}
}