#include <bits/stdc++.h>
using namespace std;

int main() {

    long long n, l, x, y;
    cin >> n >> l >> x >> y;
    long long arr[n];
    for (long long i = 0; i < n; ++i)
        cin >> arr[i];
    set<long long> stx, sty;
    bool bx = 0, by = 0;
    for (int i = 0; i < n; ++i) {
        bx |= binary_search(arr, arr + n, arr[i] - x)
                or binary_search(arr, arr + n, arr[i] + x);
        if (!bx) {
            if (arr[i] - x > 0)
                stx.insert(arr[i] - x);
            if (arr[i] + x < l)
                stx.insert(arr[i] + x);
        }
        by |= binary_search(arr, arr + n, arr[i] - y)
                or binary_search(arr, arr + n, arr[i] + y);
        if (!by) {
            if (arr[i] - y > 0)
                sty.insert(arr[i] - y);
            if (arr[i] + y < l)
                sty.insert(arr[i] + y);
        }
    }
    if (bx && by)
        cout << 0;
    else if (by)
        cout << 1 << '\n' << *stx.begin();
    else if (bx)
        cout << 1 << '\n' << *sty.begin();
    else {
        vector<long long> v(12345);
        v[0] = -1;
        set_intersection(stx.begin(), stx.end(), sty.begin(), sty.end(),
                v.begin());
        if (v[0] == -1)
            cout << 2 << '\n' << x << ' ' << y;
        else
            cout << 1 << '\n' << v[0];
    }
}
