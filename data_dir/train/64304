/*
ID: noszaly1
TASK: {TASK}
LANG: C++11               
*/

//Noszály Áron 11o Debreceni Fazekas Mihály Gimnázium

#include<iostream>
#include<vector>
#include<map>
#include<set>
#include<cassert>
#include<cassert>
#include<unordered_map>
#include<unordered_set>
#include<functional>
#include<queue>
#include<stack>
#include<cstring>
#include<algorithm>
#include<cmath>
#include<sstream>
#include<iomanip>
#include<cstdio>
#include<cstdlib>
#include<numeric>
using namespace std;

#define all(x) (x).begin(), (x).end()
#define pb push_back
#define xx first
#define yy second
#define sz(x) (int)(x).size()
#define gc getchar
#define IO ios_base::sync_with_stdio(false);cin.tie(0);cout.tie(0)
#define mp make_pair

typedef long long ll;
typedef unsigned long long ull;
typedef long double ld;

const double PI=acos(-1);

template<typename T> T getint() {
	T val=0;
	char c;
	
	bool neg=false;
	while((c=gc()) && !(c>='0' && c<='9')) {
		neg|=c=='-';
	}

	do {
		val=(val*10)+c-'0';
	} while((c=gc()) && (c>='0' && c<='9'));

	return val*(neg?-1:1);
}

int n, q;

const int maxn=100001, hgt=22;
vector<int> adj[maxn];
int par[maxn], b[maxn], lvl[maxn];
int kezdet[maxn], veg[maxn];
int dp[maxn][hgt];

int ID=0;

void dfs_lca(int x, int p=-1, int lev=0) {
	b[x]=1;
	kezdet[x]=ID++;
	par[x]=p;
	lvl[x]=lev;
	//cerr<<x<<" "<<kezdet[x]<<"?\n";
	for(auto i:adj[x]) {
		if(!b[i]) {
			dfs_lca(i,x,lev+1);
		}
	}
	
	b[x]=2;
	veg[x]=ID++;
}

void init_lca() {
	memset(dp, -1, sizeof dp);
	
	for(int i=1;i<=n;++i) {
		dp[i][0]=par[i];
	}
	
	for(int j=1;j<hgt;++j) {
		for(int i=1;i<=n;++i) {
			if(dp[i][j-1]!=-1) {
				dp[i][j]=dp[dp[i][j-1]][j-1];
			}
		}
	}
}

struct SegTree {
	vector<int> t;
	vector<pair<int,int>> tree;
	vector<int> lazy;
	
	SegTree(vector<int>& t_) {
		t=t_;
		tree.assign(4*sz(t), {0,0});
		lazy.assign(4*sz(t), -1);
	}
	
	void build() {
		build(1, 0, sz(t)-1);
	}
	
	pair<int,int> query(int i, int j) {
		if(i>j)  return make_pair(int(1e9), int(1e9));
		return query(1, 0, sz(t)-1, i, j);
	}
	
	private:
	
	inline pair<int,int> combine(pair<int,int> x, pair<int,int> y) {
		return min(x,y);
	}
	
	void propogate(int ind, int L, int R) {
		
	}
	
	void pull(int ind, int L, int R) {
		tree[ind]=combine(tree[2*ind], tree[2*ind+1]);
	}
	
	void build(int ind, int L, int R) {
		if(L==R) {
			tree[ind]={t[L], L};
		}else {
			build(2*ind, L, (L+R)/2);
			build(2*ind+1, (L+R)/2+1, R);
			
			pull(ind, L, R);
		}
	}
	
	pair<int,int> query(int ind, int L, int R, int i, int j) {
		if(R<i || j<L) return make_pair(int(1e9), int(1e9));
		
		if(i<=L && R<=j) {
			return tree[ind];
		}
			
		return combine(query(2*ind, L, (L+R)/2, i, j), query(2*ind+1, (L+R)/2+1, R, i, j));
	}
	
};


/*
int lca(int p, int q) {
	if(lvl[p]>lvl[q]) swap(p,q);
	for(int i=hgt-1;i>=0;i--) {
		if(dp[q][i]!=-1 && lvl[p]<=lvl[dp[q][i]]) q=dp[q][i];
	}
	
	if(p==q) return p;
	
	for(int i=hgt-1;i>=0;i--) {
		if(dp[q][i]!=-1 && dp[q][i]!=dp[p][i]) {
			p=dp[p][i];
			q=dp[q][i];
		}
	}
	
	return dp[p][0];
}
*/

int get_parent(int bal, int jobb, int egyik) {
	assert(bal<=jobb);
	if(kezdet[egyik]<=bal && jobb<=veg[egyik]) return egyik;
	if(dp[egyik][0]==-1) return 1;
	
	
	for(int i=21;i>=0;i--) {
		if(dp[egyik][i]!=-1 && !(kezdet[dp[egyik][i]]<=bal && jobb<=veg[dp[egyik][i]])) {
			egyik=dp[egyik][i];
		}
	}
	
	return dp[egyik][0];
}

int main() {
	IO;
	cin>>n>>q;
	for(int i=2;i<=n;++i) {
		int p;
		cin>>p;
		adj[p].push_back(i);
		adj[i].push_back(p);
	}
	
	dfs_lca(1);
	init_lca();
	
	vector<int> kezdetek(n), vegek(n);
	map<int,int> inv;
	for(int i=1;i<=n;++i){
		kezdetek[i-1]=kezdet[i];
		vegek[i-1]=-veg[i];
		inv[kezdet[i]]=i;
		inv[veg[i]]=i;
	}
	
	
	
	SegTree st(kezdetek), en(vegek);
	st.build();
	en.build();
	

	/*for(int i:kezdetek) {
		cerr<<i<<" ";
	}cerr<<"\n";*/
	
	for(int i=0;i<q;++i) {
		int a,b;
		cin>>a>>b;
		
		pair<int,int> ans={-1,0};
		
		auto bal=st.query(a-1, b-1);
		auto jobb=en.query(a-1, b-1);
		
		int legkisebb=bal.second+1;
		int legnagyobb=jobb.second+1;
		//cerr<<legkisebb<<" "<<legnagyobb<<"\n";
		
		auto bal1=min(st.query(a-1, legkisebb-2), st.query(legkisebb, b-1));
		auto jobb1=min(en.query(a-1, legkisebb-2), en.query(legkisebb, b-1));
		int elem1=(legkisebb==a?b:a);
		int x1=get_parent(bal1.first, -jobb1.first, elem1);
		//cerr<<bal1.first<<" "<<-jobb1.first<<" "<<elem1<<"\n";
		ans=max(ans, make_pair(lvl[x1], legkisebb));
		
		auto bal2=min(st.query(a-1, legnagyobb-2), st.query(legnagyobb, b-1));
		auto jobb2=min(en.query(a-1, legnagyobb-2), en.query(legnagyobb, b-1));
		int elem2=(legnagyobb==a?b:a);
		int x2=get_parent(bal2.first, -jobb2.first, elem2);
		ans=max(ans, make_pair(lvl[x2], legnagyobb));
		
		
		cout<<ans.second<<" "<<ans.first<<"\n";
	}
	
	return 0;
}
