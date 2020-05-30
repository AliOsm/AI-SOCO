#pragma GCC optimize("Ofast")
#pragma GCC target("sse,sse2,sse3,ssse3,sse4,popcnt,abm,mmx,avx,tune=native")
#pragma GCC optimize("unroll-loops")

#include<bits/stdc++.h>
#include <ext/pb_ds/assoc_container.hpp>
#include <ext/pb_ds/tree_policy.hpp>

using namespace std;
using namespace __gnu_pbds;

#define DEBUG
#ifdef DEBUG
#define debug(...) __f(#__VA_ARGS__, __VA_ARGS__)
	template <typename Arg1>
	void __f(const char* name, Arg1&& arg1)
	{
		cerr << name << " = " << arg1 << endl;
	}
	template <typename Arg1, typename... Args>
	void __f(const char* names, Arg1&& arg1, Args&&... args)
	{
		const char* comma = strchr(names + 1, ','); cerr.write(names, comma - names) << " = " << arg1 << " || ";
		__f(comma+1, args...);
	}
#else
#define debug(...)
#endif

template <class Ch, class Tr, class Container>
basic_ostream <Ch, Tr> & operator << (basic_ostream <Ch, Tr> & os, Container const& x) {
    os << "{ ";
    for(auto& y : x) os << y << " ; ";
    return os << "}";
}

template <class X, class Y>
ostream & operator << (ostream & os, pair <X, Y> const& p) {
	return os << "[ " << p.first << ", " << p.second << "]" ;
}

#define FAST_IO std::ios::sync_with_stdio(false); cin.tie(0); cout.tie(0);
#define ll long long int
#define pb push_back
#define mp make_pair
#define ld long double
#define sz(a) (ll)(a).size()
#define endl "\n"

// priority_queue<ll, vector<ll>, less<ll>>pq;     // Max Heap
// priority_queue<ll, vector<ll>, greater<ll>>pq;  // Min Heap

typedef tree<ll,null_type,less<ll>,rb_tree_tag,tree_order_statistics_node_update> ordered_set;
//K-th smallest
//cout << k << "kth (1 based indexing) smallest: " << *A.find_by_order(k - 1) << endl;
//NO OF ELEMENTS < X
//cout << "No of elements less than " << X << " are " << A.order_of_key(X) << endl;

int main()
{
	FAST_IO;

 	ll t;
 	cin >> t;
 	while(t--)
 	{
 		ll n, k;
 		cin >> n >> k;
 		ll a[n], b[n] = {0}, ans = 0, ind = -1, curr = 1;
 		for(int i=0;i<n;i++) cin >> a[i];
 		for(int i=1;i<n-1;i++) if(a[i] > a[i - 1] && a[i] > a[i + 1]) b[i] = 1;
 		for(int i=n-2;i>n-k;i--) curr += (b[i] == 1);
 		ans = curr; ind = n - k;
 		for(int i=n-k-1;i>=0;i--)
 		{
 			if(b[i + k - 1] == 1) curr -= 1;
 			if(b[i + 1] == 1) curr += 1;
 			if(curr >= ans)
 			{
 				ans = curr;
 				ind = i;
 			}
 		}
 		cout << ans << " " << ind + 1 << endl;
 	}   
    return 0;
}