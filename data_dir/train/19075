#include<bits/stdc++.h>

#define f(i, j, k) for(int i = j; i < k; i++)
#define all(x) x.begin(), x.end()
#define ll long long
using namespace std;

pair<int, pair<int, int> > parent[500][5001];

int main() {

    ios_base::sync_with_stdio(0);
    cin.tie(0);
    int tc;
    cin >> tc;
    while (tc--) {
        ll n, m, t;
        cin >> n >> m >> t;
        vector<ll> v(n), sorted;
        f(i, 0, n){
            cin >> v[i];
            if(v[i] <= t)sorted.push_back(v[i]);
        }

        if(sorted.size() == 0){
            cout << 0 << " " << t << "\n";
            continue;
        }

        sort(all(sorted));
        int lo = 0, hi = (int) sorted.size() - 1, best = -1;

        while (lo <= hi) {
            int mid = lo + hi >> 1;

            ll d = sorted[mid];
            ll so_far = 0, last_made = 0, cnt = 0, all_done = 0;
            f(i, 0, n) {
                if (v[i] <= d) {
                    last_made += v[i];
                    if (v[i] + so_far > t)break;
                    cnt++;
                    all_done++;
                    so_far += v[i];
                    if (cnt == m) {
                        cnt = 0;
                        so_far += last_made;
                        last_made = 0;
                    }
                }
            }
            f(i, 0, n)all_done -= v[i] <= d;
            if (!all_done) {
                best = mid;
                lo = mid + 1;
            } else hi = mid - 1;
        }
        if (best == -1) {
            ll d = sorted[0];
            ll so_far = 0, last_made = 0, cnt = 0, all_done = 0;
            f(i, 0, n) {
                if (v[i] <= d) {
                    last_made += v[i];
                    if (v[i] + so_far > t)break;
                    cnt++;
                    all_done++;
                    so_far += v[i];
                    if (cnt == m) {
                        cnt = 0;
                        so_far += last_made;
                        last_made = 0;
                    }
                }
            }

            cout << all_done << " " << d << "\n";
        } else {
            int cnt = 0;
            f(i, 0, n)cnt += v[i] <= sorted[best];
//            cerr << sorted[best] << "\n";
            if (best == (int) sorted.size() - 1) {
                cout << cnt << " " << sorted[best] << "\n";
            }else {
                ll d = sorted[best + 1];
                ll so_far = 0, last_made = 0, cnt__ = 0, all_done = 0;
                f(i, 0, n) {
                    if (v[i] <= d) {
                        last_made += v[i];
                        if (v[i] + so_far > t)break;
                        cnt__++;
                        all_done++;
                        so_far += v[i];
                        if (cnt__ == m) {
                            cnt__ = 0;
                            so_far += last_made;
                            last_made = 0;
                        }
                    }
                }
                if(all_done > cnt){
                    cout << all_done << " " << sorted[best + 1] << "\n";
                }else{
                    cout << cnt << " " << sorted[best] << "\n";
                }
            }
        }

    }
}