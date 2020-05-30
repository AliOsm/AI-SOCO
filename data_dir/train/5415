#include <bits/stdc++.h>
using namespace std;
int main(){
	int i,n,m,x;
	int jawaban[1000];
	int A[1000];
	
	memset(A,0,sizeof(A));
	cin>>n>>m;
	for (i=0;i<m;i++){
		cin>>x;
		for (int j=x;j<=n;j++){
			if (A[j]==0){
				jawaban[j]=x;
				A[j]=1;
			}	
		}
	}
	for (i=1;i<=n;i++){
		if (i!=n)
			cout<<jawaban[i]<<" ";
		else
			cout<<jawaban[i]<<endl;
	}
}
