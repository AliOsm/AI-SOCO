#include<bits/stdc++.h>
using namespace std;

int n,m,k;
char s[5][5];
bool eval(int x, int y, int m) {
	m/=n;
	return (m>0)&&(s[x/m][y/m]=='*'||eval(x%m,y%m,m));
}

int main() {
	ifstream fin("input.txt");
	ofstream fout("output.txt");
	fin>>n>>k;
	for (int i=0; i<n; i++)
		fin>>s[i];
	for (int i=m=1; i<=k; i++)
		m*=n;
	for (int i=0; i<m; i++) {
		for (int j=0; j<m; j++)
			fout << (eval(i,j,m) ? '*' : '.');
		fout << endl;
	}
	return 0;
}
