#include <iostream>

using namespace std;

int z(int x) {
    int ans = 0;
    for (int i = 5; i <= x; i *= 5) {
        ans += x / i;
    }

    return ans;
}

int main() {
    int m;
    cin >> m;
    if (m == 0) {
        cout << "4\n";
        cout << "1 2 3 4";
    } else {
        int lo = 4;
        int hi = 1000000;
        while (lo + 1 < hi) {
            int mid = lo + (hi - lo) / 2;
            int zeroes = z(mid);
            if (zeroes < m) {
                lo = mid;
            } else {
                hi = mid;
            }
        }

        if (z(hi) != m) {
            cout << "0\n";
        } else {
            int end = hi + 1;
            while (z(end) == m) {
                ++end;
            }

            cout << (end - hi) << '\n';
            cout << hi;
            for (int i = hi + 1; i < end; ++i) {
                cout << ' ' << i;
            }
            cout << '\n';
        }
    }
    return 0;
}
