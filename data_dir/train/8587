#include <bits/stdc++.h>
using namespace std;

#define N 100010
int n;
char s[N];
int cnt[2], S[N];

map <int, int> mp;

int main() {
	while (scanf("%d", &n) != EOF) {
		scanf("%s", s + 1);
		for (int i = 1; i <= n; ++i) S[i] = 0;
		cnt[0] = cnt[1] = 0;
		int res[2] = {0, 0};
		for (int i = 1; i <= n; ++i) {
			++cnt[s[i] - '0'];
			if (s[i] == '1') {
				--S[i];
			} else {
				++S[i];
			}
			S[i] += S[i - 1];
		}
		res[1] = min(cnt[0], cnt[1]) * 2;
		mp.clear();
		mp[0] = 0;
		for (int i = 1; i <= n; ++i) {
			if (mp.find(S[i]) != mp.end()) {
				res[0] = max(res[0], i - mp[S[i]]);
			} else {
				mp[S[i]] = i;
			}
		}
		printf("%d\n", res[0]);
	}
	return 0;
}
