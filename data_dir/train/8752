#include <bits/stdc++.h>
using namespace std;
long long fpb(long long p,long long q){
	if (q==0)
		return p;
	else
		return fpb(q,p%q);
}
int main(){
	ios_base::sync_with_stdio(0);
	long long a,b,c,l,r,d,e,f;
	long long i,j,k;
	bool ditemukan=false;
	
	cin>>l>>r;
	i=l;
	while ((i<=r) && (!ditemukan))
		{
			j=i+1;
			while ((j<=r) && (!ditemukan))
				{
					k=j+1;
					while ((k<=r) && (!ditemukan))
						{
							if ((fpb(i,j)==1) && (fpb(j,k)==1) && (fpb(i,k)!=1))
								{
									cout<<i<<" "<<j<<" "<<k<<endl;
									ditemukan=true;
									break;
								}
							else
							k++;
						}
					j++;
				}
			i++;
		}
	if (ditemukan==false)
		cout<<-1<<endl;
	return 0;
}	