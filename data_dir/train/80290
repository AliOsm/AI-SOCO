#include <iostream>
#include <iomanip>
#include <string>
#include <sstream>
#include <fstream>
#include <cassert>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <algorithm>
#include <utility>
#include <vector>
#include <queue>
#include <map>
#include <set>
#include <unordered_map>
#include <unordered_set>
#include <bitset>
#include <complex>

using namespace std;
using ll = long long;
using pii = pair<int, int>;

int dx[] = {1, 0, -1, 0};
int dy[] = {0, -1, 0, 1};

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(0); cout.tie(0);

    int q;
    cin >> q;
    while (q-- > 0) {
        int b, w;
        cin >> b >> w;

        int r = 2;
        int c = 2;
        if (b > w)
            --c;

        vector<pair<int, int>> blacks, whites;
        while (true) {
            int color = (r + c) % 2;
            if (blacks.size() < b and color) {
                blacks.emplace_back(r, c);
            } else if (whites.size() < w and !color) {
                whites.emplace_back(r, c);
            } else {
                break;
            }

            ++c;
        }

        while (blacks.size() < b) {
            for (auto& p : whites) {
                if (blacks.size() >= b) break;

                int r = p.first;
                int c = p.second;

                blacks.emplace_back(r - 1, c);
                if (blacks.size() < b) {
                    blacks.emplace_back(r + 1, c);
                }
            }
        }

        while (whites.size() < w) {
            for (auto& p : blacks) {
                if (whites.size() >= w) break;

                int r = p.first;
                int c = p.second;

                whites.emplace_back(r - 1, c);
                if (whites.size() < w) {
                    whites.emplace_back(r + 1, c);
                }
            }
        }

        set<pair<int, int>> s;
        for (auto& p : blacks) {
            s.insert(p);
        }
        for (auto& p : whites) {
            s.insert(p);
        }
        if (blacks.size() != b or whites.size() != w or s.size() != (b + w)) {
            cout << "NO\n";
            continue;
        }

        cout << "YES\n";
        for (auto& p : blacks) {
            cout << p.first << ' ' << p.second /*<<  " B " */ << '\n';
        }
        for (auto& p : whites) {
            cout << p.first << ' ' << p.second /*<<  " W " */ << '\n';
        }
    }

    return 0;
}
