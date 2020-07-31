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

    int n, k; cin >> n >> k;
    vector<int> v(n);
    unordered_map<int,int> cnt;
    f(i, 0, n)cin >> v[i], cnt[v[i]]++;
    int lo = 1, hi = n, best = 0;
    while(lo <= hi){
        int mid = lo + hi >> 1;
        // mid = how many time I will repeat
        int can = 0;
        for(auto p : cnt)can += p.second / mid;
        if(can >= k){
            best = mid;
            lo = mid + 1;
        }else hi = mid - 1;
    }

    bool first = true;
    for(auto p : cnt){
        int take = p.second / best;
        while(k && take){
            k--, take--;
            if(first)first = false;
            else cout << " ";
            cout << p.first;
        }
    }
    cout << "\n";
}