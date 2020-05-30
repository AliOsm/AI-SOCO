#include <bits/stdc++.h>
using namespace std;
const long long mod = 1000000007;
int main() {
	#ifdef tajir
		freopen("input.txt","r",stdin);
	#endif
	char s[101][101];
	long long n,m;
	scanf("%I64d %I64d",&n,&m);
	for(long long i = 0; i < n; ++i)
		scanf(" %s",s[i]);
	vector<long long> v(26);
	long long ans = 1;
	for(long long i = 0; i < m; ++i) {
		for(long long j = 0; j < 26; ++j)	v[j] = 0;
		long long cnt = 0;
		for(long long j = 0; j < n; ++j) 
			v[s[j][i] - 'A'] = 1ll;
		for(long long j = 0; j < 26; ++j) {
			if(v[j])	cnt++;
		}
		ans %= mod;
		cnt %= mod;
		ans *= cnt;
		ans %= mod;
	}
	printf("%I64d\n", ans);
	return 0;
}