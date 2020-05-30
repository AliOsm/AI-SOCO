#include <bits/stdc++.h>
#define f(i, j, n) for(int i = j; i < n; i++)
#define all(v) v.begin(), v.end()
#define ll long long
using namespace std;



int main(){
    ios_base::sync_with_stdio(0); cin.tie(0);
    int n; cin >> n;
    unordered_map<ll,int> mp;
    vector<ll> bad;
    vector<ll> v;
    f(i, 0, n){
        ll x; cin >> x;
        v.push_back(x);
        ll sqrt_ = sqrt(x);
        while(sqrt_ * sqrt_ < x) sqrt_++;
        while (sqrt_ * sqrt_ > x) sqrt_--;
        if(sqrt_ * sqrt_ == x){
            ll sqrt__ = sqrt(sqrt_);
            while(sqrt__ * sqrt__ < sqrt_) sqrt__++;
            while (sqrt__ * sqrt__ > sqrt_) sqrt__--;
            if(sqrt__ * sqrt__ == sqrt_){
                mp[sqrt__] += 4;
            }else{
                mp[sqrt_] += 2;
            }
        }else{
            ll cbrt_ = cbrt(x);
            while(cbrt_ * cbrt_ * cbrt_ < x)cbrt_++;
            while (cbrt_ * cbrt_ * cbrt_ > x)cbrt_--;
            if(cbrt_ * cbrt_ * cbrt_ == x){
                mp[cbrt_] += 3;
            }else{
                bad.push_back(x);
            }
        }
    }
    vector<ll> possible_divs;
    for(auto v : mp)possible_divs.push_back(v.first);

    int sz = (int)bad.size();
    f(i, 0, n)f(j, i + 1, n){
        ll g = __gcd(v[i], v[j]);
        if(g != 1 && (g < v[i] || g < v[j])){
            possible_divs.push_back(g);
            if(v[i] / g != 1)possible_divs.push_back(v[i] / g);
            if(v[j] / g != 1)possible_divs.push_back(v[j] / g);
        }
    }
    sort(all(possible_divs));
    possible_divs.erase(unique(all(possible_divs)), possible_divs.end());
    ll res2 = 1;
    unordered_map<ll,int> mp2;
    f(i, 0, sz){
        ll was = bad[i];
        f(j, 0, (int)possible_divs.size()){
            while((bad[i] % possible_divs[j]) == 0){
                mp[possible_divs[j]]++;
                bad[i] /= possible_divs[j];
            }
        }
        if(was == bad[i])mp2[bad[i]]++;
        else if(bad[i] != 1)res2 = res2 * 2 % 998244353;
    }
    for(auto it : mp2){
        res2 = res2 * (it.second + 1) % 998244353;
        res2 = res2 * (it.second + 1) % 998244353;
    }
    ll res = 1;
    for(auto it : mp){
        res = res * (it.second + 1) % 998244353;
    }
    cout << res * res2 % 998244353 << "\n";
}