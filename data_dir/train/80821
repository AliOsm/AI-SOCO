#include<bits/stdc++.h>
#include <ext/pb_ds/assoc_container.hpp>
#include <ext/pb_ds/tree_policy.hpp>
using namespace __gnu_pbds;
using namespace std;
#define DEBUG
#ifdef DEBUG
#define debug(...) __f(#__VA_ARGS__, __VA_ARGS__)
	template <typename Arg1>
	void __f(const char* name, Arg1&& arg1){
		cerr << name << " : " << arg1 << std::endl;
	}
	template <typename Arg1, typename... Args>
	void __f(const char* names, Arg1&& arg1, Args&&... args){
		const char* comma = strchr(names + 1, ','); cerr.write(names, comma - names) << " : " << arg1<<" | ";__f(comma+1, args...);
	}
#else
#define debug(...)
#endif
#define FOR(i,a,b) 	for(int i=a;i<b;++i)
#define RFOR(i,a,b) 	for(int i=a;i>=b;--i)
#define ln 		"\n"
#define mp make_pair
#define pb push_back
#define sz(a)	ll(a.size())
#define F first
#define S second
#define all(c)	c.begin(),c.end()
#define trace(c,x) for(auto &x:c)
#define pii pair<ll,ll>
typedef long long ll;
typedef long double ld;
typedef	priority_queue<pii,std::vector<pii>,greater<pii> > revpr;

typedef tree<int,null_type,less<int>,rb_tree_tag,tree_order_statistics_node_update> pbds;
// ordered_set X
//K-th smallest
//*X.find_by_order(k-1)
//NO OF ELEMENTS < A
//X.order_of_key(A)

const int L=2e5+7;
int a[L][33], seg[4*L][33], k, size_of_base, power[6];
void build(int start = 1, int end = size_of_base, int index = 1)
{
	if(start >= end)
	{
		FOR(i,0,power[k])
		{
			FOR(j,0,k)
			{
				if(i & power[j])
					seg[index][i] += a[start][j];
				else 
					seg[index][i] -= a[start][j];
 			}
		}
		return;
	}
	int mid = (start + end)>>1;
	build(start, mid, index<<1);
	build(mid+1, end, (index<<1) + 1);
	FOR(i,0,power[k])seg[index][i] = min(seg[index<<1][i], seg[(index<<1) + 1][i]);
	return;
}
void update(int idx, int start = 1, int end = size_of_base, int index = 1)
{
	if(idx < start || idx > end)return;
	if(start == end && idx == start)
	{
		FOR(i,0,power[k])
		{
			seg[index][i] = 0;
			FOR(j,0,k)
			{
				if(i & power[j])
					seg[index][i] += a[start][j];
				else 
					seg[index][i] -= a[start][j];
 			}
		}
		return;
	}
	int mid = (start + end)>>1;
	update(idx, start, mid, index<<1);
	update(idx, mid+1, end, (index<<1) + 1);
	FOR(i,0,power[k])seg[index][i] = min(seg[index<<1][i], seg[(index<<1) + 1][i]);
	return;
}
ll query(int l, int r, int x, int start = 1, int end = size_of_base, int index = 1)
{
	if(start > r || end < l || start > end)return INT_MAX;
	if(l <= start && end <= r)return seg[index][x];
	int mid = (start + end)>>1;
	ll query_left = query(l, r, x, start, mid, index << 1);
	ll query_right = query(l, r, x, mid + 1, end, (index << 1) + 1);
	return min(query_left, query_right);
}
void pre()
{
	power[0] = 1;
	FOR(i,1,6)power[i] = power[i-1]*2;
}
int main()
{
		ios_base::sync_with_stdio(false);
	 	cin.tie(NULL);
	 	int operations, idx, l, r, type;
	 	ll ans, x, y;
	 	cin >> size_of_base >> k;
	 	FOR(i,1,size_of_base + 1)
	 		FOR(j,0,k)
	 			cin >> a[i][j];
	 	pre();
	 	build();
	 	cin >> operations;
	 	while(operations--)
	 	{
	 		cin >> type;
	 		if(type == 1)
	 		{
	 			cin >> idx;
	 			FOR(i,0,k)cin >> a[idx][i];
	 			update(idx);
	 		}
	 		else
	 		{
	 			cin >> l >> r;
	 			ans = INT_MIN;
	 			FOR(i,0,power[k])
	 			{
	 				x = query(l, r, i), y = query(l, r,(power[k] - 1 - i));
	 				ans = max(ans, abs(x + y));
	 			}
	 			cout<<ans<<ln;
	 		}
	 	}
		return 0;
}