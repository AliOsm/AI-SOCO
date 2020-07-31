#include <bits/stdc++.h>

using namespace std;

int n, m;
int a[15], b[15];
int frek[15];

int main(){
	cin >> n >> m;
	for (int i = 0 ; i < n ; i++) {
		cin >> a[i];
		frek[a[i]]++;
	}
	sort(a, a+n);
	for (int i = 0 ; i < m ; i++) {
		cin >> b[i];
		frek[b[i]]++;
	}
	sort(b, b+m);
	for (int i = 1; i <= 9 ; i++) {
		if (frek[i] >= 2) {
			cout << i << '\n';
			return 0;
		}
	}
	cout << min(a[0], b[0]) << max(b[0],a[0]) << '\n';
	return 0;
}