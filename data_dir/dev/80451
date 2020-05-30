#include <iostream>
#include <iomanip>
#include <cstring>
#include <cmath>
#include <algorithm>
#include <utility>
#include <vector>

using namespace std;

bool cmp(pair<int, int> i1, pair<int, int> i2) {
    if (i1.first != i2.first) {
        return i1.first < i2.first;
    } else {
        return i1.second < i2.second;
    }
}

int a[100005];

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(0);

    int n, m;
    cin >> n >> m;

    int l, r;
    vector<pair<int, int> > intervals;
    int mex = 1e9;
    for (int i = 0; i < m; ++i) {
        cin >> l >> r;
        --l; --r;

        if (r - l + 1 < mex) {
            mex = r - l + 1;
        }

        intervals.push_back(make_pair(l, r));
    }

    sort(intervals.begin(), intervals.end(), cmp);

    int num_intervals = intervals.size();
    int iptr = 0;
    int x = 0;

    memset(a, -1, sizeof(a));
    for (int i = 0; iptr < num_intervals and i < n; ++i) {
        l = intervals[iptr].first;
        r = l + mex - 1;

        //cout << i << ' ' << intervals[iptr].first << ' ' << intervals[iptr].second << '\n';
        if (i < l) continue;
        while (iptr < num_intervals - 1 and i > r) {
            ++iptr;
            l = intervals[iptr].first;
            r = l + mex - 1;
        }

        if (i > r) break;

        if (l <= i and i <= r) {
            a[i] = x;
            x = (x + 1) % mex;
        }
    }

    cout << mex << '\n';
    cout << max(0, a[0]);
    for (int i = 1; i < n; ++i) {
        cout << ' ' << max(0, a[i]);
    }
    cout << '\n';

    return 0;
}
