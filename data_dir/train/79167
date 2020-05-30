#include "bits/stdc++.h"
using namespace std;

typedef long long ll;

const int maxn = 1e5 + 10;
const ll mod = 1e9 + 7;

int n;
char s[maxn], w[maxn];

ll dp[2][2][maxn];

ll f(int x, int y, int i) {
    if(dp[x][y][i] == -1) {
	if(i == n) return dp[x][y][i] = (x && y);
	dp[x][y][i] = 0;

	if(s[i] != '?') {
	    if(w[i] != '?')
		dp[x][y][i] = f(x | (s[i] > w[i]), y | (s[i] < w[i]), i + 1);
	    else
		for(char c = '0'; c <= '9'; ++c)
		    dp[x][y][i] = (dp[x][y][i] + f(x | (s[i] > c), y | (s[i] < c), i + 1)) % mod;
	}
	else {
	    if(w[i] != '?') 
		for(char c = '0'; c <= '9'; ++c)
		    dp[x][y][i] = (dp[x][y][i] + f(x | (c > w[i]), y | (c < w[i]), i + 1)) % mod;
	    else {
		for(char c = '0'; c <= '9'; ++c)
		    for(char d = '0'; d <= '9'; ++d)
			dp[x][y][i] = (dp[x][y][i] + f(x | (c > d), y | (c < d), i + 1)) % mod;
	    }	       
	}
    }
    return dp[x][y][i];
}

ll solve() {
    memset(dp, -1, sizeof(dp));
    return f(0, 0, 0);
}

int main() {
    scanf("%d %s %s", &n, w, s);
    printf("%lld\n", solve());
    return 0;
}
