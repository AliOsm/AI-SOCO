#include <bits/stdc++.h>
using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(0);
    string s;
    int q;
    cin >> s >> q;
    int n = s.size();
    s = " " + s;
    vector<vector<int>> cnt(26, vector<int>(n + 1));
    for (int i = 1; i <= n; ++i) {
        for (int j = 0; j < 26; ++j) {
            cnt[j][i] = cnt[j][i - 1];
        }
        ++cnt[s[i] - 'a'][i];
    }
    while (q--) {
        int l, r;
        cin >> l >> r;
        bool exists = false;
        if (l == r) {
            exists = true;
        } else if (s[l] != s[r]) {
            exists = true;
        } else {
            int unq = 0;
            for (int i = 0; i < 26; ++i) {
                unq += (cnt[i][r] - cnt[i][l - 1] > 0);
            }
            exists = unq >= 3;
        }
        cout << (exists ? "Yes" : "No") << "\n";
    }
    return 0;
}

