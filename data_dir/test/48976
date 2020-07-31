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
    int n; cin >> n;
    int sum = 0;
    int aux;
    for(int i = 0; i < n; i++) {
        cin >> aux;
        sum += aux;
    }
    //if( == 1) { cout << 3 << endl; return 0; }
    int cont = 0;
    for(int i = sum + 1; i <= sum + 5; i++) { 
        if(i % (n+1) != 1) cont++;
    }
    cout << cont << endl;

    return 0;
}

