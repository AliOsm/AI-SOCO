#include<bits/stdc++.h>
using namespace std;
#define SZ(a) ((int)(a).size())
const int N = 200000 + 87;
int cnt[N], a[N];
bool ov[N], ok[N];
int main()
{
	ios::sync_with_stdio(0);
	cin.tie(0);
	int n;
	cin >> n;
	for (int i = 0; i < n; ++i) {
		cin >> a[i];
		++cnt[a[i]];
	}
	queue<int> q;
	for (int i = 1; i <= n; ++i)
		if (!cnt[i])
			q.push(i);
		else
			ov[i] = cnt[i] > 1;
	cout << SZ(q) << endl;
	for (int i = 0; i < n && SZ(q); ++i)
		if (ov[a[i]]) {
			if (--cnt[a[i]] == 0 && !ok[a[i]])
				continue;
			if (ok[a[i]] || q.front() < a[i]) {
				a[i] = q.front();
				q.pop();
			} else {
				ok[a[i]] = 1;
			}
		}
	for (int i = 0; i < n; ++i)
		cout << a[i] << " \n"[i==n-1];
}
