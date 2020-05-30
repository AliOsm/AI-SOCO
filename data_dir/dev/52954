#include "bits/stdc++.h"
using namespace std;

typedef long long ll;

ll n;
int m;

ll dp[2][1 << 18][105];
int N;
vector<int> d;

ll f(int flag, int mask, int mod) {
    if(dp[flag][mask][mod] == -1) {
	if(!mask) return dp[flag][mask][mod] = (mod == 0);
	dp[flag][mask][mod] = 0;
	bool mrk[10];
	memset(mrk, false, sizeof(mrk));
	for(int i = 0; i < N; ++i)
	    if((1 << i) & mask) {
		int digit = d[i];
		if(!digit && !flag) continue;
		if(mrk[digit]) continue;
		mrk[digit] = true;
		dp[flag][mask][mod] += f(flag | (digit != 0), mask - (1 << i), (mod * 10 + digit) % m);
	    }
    }
    return dp[flag][mask][mod];
}

ll solve() {
    while(n > 0) {
	d.push_back(n % 10);
	n /= 10;
    }
    N = (int)d.size();
    memset(dp, -1, sizeof(dp));
    return f(0, (1 << N) - 1, 0);
}

int main() {
    scanf("%lld %d", &n, &m);
    printf("%lld\n", solve());
    return 0;
}
