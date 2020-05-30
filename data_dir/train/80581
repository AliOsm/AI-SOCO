#include<bits/stdc++.h>

#define f(i, j, k) for(int i = j; i < k; i++)
#define all(x) x.begin(), x.end()
#define ll long long
using namespace std;


int main() {

    ios_base::sync_with_stdio(0);
    cin.tie(0);

    int n, m; cin >> n >> m;
    vector<bool> hero(n);
    vector<ll> v(n);
    vector<int> pos_num(n);
    f(i, 0, m){
        int s, h;
        cin >> s >> h;
        hero[--s] = 1;
        pos_num[s] = i;
        v[s] = h;
    }
    f(i, 0, n){
        int x; cin >> x;
        if(!hero[i])v[i] = x;
    }

    f(cell, 0, n){
        vector<int>order;
        vector<ll> v_;
        vector<bool> hero_;
        for(bool x : hero)hero_.push_back(x);
        for(long long x : v)v_.push_back(x);

        f(dum, 0, m){
            vector<bool> can(n);
            f(i, 0, n)
                if(hero_[i]){
                    int inc = i <= cell ? 1 : -1;
                    ll sum = 0;
                    int idx = i;
                    bool ok = 1;
                    while(1){
                        if(idx == i || !hero_[idx])
                        sum += v_[idx];
                        if(sum < 0)ok = 0;
                        if(idx == cell)break;
                        idx += inc;
                    }
                    if(ok)can[i] = 1;
                }
            int idx = -1;
            f(i, 0, cell + 1){
                if(can[i]){
                    idx = i;
                    break;
                }
            }
            for(int i = n - 1; i >= cell; i--)
                if(can[i]){
                    idx = i;
                    break;
                }
            if(idx == -1)break;
            int inc = idx <= cell ? 1 : -1;
            order.push_back(pos_num[idx]);
            hero_[idx] = 0;
//            if(cell == 6)cerr << idx << " " << pos_num[idx] << "\n";
            while(1){
                v_[idx] = 0;
                if(idx == cell)break;
                idx += inc;
            }
        }



        if(order.size() == m){
            cout << cell + 1 << "\n";
            f(i, 0, m){
                if(i)cout << " ";
                cout << order[i] + 1;
            }
            cout << "\n";
            return 0;
        }
    }
    cout << -1 << "\n";
}