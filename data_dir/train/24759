#include <bits/stdc++.h>
using namespace std;

int main() {
	int n; cin>>n;
	vector<int> a(n);
	for (int i=0; i<n; i++)
		cin>>a[i], a[i]%=2;
	stack<int> st;
	for (int i=0; i<n; i++)
		if (!st.empty()&&a[i]==st.top()) st.pop();
		else st.push(a[i]);
	cout<<(st.size()<=1?"YES":"NO")<<"\n";
	return 0;
}
