#include<bits/stdc++.h>
using namespace std;
typedef long long ll;
int main()
{
    ll X,d;
    cin >> X >> d;
    vector<ll> a{1};
    int l=0;
    --X;
    for (; a.size() <= 10000 && X; ) {
        /*
        cerr << "a:";
        for (int x : a)
            cerr << x << ' ';
        cerr << endl;
*/
        ll b = a.back();
        while (l < a.size() && b - a[l] >= d)
            ++l;
        ll w = (1LL<<(a.size()-l));
        while (a.size()-l > 60 || w > X) {
            b = a[l] + d;
            while (l < a.size() && b - a[l] >= d)
                ++l;
            w = (1LL<<(a.size()-l));
        }
        a.push_back(b);
        X -= w;
    }
    if (X) {
        cout << "-1\n";
        return 0;
    }
    cout << a.size() << endl;
    for (int i = 0; i < a.size(); ++i)
        cout << a[i] << " \n"[i+1==a.size()];
}
