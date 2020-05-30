#include <bits/stdc++.h>

#define ll long long
#define all(x) x.begin(), x.end()
#define f(i, j, k) for (int i = j; i < k; i++)
#define pb(x) push_back(x)
#define F first
#define S second

using namespace std;



int main() {
    ios_base::sync_with_stdio(0);
    cin.tie(0);


    int n; cin >> n;
    ll sum = 0;
    vector<ll> v(n);
    unordered_map<ll,ll> cnt;
    f(i, 0, n)cin >> v[i], sum += v[i], cnt[v[i]]++;
    vector<int> res;
    f(i, 0, n){
        cnt[v[i]]--;
        if((sum - v[i]) % 2ll == 0 && cnt[(sum - v[i]) / 2])res.push_back(i);
        cnt[v[i]]++;
    }
    cout << (int)res.size() << "\n";
    f(i, 0, (int)res.size()){
        if(i)cout << " ";
        cout << res[i] + 1;
    }
    cout << "\n";
}