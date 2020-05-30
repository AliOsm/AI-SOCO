#include <iostream>
#include <vector>
#include <utility>
#include <algorithm>

using namespace std;

int main() {
    int n, k;
    cin >> n >> k;
    vector<pair<int, int>> a(n);
    for (int i = 0; i < n; ++i) {
        cin >> a[i].first;
        a[i].second = i + 1;
    }

    if (n == 1) {
        cout << "0 0\n";
        return 0;
    }

    sort(begin(a), end(a));
    vector<pair<int, int>> moves;
    int ans = 1e9;
    while (k-- > 0) {
        int cur_state = a.back().first - a[0].first;
        ans = min(ans, cur_state);

        moves.emplace_back(a.back().second, a[0].second);
        a[0].first++;
        a.back().first--;
        sort(begin(a), end(a));
    }

    ans = min(ans, a.back().first - a[0].first);

    while (!moves.empty() and a.back().first - a[0].first != ans) {
        int u = moves.back().first;
        int v = moves.back().second;

        for (int i = 0; i < n; ++i) {
            if (a[i].second == u)
                ++a[i].first;
            else if(a[i].second == v)
                --a[i].first;
        }

        moves.pop_back();
        sort(begin(a), end(a));
    }

    cout << (a.back().first - a[0].first) << " " << moves.size() << '\n'; 
    for (auto& p : moves) {
        cout << p.first << " " << p.second << '\n';
    }

    return 0;
}
