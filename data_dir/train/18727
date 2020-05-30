#include <bits/stdc++.h>
using namespace std;

#define pb push_back
#define mp make_pair
#define fi first
#define se second

typedef long long ll;
const int INF = 0x3f3f3f3f;

bool isdiff(int x) {
    int row[10];
    memset(row, 0, sizeof row);
    while(x > 0) {
        int aux = x % 10;
        row[aux]++;
        x /= 10;
    }
    for(int i = 0; i < 10; i++) 
        if(row[i] > 1) return false;
    return true;
}

int main() {
    ios::sync_with_stdio(false);
    int n; cin >> n;
    while(!isdiff(++n)) continue;
    cout << n << endl;

    return 0;
}

