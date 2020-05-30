#include<bits/stdc++.h>
using namespace std;
int gcd(int a,int b) {return b ? gcd(b,a%b) : abs(a);}
int x[1005], y[1005], n, tot;
long long ans;
map<pair<int,int>,int> m;
int main()
{
    cin >> n;
    for (int i = 0; i < n; ++i) {
        cin >> x[i] >> y[i];
        vector<pair<int,int>> v;
        for (int j = 0; j < i; ++j) {
            int a = x[i] - x[j], b = y[i] - y[j];
            int g = gcd(a,b);
            a /= g, b /= g;
            if (a < 0 || (a == 0 && b < 0)) 
                a = -a, b =-b;
            v.emplace_back(a,b);
        }
        sort(begin(v),end(v));
        for (int j = 0, k = 0; j < v.size(); j = k) {
            for (;k < v.size() && v[k] == v[j]; ++k);
            if (k - j == 1) {
                ans += tot++ - m[v[j]]++;
            }
        }
    }
    cout << ans << endl;
}
