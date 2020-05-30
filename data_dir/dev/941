#include <bits/stdc++.h>

#define endl '\n'
#define ll long long int
#define let(x, a) __typeof(a) x(a)
#define all(a) (a).begin(), (a).end()
#define present(c, x) ((c).find(x) != (c).end())
#define tr(v, it) for (let(it, v.begin()); it != v.end(); it++)
#define rtr(v, it) for (let(it, v.rbegin()); it != v.rend(); it++)

#define trace1(x)					cerr << #x << ": " << x << endl;
#define trace2(x, y)				cerr << #x << ": " << x << " | " << #y << ": " << y << endl;
#define trace3(x, y, z)				cerr << #x << ": " << x << " | " << #y << ": " << y << " | " << #z << ": " << z << endl;
#define trace4(a, b, c, d)			cerr << #a << ": " << a << " | " << #b << ": " << b << " | " << #c << ": " << c << " | " << #d << ": " << d << endl;
#define trace5(a, b, c, d, e)		cerr << #a << ": " << a << " | " << #b << ": " << b << " | " << #c << ": " << c << " | " << #d << ": " << d << " | " << #e << ": " << e << endl;
#define trace6(a, b, c, d, e, f)	cerr << #a << ": " << a << " | " << #b << ": " << b << " | " << #c << ": " << c << " | " << #d << ": " << d << " | " << #e << ": " << e << " | " << #f << ": " << f << endl;

using namespace std;

class Point {
public:
	ll x,y,z,pos;

	Point(ll xx, ll yx, ll zx, ll pos1) {
		x=xx; y=yx; z=zx; pos=pos1;
	}

	Point() {}
};

bool cmp(Point a, Point b) {
	ll aa=1e10*a.x+1e5*a.y+a.z;
	ll bb=1e10*b.x+1e5*b.y+b.z;
	return aa<bb;
}

ll dist(Point a, Point b) {
	return (a.x-b.x)*(a.x-b.x)+(a.y-b.y)*(a.y-b.y)+(a.z-b.z)*(a.z-b.z);
}

int main() {
	ios::sync_with_stdio(false);
	int n,x,y,z;
	cin>>n;
	vector<Point> P;
	for(int i=0;i<n;i++) {
		cin>>x>>y>>z;
		P.push_back(Point(x,y,z,i+1));
	}
	//sort(all(P),cmp);
	vector<int> marked(n+1,0);
	vector<pair<ll,pair<int,int>>> V;
	for(int i=0;i<n;i++) {
		for(int j=i+1;j<n;j++) {
			ll d=dist(P[i],P[j]);
			//trace3(i,j,d);
			V.push_back({d, {i,j}});
		}
	}
	sort(all(V));
	for(auto v:V) {
		int i=v.second.first, j=v.second.second;
		if(marked[i] || marked[j]) continue;
		marked[i]=marked[j]=1;
		cout<<i+1<<" "<<j+1<<endl;
	}
	return 0;
}