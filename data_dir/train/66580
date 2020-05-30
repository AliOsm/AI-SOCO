#include "bits/stdc++.h"
using namespace std;

typedef long long ll;
const int maxn = 1e5 + 10;
const ll mod = 777777777;

int n, m;
int w[3][3];

int a[maxn];

struct node {
    ll dp[3][3];
    
    inline void merge(node L, node R, int i, int j) {
	int mid = (i + j) >> 1;

	for(int x = 0; x < 3; ++x)
	    for(int y = 0; y < 3; ++y)
		dp[x][y] = 0;
	
	for(int x = 0; x < 3; ++x)
	    for(int y = 0; y < 3; ++y)
		for(int k = 0; k < 3; ++k)
		    for(int q = 0; q < 3; ++q)
			if((!a[mid] || a[mid] == k + 1) && (!a[mid + 1] || a[mid + 1] == q + 1) && w[k][q])
			    dp[x][y] = (dp[x][y] + L.dp[x][k] * R.dp[q][y]) % mod; 
    }
} seg[4 * maxn];

void build(int idx, int i, int j) {
    if(i == j) {
	for(int x = 0; x < 3; ++x) seg[idx].dp[x][x] = 1;
	return;
    }
    int mid = (i + j) >> 1;
    int left = idx << 1;
    int right = left | 1;
    build(left, i, mid);
    build(right, mid + 1, j);
    seg[idx].merge(seg[left], seg[right], i, j);
}

void update(int idx, int i, int j, int pos) {
    if(i == j) {
	for(int x = 0; x < 3; ++x)
	    for(int y = 0; y < 3; ++y)
		seg[idx].dp[x][y] = 0;

	if(!a[i]) for(int x = 0; x < 3; ++x) seg[idx].dp[x][x] = 1;
	else seg[idx].dp[a[i] - 1][a[i] - 1] = 1;

	return;
    }
    int mid = (i + j) >> 1;
    int left = idx << 1;
    int right = left | 1;
    if(pos <= mid) update(left, i, mid, pos);
    else update(right, mid + 1, j, pos);
    seg[idx].merge(seg[left], seg[right], i, j);
}

int main() {
    scanf("%d %d", &n, &m);
    for(int i = 0; i < 3; ++i)
	for(int j = 0; j < 3; ++j)
	    scanf("%d", &w[i][j]);
    build(1, 1, n);
    while(m--) {
	int v, t;
	scanf("%d %d", &v, &t);
	a[v] = t;
	update(1, 1, n, v);
	ll ans = 0;
	for(int x = 0; x < 3; ++x)
	    for(int y = 0; y < 3; ++y)
		ans = (ans + seg[1].dp[x][y]) % mod;
	printf("%lld\n", ans);
    }
    return 0;
}
