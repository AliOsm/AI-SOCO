;
//be naame khodaa
#include <iostream>
#include <cmath>
#include <vector>
#include <queue>
#include <stack>
#include <map>
#include <string>
#include <cstdio>
#include <algorithm>
#include <set>
#include <cassert>
#include <iomanip>
#include <cstring>
#include <sstream>
#include <complex>
#define pb push_back

using namespace std;
typedef long long ll;

const int N = 1000*1000 + 5;

int f[N], z[N];

void calcz(string s, int n){
	fill(z, z + n, 0);
	z[0] = n;
	int l =0, r = 0;
	for (int i = 1; i < n; i++){
		if (r > i) 
			z[i] = min(r-i, z[i-l]);
		while (i+z[i] < n && s[i+z[i]] == s[z[i]]) 
			z[i]++;
		if (i+z[i] > r) 
			l = i, r = i+z[i];
	}
}

void calcf(string s, int n){
	f[0] = -1;
	for (int i = 1; i <= n; i++){
		f[i] = f[i-1];
		while (f[i] >= 0 && s[i-1] != s[f[i]])
			f[i] = f[f[i]];
		f[i]++;
	}
}

int patMatch(string t, string s, int n){
	int cur = 0, ans = 0;
	for (int i = 0; i < t.size(); i++){
		while (cur >= 0 && t[i] != s[cur])
			cur = f[cur];
		cur++;
		if (cur == n) cout << i-n+1 << '\n', cur = f[n], ans++;
	}
	return ans;
}

int main(){
	ios::sync_with_stdio(0);
	string t, s;
	cin >> s;
	int n = s.length();
	calcz(s, n);
	int inix = 0;
	for (int i = 1; i < n; i++)
	{
		if (z[i] == n-i && inix >= z[i])
		{
			cout << s.substr(i, z[i]) << endl;
			return 0;
		}
		inix = max(inix, z[i]);
	}
	cout << "Just a legend\n";
	return 0;
	calcf(s, n);
	patMatch(t, s, n);
}
