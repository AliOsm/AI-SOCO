#include <bits/stdc++.h>
using namespace std;
typedef long long ll;

const ll mod = 998244353;

ll power(ll a, ll b) {
    if (b <= 0) return 1;
    ll temp = power(a, b / 2) % mod;
    if (b % 2 == 0) {
        return (temp * temp) % mod;
    }
    else {
        return (((a * temp) % mod) * temp) % mod;
    }
}

int arr[1002][1002];
ll expected[1002][1002] = {0};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(0);
    cout.tie(0);
    int n, m;
    cin >> n >> m;
    map<int, vector<pair<int, int> > > sorted;
    for(int i = 1; i <= n; ++i) {
        for(int j = 1; j <= m; ++j) {
            cin >> arr[i][j];
            sorted[arr[i][j]].push_back({i,j});
        }
    }
    int row, col;
    cin >> row >> col;
    int i, j;
    ll sumI = 0, sumJ = 0, sumI2 = 0, sumJ2 = 0;
    int cnt = 0;
    ll sumExpected = 0;
    for(auto &elem : sorted) {
        ll cntInv = power(cnt, mod-2);
        for(auto &p : elem.second) {
            i = p.first;
            j = p.second;
            ll currExpected = 0;
            currExpected += 1LL*cnt*i*i;
            currExpected -= 2LL*i*sumI;
            currExpected += sumI2;
            
            currExpected += 1LL*cnt*j*j;
            currExpected -= 2LL*j*sumJ;
            currExpected += sumJ2;
            currExpected %= mod;
            currExpected += mod;
            currExpected %= mod;
            
            currExpected += sumExpected;
            currExpected %= mod;
            
            currExpected *= cntInv;
            currExpected %= mod;
            
            expected[i][j] = currExpected;

            //sumExpected += currExpected;
            //sumExpected %= mod;
        }

        //sumExpected *= power(cnt, mod-2);
        //sumExpected %= mod;

        for(auto &p : elem.second) {
            i = p.first;
            j = p.second;
            sumI += i;
            sumJ += j;
            sumI2 += 1LL*i*i;
            sumJ2 += 1LL*j*j;
            sumExpected += expected[i][j];
            
            sumI %= mod;
            sumJ %= mod;
            sumI2 %= mod;
            sumJ2 %= mod;
            sumExpected %= mod;
            cnt++;
        }
    }
    
    cout << expected[row][col] << '\n';
    return 0;
}









































