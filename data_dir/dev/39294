#include<bits/stdc++.h>

using namespace std;

typedef long long LL;
typedef unsigned long long uLL;
typedef long double ldb;
typedef pair<int,int> pii;

int main()
{
ios_base::sync_with_stdio(0);
	string a;
	int k;
	char t;
	cin>>a>>k;
	for(int i = 0; i < a.size(); ++i)
	{
		int m = i;
		for(int j = i+1; j <= i+k && j < a.size(); ++j)
		{
			if(a[j] > a[m])m = j;
		}
		k -= m - i;
		t = a[m];
		for(int j = m; j > i; --j)a[j] = a[j-1];
		a[i] = t;
	}
	cout<<a;
	return 0;
}
