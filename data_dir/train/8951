#include <bits/stdc++.h>
using namespace std;

#define pb push_back
#define mk make_pair
#define fi first
#define se second
#define eb emplace_back

typedef long long ll;
typedef pair<int,int> ii;
typedef vector< pair<int,int> > vii;
const int INF = 0x3f3f3f3f;
const int n = 4;
int MOD = 1e9 + 7;
typedef vector< vector<ll> > mat;

mat operator * (const mat &a, const mat &b) {
    mat m(n, vector<ll>(n));
    for(int i = 0; i < n; i++)
        for(int j = 0; j < n; j++)
            for(int k = 0; k < n; k++) {
                m[i][j] += (a[i][k] * b[k][j]) % MOD;
                m[i][j] %= MOD;
            }
    return m;
}

mat id() {
    mat m(n, vector<ll>(n));
    for(int i = 0; i < n; i++) m[i][i] = 1;
    return m;
}

void print(mat m) {
    for(int i = 0; i < n; i++) {
        for(int j = 0; j < n; j++)
            cout << m[i][j] << " ";
        cout << endl;
    }
    cout << endl;
}

ll expo(mat ele, ll e) {
    mat ans = id();

    while(e) {
        if(e & 1) ans = ans * ele;
        ele = ele * ele;
        e >>= 1;
    }

    return ans[0][0];
}

int main() {
    ios::sync_with_stdio(false);
    int p; cin >> p;
    mat m(n, vector<ll>(n,1LL));
    for(int i = 0; i < n; i++) m[i][i] = 0;
    cout << expo(m, p) << endl;
    return 0;
}

