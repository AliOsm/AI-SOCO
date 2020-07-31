#include <iostream>
#include <cstdio>
#include <cmath>
#include <string>
#include <algorithm>
#include <vector>
#include <queue>
#include <deque>
#include <map>
#include <set>
#include <ctime>
#include <memory.h>
#include <assert.h>
#include <complex>
#include <ctime>  
#include <cstdlib>
using namespace std;

#pragma comment(linker, "/STACK:100000000")

#define mp make_pair
#define pb push_back
#define sz(x) (int)(x).size()
#define ll long long
#define ull unsigned long long

int n, m;

string s;
int col[505];

int dp[2][505][505];

int main() {
    //freopen("input.txt", "rt", stdin);
    //freopen("seq.in", "rt", stdin);
    //freopen("seq.out", "wt", stdout);

	int mod;
	scanf("%d %d %d", &n, &m, &mod);
	for(int i = 0; i < m; i++) {
		cin >> s;
		for(int j = 0; j < n; j++) {
			if(s[j] == '1') col[j]++;
		}

	}
	int p0 = 0, p1 = 0;
	for(int i = 0; i < n; i++) {
		if(col[i] == 0) p0++;
		else if(col[i] == 1) p1++;
	}

	dp[0][p0][p1] = 1; 
	for(int step = m; step < n; step++) {
		for(int i = 0; i <= n; i++) {
			int maxj = n - i + 1;
			for(int j = 0; j < maxj; j++) {
				if(dp[0][i][j] == 0) continue;
				// что
				if(i > 1) {

					ll val = (ll)dp[0][i][j] * (ll)i * (ll)(i-1LL) / 2LL;
					val %= (ll)mod;
					dp[1][i-2][j+2] += val;
					dp[1][i-2][j+2] %= mod;
				}
				if(j > 1) {
					ll val = (ll)dp[0][i][j] * (ll)j * (ll)(j-1LL) / 2LL;
					val %= (ll)mod;
					dp[1][i][j-2] += val;
					dp[1][i][j-2] %= mod;
				}
				if(i > 0 && j > 0) {
					ll val = (ll)dp[0][i][j] * (ll)i * (ll)j;
					val %= (ll)mod;
					dp[1][i-1][j] += val;
					dp[1][i-1][j] %= mod;
				}

			}
		}

		for(int i = 0; i < 505; i++) {
			for(int j = 0; j < 505; j++) {
				dp[0][i][j] = dp[1][i][j];
				dp[1][i][j] = 0;
			}
		}

	}
	cout <<  dp[0][0][0] << endl;
	
    return 0;
}