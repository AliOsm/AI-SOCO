#include <bits/stdc++.h>
using namespace std;
using ll = long long;

map<int,char> mp = {{1,'A'},{3,'B'},{2,'C'},{0,'D'}};

int main()
{
    ios_base::sync_with_stdio(false); cin.tie(0);
    int x; cin >> x;
    int rem = x%4;
    vector<pair<int,char>> a = {{0,mp[x%4]},
                                {1,mp[(x+1)%4]},
                                {2,mp[(x+2)%4]}};
    sort(a.begin(),a.end(),[](auto a, auto b) {
            return a.second < b.second;
            });
    cout << a[0].first << ' ' << a[0].second << '\n';
}

