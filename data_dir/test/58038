#include <bits/stdc++.h>
using namespace std;
string s;
int n,i,j;
int A[1000];

bool cek1(){
	bool temp=false;;
	for (i=65;i<=90;i++){
		if (A[i]>=1){
			temp=true;
			break;
		}
	}
	return temp;	
}
bool cek2(){
	bool temp=false;
	for (i=48;i<=57;i++){
		if (A[i]>=1){
			temp=true;
			break;
		}
	}
	return temp;
}
bool cek3(){
	bool temp=false;
	for (i=97;i<=122;i++){
		if (A[i]>=1){
			temp=true;
			break;
		}
	}
	return temp;
}
int main(){
	memset(A,0,sizeof(A));
	getline(cin,s);
	if (s.length()<5)
		cout<<"Too weak"<<endl;
	else{
	for (i=0;i<s.length();i++){
		A[int(s[i])]++;
	}
		if (cek1()&&cek2() &&cek3())
			cout<<"Correct"<<endl;
		else
			cout<<"Too weak"<<endl;
	}
}
