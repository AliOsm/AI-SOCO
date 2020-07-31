#include <cstdio>
#include <unordered_map>
using namespace std;
typedef long long ll;
int main()
{
	unordered_map<int, int> cnt;
	int n;
	ll ans = 0;
	scanf("%d", &n);
	for (int i = 0; i < n; ++i) {
		int a;
		scanf("%d", &a);
		for (ll j = 2; j <= 2e9; j <<= 1)
			if (cnt.count(j - a))
				ans += cnt[j - a];
		++cnt[a];
	}
	printf("%lld\n", ans);
}
