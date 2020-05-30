/**
SXR0aXAkI0JwbXptI3FhI3Z3I293bCNqY2IjUG0jMCNicG0jVHFkcXZvLyNCcG0jQW10bjBhY2phcWFicXZvLyNNYm16dml0MSNWdyNhdGN1am16I2tpdiNhbXF9bSNQcXUjVnd6I0F0bW14MSNQcWEjaXptI2l0dCNicHF2b2EjUXYjYnBtI3BtaWRtdmEjaXZsI3d2I21pemJwMSNFcHcjcWEjYnBtem0ja2l2I3F2Ym16a21sbSNRdiNQcWEjeHptYW12a20jbXtrbXhiI0lhI3BtI3htenVxYmJtYnBHI1BtI3N2d2VtYnAjRXBpYiMraXh4bWl6bWJwI2J3I1BxYSNrem1pYmN6bWEjSWEsI0ptbnd6bSN3eiNJbmJteiN3eiNKbXBxdmwjYnBtdTEjVnd6I2FwaXR0I2JwbXwja3d1eGlhYSNJY29wYiN3biNwcWEjc3Z3ZXRtbG9tI017a214YiNpYSNQbSNlcXR0bWJwMSNQcWEjYnB6d3ZtI2x3YnAjbXtibXZsI1dkbXojYnBtI3BtaWRtdmEjSXZsI3d2I21pemJwLyNpdmwjUG0jbm1tdG1icCNWdyNuaWJxb2NtI3F2I29jaXpscXZvI0l2bCN4em1hbXpkcXZvI2JwbXUvI053eiNQbSNxYSNicG0jVXdhYiNQcW9wMSNCcG0jQWN4em11bSMrcXYjb3R3enwsMQ==
*/
#include <cstring>
#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <queue>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <cassert>

#define F first
#define S second
#define endl '\n'
#define pb push_back

const long long MOD = 1e9 + 7;
const long long MAXN = 1e6 + 1;
using namespace std;

typedef long long ll;

long long readInt() {
    bool minus1 = false;
    long long result = 0;
    char ch;
    ch = getchar();
    while (true) {
        if (ch == '-') break;
        if (ch >= '0' && ch <= '9') break;
        ch = getchar();
    }
    if (ch == '-') minus1 = true; else result = ch-'0';
    while (true) {
        ch = getchar();
        if (ch < '0' || ch > '9') break;
        result = result*10 + (ch - '0');
    }
    if (minus1)
        return -result;
    else
        return result;
}

const long long ARAL = 1;
const long long LES = 0;

long long dp[2][55][55];

long long kol[2][55][55];



long long cnt[3];

long long c[1111][1111];

struct aaa {
	long long kaida, kol1, kol2;
};

long long binpow (long long a, long long n) {
	if (n == 0)
		return 1;
	if (n % 2 == 1)
		return ((binpow (a, n-1)%MOD) * a) % MOD;
	else {
		long long b = binpow (a, n/2) % MOD;
		return (b * b) % MOD;
	}
}


void build() {
	for (long long i = 0; i <= 1000; i++) 
		c[i][0] = 0;

	for (long long i = 0; i <= 1000; i++) 
		c[0][i] = 1;

	for (long long i = 1; i <= 1000; i++) 
		for (long long j = 1; j <= 1000; j++) {
			c[i][j] = (c[i - 1][j - 1] + c[i][j - 1]) % MOD;
		}

}
long long cnk(long long k, long long n) {
	return c[k][n];
}
int main() {
	#ifdef IZI_KATKA
	assert(freopen("input", "r", stdin));
    assert(freopen("output", "w", stdout));
    #endif
    long long n = readInt(), k = readInt();
	for (long long i = 1; i <= n; i++) {
		cnt[readInt() / 50]++;
	}
	build();    
	for (long long i = 0; i <= cnt[1]; i++) {
		for (long long j = 0; j <= cnt[2]; j++) {
			dp[LES][i][j] = 1e9;
			kol[LES][i][j] = 0;
			dp[ARAL][i][j] = 1e9;
			kol[ARAL][i][j] = 0;
		}
	}
	dp[LES][cnt[1]][cnt[2]] = 0;
	kol[LES][cnt[1]][cnt[2]] = 1;
	queue <aaa> q;
	aaa naw;
	naw.kaida = LES;
	naw.kol1 = cnt[1];
	naw.kol2 = cnt[2];
	q.push(naw);
	while(!q.empty()) {
		aaa tmp = q.front();
		q.pop();
		for (long long i = 0; i <= (tmp.kaida == LES ? tmp.kol1 : cnt[1] - tmp.kol1); i++) {
			for (long long j = 0; j <= (tmp.kaida == LES ? tmp.kol2 : cnt[2] - tmp.kol2); j++) {
				if (i*50+j*100 > 0 && i * 50 + j * 100 <= k) {
					aaa kuda;
					kuda.kaida = (tmp.kaida^1);
					if (tmp.kaida == LES) {
						kuda.kol1 = tmp.kol1 - i;
						kuda.kol2 = tmp.kol2 - j;
					}
					else {
						kuda.kol1 = tmp.kol1 + i;
						kuda.kol2 = tmp.kol2 + j;
					}					
					if (dp[kuda.kaida][kuda.kol1][kuda.kol2] > 1 + dp[tmp.kaida][tmp.kol1][tmp.kol2]) {
						dp[kuda.kaida][kuda.kol1][kuda.kol2] = 1 + dp[tmp.kaida][tmp.kol1][tmp.kol2];
						kol[kuda.kaida][kuda.kol1][kuda.kol2] = kol[tmp.kaida][tmp.kol1][tmp.kol2] * cnk(i, (tmp.kaida == LES ? tmp.kol1 : cnt[1] - tmp.kol1)) * cnk(j, (tmp.kaida == LES ? tmp.kol2 : cnt[2] - tmp.kol2));
						kol[kuda.kaida][kuda.kol1][kuda.kol2] %= MOD;
						q.push(kuda); 
					} else if (dp[kuda.kaida][kuda.kol1][kuda.kol2] == 1 + dp[tmp.kaida][tmp.kol1][tmp.kol2]) {
						kol[kuda.kaida][kuda.kol1][kuda.kol2] += kol[tmp.kaida][tmp.kol1][tmp.kol2] * cnk(i, (tmp.kaida == LES ? tmp.kol1 : cnt[1] - tmp.kol1)) * cnk(j, (tmp.kaida == LES ? tmp.kol2 : cnt[2] - tmp.kol2)); 
						kol[kuda.kaida][kuda.kol1][kuda.kol2] %= MOD;						
					}
				}
			}
		}		
	}
	if (dp[ARAL][0][0] == 1e9) {
		cout << "-1\n0";
		return 0;
	}
	cout << dp[ARAL][0][0] << endl;
	cout << kol[ARAL][0][0] << endl;    
    return 0;
}
