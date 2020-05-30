#include <bits/stdc++.h>
using namespace std;

void test_case() {
    int n;
    cin >> n;
    vector<pair<int, int>> pts(n);
    int max_x = 0;
    for (int i = 0; i < n; ++i) {
        cin >> pts[i].first >> pts[i].second;
        max_x = max(max_x, pts[i].first);
    }
    vector<vector<int>> y(max_x + 1);
    for (auto &pt : pts) {
        y[pt.first].emplace_back(pt.second);
    }
    for (auto &v : y) {
        sort(v.begin(), v.end());
    }
    bool bad = false;
    auto simulate = [&](bool print) {
        int cy = 0;
        for (int i = 0; i <= max_x; ++i) {
            if (y[i].size()) {
                if (y[i].front() < cy) {
                    bad = true;
                    return;
                }
                for (auto &_y : y[i]) {
                    if (print) {
                        while (cy != _y) {
                            cout << "U";
                            ++cy;
                        }
                    } else {
                        cy = _y;
                    }
                }
            }
            if (i != max_x && print) {
                cout << "R";
            }
        }
        if (print) {
            cout << "\n";
        }
    };
    simulate(false);
    if (bad) {
        cout << "NO\n";
    } else {
        cout << "YES\n";
        simulate(true);
    }
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(0);
    int tt;
    cin >> tt;
    while (tt--) {
        test_case();
    }
    return 0;
}

