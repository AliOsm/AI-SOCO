#include <bits/stdc++.h>
using namespace std;

typedef long long LL;

const int MAXN = (int)1e5;

LL N, K, L;
LL arr[MAXN + 5];

int main(){
	ios_base::sync_with_stdio(0); cin.tie(0); cout.tie(0);
	cin >> N >> K >> L;
	for (int i = 0 ; i < N * K; i++)
		cin >> arr[i];
	sort(arr, arr + N * K);
	int bil = arr[0];
	int idx = lower_bound(arr, arr + N*K, bil + L + 1) - arr;
	idx--;
	if (N > idx + 1) cout << 0 << '\n';
	else {
		int id = 0;
		LL ans = 0;
		for (int i = 0 ; i < N; i++) {
			ans += arr[id];
			int lo = 0;
			int hi = K-1;
			int ans = 0;
			while (lo <= hi) {
				int mid = (lo + hi) / 2;
				int t_id = id + mid;
				if (idx - (t_id + 1) + 1 >= N-i-1) {
					ans = mid;
					lo = mid + 1;
				}
				else hi = mid - 1;
			}
			id += ans + 1;
		} 
		cout << ans << '\n';
	}
	return 0;
}