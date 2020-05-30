#include <bits/stdc++.h>
using namespace std;

int main() {
    int n, k;
    cin >> n >> k;
    pair<int, int> arr[n];
    for (int i = 0; i < n; ++i)
        cin >> arr[i].first, arr[i].second = i + 1;
    vector<pair<int, int> > res;
    for (int i = 0; i < k; ++i) {
        sort(arr, arr + n);
        if (arr[n - 1].second != arr[0].second
                && arr[n - 1].first != arr[0].first) {
            res.push_back(make_pair(arr[n - 1].second, arr[0].second));
            arr[n - 1].first--, arr[0].first++;
        }
    }
    sort(arr, arr + n);
    cout << arr[n - 1].first - arr[0].first << ' ' << res.size() << '\n';
    for (int i = 0; i < res.size(); ++i)
        cout << res[i].first << ' ' << res[i].second << '\n';
}
