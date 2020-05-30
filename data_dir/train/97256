/*-----Deep D. Savani------------
-------DAIICT,INDIA--------------
*/
#include<bits/stdc++.h>
#define pb push_back
#define ff first
#define ss second
#define mp make_pair
#define mod 1000000007
#define deb(x) cout<<#x<<" : "<<x<<endl;
#define deb2(x,y) cout<<#x<<" : "<<x<<"\t"<<#y<<" : "<<y<<endl;
#define deb3(x,y,z) cout<<#x<<" : "<<x<<"\t"<<#y<<" : "<<y<<"\t"<<#z<<" : "<<z<<endl;
#define nax 1000010
typedef long long ll;
	
using namespace std;
	
long long modulo(long long base,long long exponent,long long modulus);
long long choose(ll n,ll k);
ll inverse(ll a,ll m);


void build()
{
	
}
	
	
int main(){

    build();
	ll n,k;
	cin>>n>>k;
	set<ll> s;
	for(int i=0;i<n;i++)
	{
		ll temp=0;
		for(int j=0;j<k;j++)
		{
			ll x;
			scanf("%lld",&x);
			if(x==1)
			temp+=(ll)pow(2,j);
		}
		s.insert(temp);
	}

	bool flag=false;

	set<ll> :: iterator it,it2;
	vector<ll> a;
	for(it=s.begin();it!=s.end();it++)
	{
		a.pb(*it);
	}

	for(int i=0;i<a.size();i++)
	{
		//deb(a[i]);
		for(int j=i;j<a.size();j++)
		{
			if( (a[i]&a[j]) ==0)
				flag=true;
		}
	}

	if(flag)
		cout<<"YES";
	else
		cout<<"NO";

	return 0;
}
	
		
	
long long modulo(long long base,long long exponent,long long modulus)
{
    if(modulus ==1)
        return 0;
	
    long long result=1;
    base=base % modulus;
    while(exponent>0)
    {
        if(exponent%2==1)
        {
            result=(result*base) % modulus;

        }
        exponent=exponent>>1;
        base = (base*base) % modulus;
    }
        return result;
}
	
long long choose(ll n,ll k)
{
    if(k==0)  return 1;
    return (n* choose(n-1,k-1))/k;
}
	
void EE(ll a,ll b,ll &co1,ll &co2)
{
    if(a%b==0)
    {
        co1=0;
        co2=1;
        return;
    }
    EE(b,a%b,co1,co2);
    ll temp=co1;
    co1=co2;
    co2=temp-co2*(a/b);
}
	
ll inverse(ll a,ll m)
{
    ll x,y;
    EE(a,m,x,y);
    if(x<0) x+=m;
    return x;
}
