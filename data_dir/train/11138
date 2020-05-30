#include <bits/stdc++.h>

using namespace std;
int main() {
    int n;
    cin >> n;
    long long ans = 0;
    int arr[n];
    for (int i = 0; i < n; ++i)
        cin >> arr[i];
    sort(arr, arr + n, greater<int>());
    for (int i = 0; i + 3 < n; ++i)
        if (arr[i] == arr[i + 1] or arr[i] == 1 + arr[i + 1]) {
            int j = i + 2;
            for (; j + 1 < n && arr[j] - arr[j + 1] && arr[j] - arr[j + 1] - 1; ++j)
                ;
            if (j + 1 < n)
              ans += arr[i + 1] * (long long) arr[j + 1];
            i = j + 1;
        }
    cout << ans;

}
