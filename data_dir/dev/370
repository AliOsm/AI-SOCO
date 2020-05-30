#include <bits/stdc++.h>
using namespace std;

int maxNodo;
int g[7000005][2];
int cnt[7000005][2];

void add(string s){
	int u = 1;
	for(char c : s){
		c -= '0';
		if(!g[u][c]) g[u][c] = ++maxNodo;
		cnt[u][c]++;
		u = g[u][c];
	}
}

void remove(string s){
	int u = 1;
	for(char c : s){
		c -= '0';
		cnt[u][c]--;
		u = g[u][c];
	}
}

int query(string s){
	int u = 1, pos = 31, res = (int)bitset<32>(s).to_ulong();
	int n = res;
	// cout << s << " " << res << endl;
	for(char c : s){
		c -= '0';
		if(g[u][!c] and cnt[u][!c]){
			u = g[u][!c];
			res |= (1 << pos);
		}
		else{
			u = g[u][c];
			res &= ~(1 << pos);
		}
		pos--;
	}
	return max(n, res);
}

int main(){
	cout.sync_with_stdio(false);
	cin.tie(NULL);
	maxNodo = 1;

	int t; cin >> t;
	for(int caso = 0; caso < t; caso++){
		string op; cin >> op;
		int n; cin >> n;
		string s = bitset<32>(n).to_string();
		if(op == "+")
			add(s);
		else if(op == "-")
			remove(s);
		else
			cout << query(s) << endl;
	}

    return 0;
}