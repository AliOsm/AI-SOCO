#include <bits/stdc++.h>
using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(0);
    int tt;
    cin >> tt;
    while (tt--) {
        int n, x;
        string s;
        cin >> n >> x >> s;
        s = " " + s;
        vector<int> c0(n + 1);
        vector<int> c1(n + 1);
        map<int, int> cnt;
        for (int i = 1; i <= n; ++i) {
            c0[i] = c0[i - 1] + (s[i] == '0');
            c1[i] = c1[i - 1] + (s[i] == '1');
            ++cnt[c0[i] - c1[i]];
        }
        if (c0[n] == c1[n]) {
            if (!cnt.count(x)) {
                cout << "0\n";
            } else {
                cout << "-1\n";
            }
        } else {
            int diff = c0[n] - c1[n];
            int res = x == 0;
            for (auto &p : cnt) {
                int num = x - p.first;
                if (num % diff == 0 && num / diff >= 0) {
                    res += p.second;
                }
            }
            cout << res << "\n";
        }
    }
    return 0;
}

