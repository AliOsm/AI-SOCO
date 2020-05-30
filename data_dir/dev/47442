#include <bits/stdc++.h>

using namespace std;

int n;

int arr[5005];

int main(){
	ios_base::sync_with_stdio(0); cin.tie(0); cout.tie(0);
	cin >> n;
	for (int i = 0 ; i < n ; i++)
		cin >> arr[i];
	sort(arr, arr+n);
	int i = 0;
	int maks = -1;
	int ans = 0;
	while (i < n) {
		ans = 1;
		int j = i + 1;
		while (j < n && arr[j] == arr[i]) {
			ans++;
			j++;
		}
		maks = max(maks, ans);
		i = j;
	}
	cout << maks << '\n';
	return 0;
}