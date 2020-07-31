#include <bits/stdc++.h>

typedef long long ll;

using namespace std;

int main() {
    ios_base::sync_with_stdio(0); cin.tie(0);
    int n ;
    cin >> n;
    vector<ll>v(n << 1);
    unordered_map<ll,int> mp;
    for(int i = 0; i < 2 * n; i++) {
        cin >> v[i];
        mp[v[i]]++;
        if(mp[v[i]] == n) {
            cout << "0\n";
            return 0;
        }
    }

    sort(v.begin(), v.end());

    if(n == 1) {
        cout << 0 << "\n";
        return 0;
    }

    ll best = (v[n - 1] - v[0]) * (v[v.size() - 1] - v[n]);

    for(int i = 1; i < n; i++) {
        ll here = (v[i + n - 1] - v[i]) * (v[v.size() - 1] - v[0]);
        best = min(best, here);
    }
    cout << best << "\n";
}