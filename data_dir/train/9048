#include <bits/stdc++.h>
#define fast ios::sync_with_stdio(0); cin.tie(0); cout.tie(0)
#define pb push_back
#define endl '\n'
#define MOD 1000000007

using namespace std;
typedef long long int ll;

int pi[1000010];
int pi2[1000010];

void pre_fun(string &s, int a[])
{
	int n = s.size();
	for (int i = 1; i < n; ++i)
	{
		int j = a[i-1];
		while (j > 0 and s[i] != s[j]) j = a[j-1];
		if (s[i] == s[j]) ++j;
		a[i] = j;
	}
}

int main(void)
{
	#ifndef ONLINE_JUDGE
	freopen("in.txt", "r", stdin);
	#endif
	fast;
	string s; cin >> s;
	pre_fun(s, pi);
	int n = s.size();
	set<int> vals;
	int k = n-1;
	while (1)
	{
		if (pi[k] == 0) break;
		vals.insert(pi[k]);
		k = pi[k]-1;
	}
	int ans = 0;
	for (int i = 1; i < n-1; ++i)
	{
		if (vals.find(pi[i]) != vals.end()) ans = max(ans, pi[i]);
	}
	if (ans == 0) cout << "Just a legend\n";
	else cout << s.substr(0, ans) << '\n';
}