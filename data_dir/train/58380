#include<bits/stdc++.h>
#define f(i, j, k) for(int i = j; i < k; i++)
#define ll long long
using namespace std;


int main() {

    int n;
    ll k;
    cin >> n >> k;
    vector<ll> v(n), rem(n);
    f(i, 0, n){
        cin >> v[i];
        rem[i] = v[i] % k;
    }

    ll res = 0;
    ll must = 0;
    f(i, 0, n){
        res += (v[i] + must) / k;
        ll left = (v[i] + must) % k;
        if(left > v[i])res++, left = 0;
        must = left;
    }
    cout << res + (must ? 1 : 0) << "\n";
}