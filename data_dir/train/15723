#include <bits/stdc++.h>
using namespace std;
int main(){
	string s;
	int i,j,idx1=0,idx2=0;
	bool ditemukan=true;
	
	getline(cin,s);
	i=0;
	while ((i<s.length())&&(ditemukan)){
		if (((i==0)&&(s[i]=='4'))||((s[i]!='4') && (s[i]!='1')))
			ditemukan=false;
		else{
			if ((s[i]=='1') && (s[i+1]=='4')){
				if (i==s.length()-2)
					break;
				if ((s[i+2]=='1')){
					i=i+2;
				}
				else if (s[i+2]=='4'){
					i=i+3;
				}
				else if ((s[i]!='1') && (s[i]!='4')){
					ditemukan=false;
				}
			}
			else if (s[i]=='1'){
				i++;
			}
			else if ((s[i]!='1') && (s[i]!='4'))
				ditemukan=false;
			else if ((s[i]=='4') && (s[i-1]!='1'))
				ditemukan=false;
		}
	}
	if (ditemukan)
		cout<<"YES"<<endl;
	else
		cout<<"NO"<<endl;
}
