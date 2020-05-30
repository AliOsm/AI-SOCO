#include<bits/stdc++.h>
#define FOR(i,s,n) for (int i = s; i < n; i++)
#define FAST ios_base::sync_with_stdio(0); cin.tie(0);
using namespace std;

typedef long long ll;


string s;

int simulate (vector<pair<char,int> > v) {
    if (v.size() <= 1) return 0;

    int sz = v.size();
    vector<pair<char,int> > v2;

    FOR(i, 0, sz) {
        pair<char,int> p = {-1, -1};
        if (i == 0 || i == v.size() - 1) {
            if (v[i].second != 1) p = {v[i].first, v[i].second - 1};
        } else {
            if (v[i].second > 2) p = {v[i].first, v[i].second - 2};
        }
        if (p.first != -1) {
            if (v2.empty() || v2[v2.size() - 1].first != p.first)
                v2.push_back(p);
            else v2[v2.size() - 1].second += p.second;
        }
    }
    return 1 + simulate(v2);
}

int main() {
    FAST

    cin >> s;

    vector<pair<char,int> > v;
    for (int i = 0; i < s.length();) {
        int j = i;
        while(j + 1 < s.length() && s[j + 1] == s[j]) j++;
        v.push_back({s[i], j - i + 1});
        i = j + 1;
    }

    cout << simulate (v) << "\n";
    return 0;
}