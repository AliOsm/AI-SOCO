#include<bits/stdc++.h>
using namespace std;

typedef long long ll;
typedef pair<int,int> ii;

const int mx=500000;

int main() {
	cin.tie(0); cout.tie(0); ios_base::sync_with_stdio(0);
	vector<bool> prime(mx,true);
	prime[0]=prime[1]=false;
	for (int i=2; i*i<mx; i++)
		if(prime[i])
			for (int j=i; j*i<mx; j++)
				prime[i*j]=false;

	int n,a; cin>>n;
	int one=0, two=0;
	for (int i=0; i<n; i++) {
		cin>>a;
		if(a==1) one++;
		else two++;
	}

	int ret2=-1, ret=-1, mx=-1;
	for (int pre2=0; pre2<=min(2,two); pre2++)
	for (int pre=0; pre<=min(5,one); pre++) {
		int suf2=two-pre2, suf=one-pre, cur=0, ct=0;
		for (int i=0; i<pre2; i++) {
			cur+=2;
			if(prime[cur]) ct++;
		}

		for (int i=0; i<pre; i++) {
			cur+=1;
			if(prime[cur]) ct++;
		}

		for (int i=0; i<suf2; i++) {
			cur+=2;
			if(prime[cur]) ct++;
		}

		for (int i=0; i<suf; i++) {
			cur+=1;
			if(prime[cur]) ct++;
		}

		if(mx<ct)
			mx=ct, ret=pre, ret2=pre2;
	}
	for (int i=0; i<ret2; i++)
		cout << 2 << " ";
	for (int i=0; i<ret; i++)
		cout << 1 << " ";
	for (int i=0; i<two-ret2; i++)
		cout << 2 << " ";
	for (int i=0; i<one-ret; i++)
		cout << 1 << " ";
	cout << endl;
	return 0;
}
