#include "bits/stdc++.h"
using namespace std;

typedef long long ll;

ll n, k;

bool solve() {
    set<ll> S;
    for(ll i = 1; i <= k; ++i) {
	if(S.find(n % i) != S.end()) return false;
	S.insert(n % i);
    }
    return true;
}

int main() {
    scanf("%lld %lld", &n, &k);
    if(solve()) printf("Yes\n");
    else printf("No\n");
    return 0;
}
