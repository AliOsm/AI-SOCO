#include <bits/stdc++.h>
using namespace std;

#define pb push_back
#define mp make_pair
#define fi first
#define se second

typedef long long ll;
const int INF = 0x3f3f3f3f;

int main() {
    ios::sync_with_stdio(false);
    ll n, m;
    cin >> n >> m;
    ll mini = max(0LL, n - m*2);
    cout << mini << " ";
    ll maxi = 3;
    if(m == 0) maxi = 0;
    else if(m <= 2) maxi = m + 1; 
    else if(m == 3) maxi = m;
    else { 
        ll tmp = 3;
        ll cont = 2;
        while(tmp < m) {
            tmp++;
            tmp += cont;
            cont++;
            maxi++;
        }
    }
    cout << max(0LL, n - maxi) << endl;

    return 0;
}

