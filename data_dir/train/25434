#include <bits/stdc++.h>

#define ll long long
#define all(x) x.begin(), x.end()
#define f(i, j, k) for (int i = j; i < k; i++)
#define pb(x) push_back(x)
#define F first
#define S second

using namespace std;


const int n_ = 3e5 + 10;
vector<int> adj[n_];
ll mem[n_];
int n, m;

ll dp(int idx){
    if(idx > n)return 0;
    ll &ret = mem[idx];
    if(ret != -1)return ret;

    if((int)adj[idx].size() > 1)ret = 1;
    else ret = 1 + dp(adj[idx][0]);
    return ret;
}
int main() {
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    memset(mem, -1, sizeof mem);
    cin >> n >> m;
    f(i, 0, m){
        int lst; cin >> lst;
        f(i, 0, n - 1){
            int x; cin >> x;
            adj[lst].push_back(x);
            lst = x;
        }
        adj[lst].push_back(n + 2);
    }
    f(i, 0, n_){
        sort(all(adj[i]));
        adj[i].erase(unique(all(adj[i])), adj[i].end());
    }

    ll res = 0;
    f(i, 1, n + 1)res += dp(i);
    cout << res << "\n";
}