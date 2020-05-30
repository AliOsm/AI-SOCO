/**
SXR0aXAkI0JwbXptI3FhI3Z3I293bCNqY2IjUG0jMCNicG0jVHFkcXZvLyNCcG0jQW10bjBhY2phcWFicXZvLyNNYm16dml0MSNWdyNhdGN1am16I2tpdiNhbXF9bSNQcXUjVnd6I0F0bW14MSNQcWEjaXptI2l0dCNicHF2b2EjUXYjYnBtI3BtaWRtdmEjaXZsI3d2I21pemJwMSNFcHcjcWEjYnBtem0ja2l2I3F2Ym16a21sbSNRdiNQcWEjeHptYW12a20jbXtrbXhiI0lhI3BtI3htenVxYmJtYnBHI1BtI3N2d2VtYnAjRXBpYiMraXh4bWl6bWJwI2J3I1BxYSNrem1pYmN6bWEjSWEsI0ptbnd6bSN3eiNJbmJteiN3eiNKbXBxdmwjYnBtdTEjVnd6I2FwaXR0I2JwbXwja3d1eGlhYSNJY29wYiN3biNwcWEjc3Z3ZXRtbG9tI017a214YiNpYSNQbSNlcXR0bWJwMSNQcWEjYnB6d3ZtI2x3YnAjbXtibXZsI1dkbXojYnBtI3BtaWRtdmEjSXZsI3d2I21pemJwLyNpdmwjUG0jbm1tdG1icCNWdyNuaWJxb2NtI3F2I29jaXpscXZvI0l2bCN4em1hbXpkcXZvI2JwbXUvI053eiNQbSNxYSNicG0jVXdhYiNQcW9wMSNCcG0jQWN4em11bSMrcXYjb3R3enwsMQ==
*/
#include <cstring>
#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <queue>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <cassert>

#define F first
#define S second
#define endl '\n'
#define deb(x) cout<<#x<<' '<<x<<endl;
#define pb push_back
#define int __int64


const long long MOD = 1e9 + 7;
const long long MAXN = 1e6 + 1;
using namespace std;

typedef long long ll;

long long readInt() {
    bool minus1 = false;
    long long result = 0;
    char ch;
    ch = getchar();
    while (true) {
        if (ch == '-') break;
        if (ch >= '0' && ch <= '9') break;
        ch = getchar();
    }
    if (ch == '-') minus1 = true; else result = ch-'0';
    while (true) {
        ch = getchar();
        if (ch < '0' || ch > '9') break;
        result = result*10 + (ch - '0');
    }
    if (minus1)
        return -result;
    else
        return result;
}


int t[MAXN * 4];
int sum[MAXN * 4];
int push[MAXN * 4];

void Push(int v, int tl, int tr) {
	if (push[v] != 0) {
		sum[v] += (tr - tl + 1)	 * push[v];
		if (tl != tr) {
			push[v * 2] += push[v];
			push[v * 2 + 1] += push[v];
		}
		if (t[v]) {
    		t[v * 2] = t[v * 2 + 1] = t[v];
  		}
		push[v] = 0;           
	}			
}

void build(int v, int tl, int tr) {
	if (tl == tr) {
		t[v] = tl;
		return;
	}
	int tm = (tl + tr) / 2;
	build(v * 2, tl, tm);
	build(v * 2 + 1, tm + 1, tr);
}

int get(int v, int tl, int tr, int l, int r) {
	Push(v, tl, tr);
	if (tr < l || tl > r) return 0;
	if (l <= tl && tr <= r) return sum[v];
	int tm = (tl + tr) / 2;
	return get(v * 2, tl, tm, l, r) + get(v * 2 + 1, tm + 1, tr, l, r);
} 

void upd(int v, int tl, int tr, int l, int r, int x) {
	Push(v, tl, tr);
	if (tr < l || tl > r) return;
	if (l <= tl && tr <= r && t[v]) {
		push[v] += abs(x - t[v]);				
		t[v] = x;
		Push(v, tl, tr);
		return;
	}
	int tm = (tl + tr) / 2;
	upd(v * 2, tl, tm, l, r, x);
	upd(v * 2 + 1, tm + 1, tr, l, r, x);
	t[v] = (t[v * 2] == t[v * 2 + 1] ? t[v * 2] : 0);
	sum[v] = sum[v * 2] + sum[v * 2 + 1];
}                    

 main() {
	#ifdef IZI_KATKA
	assert(freopen("input", "r", stdin));
    assert(freopen("output", "w", stdout));
    #endif
    int n = readInt(), m = readInt();
    build(1, 1, n);
    while (m--) {
		int type = readInt();
		int l = readInt(), r = readInt();
		if (type & 1) {
			int x = readInt();
			upd(1, 1, n, l, r, x);	
		} else {
			cout << get(1, 1, n, l, r) << "\n";		
		}    	
    }
    return 0;
}