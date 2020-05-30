#include <bits/stdc++.h>

using namespace std;

const int N = 1e5 + 5;

map<int, int> mp;

int arr[N];

void order() {
    int curr = 1;
    for (auto &p : mp) {
        p.second = curr++;
    }
}

vector <vector<int>> res;
bool vis[N];

int main() {
#ifdef Local
    freopen("test.in", "r", stdin);
#else
#define endl '\n'
#endif

    int n;
    cin >> n;

    for (int i = 1; i <= n; ++i) {
        cin >> arr[i];
        mp[arr[i]];
    }

    order();

    for (int i = 1 ; i <= n ; ++i) {
        if (vis[i]) continue;
        int curr = i;
        vector <int> v;
        while (!vis[curr]) {
            vis[curr] = true;
            v.push_back(curr);
            curr = mp[arr[curr]];
        }
        res.push_back(v);
    }

    cout << res.size() << endl;

    for (auto& v : res) {
        cout << v.size() << ' ';
        for (int x : v) {
            cout << x << ' ';
        }
        cout << '\n';
    }


    return 0;
}