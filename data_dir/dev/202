//Noszály Áron 8a Debreceni Fazekas Mihály Gimnázium

#include<bits/stdc++.h>
#include<cstdlib>

using namespace std;

typedef long long ll;
typedef unsigned long long ul;
typedef long double ld;

#define all(s) (s).begin(),(s).end()
#define pb push_back
#define IO ios_base::sync_with_stdio(false); cin.tie(0); cout.tie(0)
#define INF std::numeric_limits<int>::max()
#define MINF std::numeric_limits<int>::min()
#define tmax(a,b,c) max((a),max((b),(c)))
#define tmin(a,b,c) min((a),min((b),(c)))
#define vpii vector<pair<int,int>>
#define vpll vector<pair<ll,ll>>
#define mp make_pair
#define xx first
#define yy second

#ifndef ONLINE_JUDGE
#  define LOG(x) (cerr << #x << " = " << (x) << endl)
#else
#  define LOG(x) ((void)0)
#endif

const long double PI = acos(-1);

int d1[4][2]={{0,1},{1,0},{0,-1},{-1,0}};
int d2[8][2]={{1,0},{0,1},{0,-1},{-1,0},{1,1},{-1,1},{1,-1},{-1,-1}};
int n,m,len1,len2;
string elso;
int gans=0;
int val(string& curr)
{
	int szaml=1;
	int ans=0;
	for(int i=curr.size()-1;i>=0;i--)
	{
		ans+=(szaml*int(curr[i]-'0'));
		szaml*=7;
	}
	return ans;
}
void gen2(int j, string& curr)
{
	
	if(j==len2)
	{
		int oc[7];memset(oc, 0, sizeof(oc));
		for(auto i:elso)
		{
			oc[i-'0']++;
		}
		for(auto i:curr)
		{
			oc[i-'0']++;
		}
		bool ok=true;
		for(int i=0;i<7 && ok;++i)
		{
			if(oc[i]>1) ok=false;
		}
		if(!ok) return ;
		if(val(elso)>=n || val(curr)>=m) return ;
		
		gans++;
		return ;
	}
	
	for(int ii=0;ii<7;++ii)
	{
		char c=('0'+ii);
		curr.push_back(c);
		gen2(j+1, curr);
		curr.erase(curr.end()-1);
	}
}
void gen1(int i, string& curr)
{
	if(i==len1)
	{
		
		elso=curr;
		string masodik="";
		gen2(0,masodik);
		return ;
	}
	
	for(int ii=0;ii<7;++ii)
	{
		char c=('0'+ii);
		curr.push_back(c);
		gen1(i+1, curr);
		curr.erase(curr.end()-1);
	}
}



int main()
{
	IO;
	cin>>n>>m;
	len1=ceil(log(n)/log(7));
	len2=ceil(log(m)/log(7));
	if(len1==0) len1++;
	if(len2==0) len2++;
	
	
	if((len1+len2)>9)
	{
		cout<<"0\n";
		return 0;
	}
	string c="";
	gen1(0, c);
	cout<<gans<<"\n";
	return 0;
}

