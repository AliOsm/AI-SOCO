#include<bits/stdc++.h>

using namespace std;

typedef long long LL;
typedef unsigned long long uLL;
typedef long double ldb;
typedef pair<int,int> pii;

int A[256],C[256];

int main()
{
    ios_base::sync_with_stdio(0);
    LL n;
    cin>>n;
    string s;
    cin>>s;
    LL ans = 0,cur=0,m=1,d=1;
    for(int i = s.size()-1; i >= 0; )
    {
    	LL digit = s[i]-'0';
    	int j;
    	for(j = 0; j <= i; ++j)
    	{
    		cur = 0;
    		if(s[j]=='0')continue;
    		int k;
    		for(k = j; k <= i && cur < n; ++k)
    		{
    			cur = cur*10 + s[k]-'0';
    		}
    		if(cur<n&&cur)break;
    	}
    	ans += cur * d;
    	i = min(j-1,i-1);
    	d *= n;
    }
    cout<<ans<<endl;
   	return 0;
}